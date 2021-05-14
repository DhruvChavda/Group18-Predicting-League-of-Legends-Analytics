from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import requests
import joblib
from pandas import DataFrame as df
import csv
import ast
import os
import sys
import sklearn

# CREATING PATH FOR FILES
###########################################
def resource_path(relative):
    #print(os.environ)
    application_path = os.path.abspath(".")
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    #print(application_path)
    return os.path.join(application_path, relative)
###########################################


# CSV LOADING
###########################################
filename = resource_path("champion_abilities.csv")

rows= []
fields = []
with open(filename, 'r', encoding = 'utf8') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        if(row):
            rows.append(row)

filename = resource_path('champion.csv')
suggested_lane = {}
fields = []
with open(filename, 'r', encoding = 'utf8') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        if(row):
            tmp = {}
            tmp["roles"] = ast.literal_eval(row[6])
            tmp["lane"] = row[8]
            suggested_lane[row[1]] = tmp


###########################################


global player_name
player_name_req = requests.get('https://127.0.0.1:2999/liveclientdata/activeplayername', verify = resource_path('riotgames.pem'))
player_name = player_name_req.json()


all_players_url = 'https://127.0.0.1:2999/liveclientdata/playerlist'
all_players_req = requests.get(all_players_url, verify = resource_path('riotgames.pem'))
all_players = all_players_req.json()

global c_name
c_name = "NONE"

for x in all_players:
    if(x["summonerName"] == player_name):
        c_name = x["championName"]
        break
c_name_no_space = c_name
c_name_no_space = "".join(c_name_no_space.split())
champion_image_path = resource_path("heros_images/" + c_name + ".jpg")


Regression = joblib.load(resource_path('KDA_Regression.pkl'))

###########################################

foreground = 'white'
background = '#313737'
fontfam = 'Arial'

nq = ""
nw = ""
ne = ""
nr = ""
np = ""

for row in rows:
    if(row[0] == c_name_no_space):
        nq = row[1]
        nw = row[2]
        ne = row[3]
        nr = row[4]
        np = row[5]
        break

###########################################

root = Tk()
hero_img = ImageTk.PhotoImage(Image.open(champion_image_path))
imgQ = ImageTk.PhotoImage(Image.open(resource_path("spell/" + nq)))
imgW = ImageTk.PhotoImage(Image.open(resource_path("spell/" + nw)))
imgE = ImageTk.PhotoImage(Image.open(resource_path("spell/" + ne)))
imgR = ImageTk.PhotoImage(Image.open(resource_path("spell/" + nr)))
imgP = ImageTk.PhotoImage(Image.open(resource_path("passive/" + np)))
def update_images():
    global player_name
    global c_name
    all_players_url = 'https://127.0.0.1:2999/liveclientdata/playerlist'
    all_players_req = requests.get(all_players_url, verify = resource_path('riotgames.pem'))
    all_players = all_players_req.json()
    for x in all_players:
        if(x["summonerName"] == player_name):
            tmp_name = x["championName"]
            break

    if(c_name != tmp_name):
        c_name = tmp_name
        champion_image_path = resource_path("heros_images/" + c_name + ".jpg")

        nq = ""
        nw = ""
        ne = ""
        nr = ""
        np = ""

        c_name_no_space = c_name
        c_name_no_space = "".join(c_name_no_space.split())
        for row in rows:
            if(row[0] == c_name_no_space):
                nq = row[1]
                nw = row[2]
                ne = row[3]
                nr = row[4]
                np = row[5]
                break
            
        global hero_img
        global imgQ
        global imgW
        global imgE
        global imgR
        global imgP
        hero_img = ImageTk.PhotoImage(Image.open(champion_image_path))
        imgQ = ImageTk.PhotoImage(Image.open(resource_path("spell/" + nq)))
        imgW = ImageTk.PhotoImage(Image.open(resource_path("spell/" + nw)))
        imgE = ImageTk.PhotoImage(Image.open(resource_path("spell/" + ne)))
        imgR = ImageTk.PhotoImage(Image.open(resource_path("spell/" + nr)))
        imgP = ImageTk.PhotoImage(Image.open(resource_path("passive/" + np)))


def refresher():
    
    # DATA CALLS
    ###########################################
    url = 'https://127.0.0.1:2999/liveclientdata/playerscores?summonerName=' + player_name
    player_stats_req = requests.get(url , verify = resource_path('riotgames.pem'))

    game_stats_link = 'https://127.0.0.1:2999/liveclientdata/gamestats'
    game_stats_req = requests.get(game_stats_link, verify = resource_path('riotgames.pem'))

    act_url = 'https://127.0.0.1:2999/liveclientdata/activeplayer'
    active_player_details = requests.get(act_url , verify = resource_path('riotgames.pem'))

    active_player_details = active_player_details.json()
    game_stats = game_stats_req.json()
    player_stats = player_stats_req.json()
    ###########################################


    # ASSIGNING AND IMPORTING VARIABLES
    ###########################################
    global kills_var
    global deaths_var
    global assist_var
    global win_rate
    global minion_var
    global eta
    global hero_img
    global imgQ
    global imgW
    global imgE
    global imgR
    global imgP


    kills_var = player_stats["kills"]
    deaths_var = player_stats["deaths"]
    assist_var = player_stats["assists"]
    minion_var = player_stats["creepScore"]
    eta = game_stats["gameTime"]
    ###########################################


    # WIN PREDICTION
    ###########################################
    variables = ["kills", "deaths", "assists", "totminionskilled", "duration"]
    vals = [[kills_var, deaths_var, assist_var, minion_var, eta]]
    params = df(vals, columns = variables)
    win_rate = Regression.predict_proba(params)
    ###########################################

    # LANE PREDICTION
    ###########################################
    c_name_no_space = c_name
    c_name_no_space = "".join(c_name_no_space.split())
    lane_suggestion = suggested_lane[c_name_no_space]["lane"]
    role = suggested_lane[c_name_no_space]["roles"]
    ###########################################


    # CONFIGURATIONS
    ###########################################
    for i in range(2):
        root.columnconfigure(i, weight=1)
        root.rowconfigure(i, weight=1)
    root.configure(background = background)
    # Fonts
    fontStyle1 = tkFont.Font(family=fontfam, size=25)
    fontStyle2 = tkFont.Font(family=fontfam, size=12)
    ###########################################

    # IMAGE LOADING
    ###########################################
    update_images()
    ###########################################


    # UPPER FRAME
    ###########################################
    uf = Frame(root, bg = background)
    uf.grid(row = 0, column = 0,  columnspan = 2)
    roles = Label(uf, text = "Roles : " + role[0] + (", " + role[1] if len(role) > 1 else ""), font = fontStyle2)
    image = Label(uf, image = hero_img, justify = CENTER)
    imageQ = Label(uf, image = imgQ)
    imageW = Label(uf, image = imgW)
    imageE = Label(uf, image = imgE)
    imageR = Label(uf, image = imgR)
    imageP = Label(uf, image = imgP)
    player = Label(uf, text = "Active player : " + player_name, font = fontStyle2)
    champion_name = Label(uf, text = c_name + " : " + "Level " + str(active_player_details["level"]), font = fontStyle2)
    qlbl = Label(uf, text = "Q : " + str(active_player_details["abilities"]["Q"]["abilityLevel"]), font = tkFont.Font(family=fontfam, size=10))
    wlbl = Label(uf, text = "W : " + str(active_player_details["abilities"]["W"]["abilityLevel"]), font = tkFont.Font(family=fontfam, size=10))
    elbl = Label(uf, text = "E : " + str(active_player_details["abilities"]["E"]["abilityLevel"]), font = tkFont.Font(family=fontfam, size=10))
    rlbl = Label(uf, text = "R : " + str(active_player_details["abilities"]["R"]["abilityLevel"]), font = tkFont.Font(family=fontfam, size=10))
    plbl = Label(uf, text = "P", font = tkFont.Font(family=fontfam, size=10))
    lane_suggestion = Label(uf, text = "Suggested Lane : " + lane_suggestion, font = tkFont.Font(family=fontfam, size=13))
    ###########################################


    # blank = Label(root, text = "\n", bg = background)
    # blank.grid(row = 1, column = 0, sticky = W+E+N+S, columnspan = 2)
    # champion_abilities = Label(uf, text = "Champion Abilities", font = fontStyle2, justify = CENTER)



    # LOWER FRAME
    ###########################################
    lf = Frame(root, bg = background)
    lf.grid(row = 2, column = 0,  columnspan = 2, pady = (20, 0))

    stats_label = Label(lf, text = "Stats", font = tkFont.Font(family = fontfam, size = 16))

    total_kills = Label(lf, text = "Kills", font = fontStyle2)
    deaths = Label(lf, text = "Deaths", font = fontStyle2)
    assist = Label(lf, text = "Total Assists", font = fontStyle2)
    minion = Label(lf, text = "Total Minions Killed", font = fontStyle2)
    prediction = Label(lf, text = "Win Percentage", font = fontStyle2)

    # Values
    n_kills = Label(lf, text = kills_var, font = fontStyle2)
    n_deaths = Label(lf, text = deaths_var, font = fontStyle2)
    n_assist = Label(lf, text = assist_var, font = fontStyle2)
    n_minions = Label(lf, text = minion_var, font = fontStyle2)
    n_win = Label(lf, text = str(round(win_rate[0][1]*100, 2)), font = fontStyle2)
    ###########################################


    # CONFIGURING COLORS
    ###########################################
    wlist_upper = uf.winfo_children()
    wlist_lower = lf.winfo_children()

    for wid in wlist_upper:
        wid.configure(fg = foreground, bg = background)
    for wid in wlist_lower:
        wid.configure(fg = foreground, bg = background)

    n_kills = Label(lf, text = kills_var, font = fontStyle2, fg = 'light green', bg = background)
    n_deaths = Label(lf, text = deaths_var, font = fontStyle2, fg = 'dark orange', bg = background)
    n_assist = Label(lf, text = assist_var, font = fontStyle2, fg = 'aqua', bg = background)

    if(win_rate[0][1]*100 > 50.0):
        ween_c = 'light green'
    else:
        ween_c = 'dark orange'
    n_win = Label(lf, text = str(round(win_rate[0][1]*100, 2)), font = fontStyle2, fg = ween_c, bg = background)
    ###########################################

    # Packing
    ###########################################
    # UPPER FRAME
   

    player.grid(row = 0, column = 0, sticky=E+W+N+S, columnspan = 5, pady = 15)
    champion_name.grid(row = 1, column = 0, sticky=E+W+N+S, columnspan = 5)
    roles.grid(row = 2, column = 0, sticky=E+W+N+S, columnspan = 5)
    image.grid(row = 3, column = 0, padx = 50, pady = 15, sticky=E+W+N+S, columnspan = 5)
    # champion_abilities.grid(row = 4, column = 0, columnspan = 5, pady = 20, sticky = E+W+N+S)
    imageQ.grid(row = 4, column = 0, padx = 5, pady = 15)
    imageW.grid(row = 4, column = 1, padx = 5, pady = 15)
    imageE.grid(row = 4, column = 2, padx = 5, pady = 15)
    imageR.grid(row = 4, column = 3, padx = 5, pady = 15)
    imageP.grid(row = 4, column = 4, padx = 5, pady = 15)
    qlbl.grid(row = 5, column = 0, padx = 5)
    wlbl.grid(row = 5, column = 1, padx = 5)
    elbl.grid(row = 5, column = 2, padx = 5)
    rlbl.grid(row = 5, column = 3, padx = 5)
    plbl.grid(row = 5, column = 4, padx = 5)
    lane_suggestion.grid(row = 6, column = 0, columnspan = 5, pady = 10)



    # LOWER FRMAE
    stats_label.grid(row = 0, column = 0, columnspan = 2, sticky=E+W+N+S, pady = (0,20))

    total_kills.grid(row = 1, column = 0, sticky = W, pady = 5, padx = 30)
    deaths.grid(row = 2, column = 0, sticky=W, pady = 5, padx = 30)
    assist.grid(row = 3, column = 0, sticky=W, pady = 5, padx = 30)
    minion.grid(row = 4, column = 0, sticky=W, pady = 5, padx = 30)
    prediction.grid(row = 5, column = 0, sticky=W,pady = 5, padx = 30)

    n_kills.grid(row  = 1, column = 1, sticky=E, pady = 5, padx = 30)
    n_deaths.grid(row = 2, column = 1, sticky=E, pady = 5, padx = 30)
    n_assist.grid(row = 3, column = 1, sticky=E, pady = 5, padx = 30)
    n_minions.grid(row = 4, column = 1, sticky=E,pady = 5, padx = 30)
    n_win.grid(row = 5, column = 1, sticky=E, pady = 5, padx = 30)
    root.after(2000, refresher)
    ###########################################

refresher()
root.mainloop()




