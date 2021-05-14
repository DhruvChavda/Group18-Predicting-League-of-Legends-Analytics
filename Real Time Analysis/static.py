from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import requests
import csv

foreground = 'white'
background = '#313737'
fontfam = 'Fira Code'
filename = 'champion_abilities.csv'

# ability_P_url = 'http://ddragon.leagueoflegends.com/cdn/11.9.1/img/spell/AhriSeduce.png'
# img_P = requests.get(ability_P_url)
# file = open("src/abi_P.png", "wb")
# file.write(img_P.content)
# file.close()

rows= []
fields = []
with open(filename, 'r', encoding = 'utf8') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        if(row):
            rows.append(row)

print(rows[0][0])
nq = ""
nw = ""
ne = ""
nr = ""
np = ""

for row in rows:
    if(row[0] == 'Caitlyn'):
        nq = row[1]
        nw = row[2]
        ne = row[3]
        nr = row[4]
        np = row[5]
        break
print(nq, nw, ne, nr)
root = Tk()

# CONFIGURATIONS
for i in range(2):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)
root.configure(background = background)
# Fonts
fontStyle1 = tkFont.Font(family=fontfam, size=25)
fontStyle2 = tkFont.Font(family=fontfam, size=14)

# IMAGE LOADING
hero_img = ImageTk.PhotoImage(Image.open("G:/Sem_6/SE_Project/RTA/src/heros_images/Caitlyn.jpg"))
imgQ = ImageTk.PhotoImage(Image.open("G:/Sem_6/SE_Project/RTA/Images/9.3.1/img/spell/" + nq))
imgW = ImageTk.PhotoImage(Image.open("G:/Sem_6/SE_Project/RTA/Images/9.3.1/img/spell/" + nw))
imgE = ImageTk.PhotoImage(Image.open("G:/Sem_6/SE_Project/RTA/Images/9.3.1/img/spell/" + ne))
imgR = ImageTk.PhotoImage(Image.open("G:/Sem_6/SE_Project/RTA/Images/9.3.1/img/spell/" + nr))
imgP = ImageTk.PhotoImage(Image.open("G:/Sem_6/SE_Project/RTA/Images/9.3.1/img/passive/" + np))

# bg = ImageTk.PhotoImage(Image.open("G:/Sem_6/SE_Project/RTA/src/background/brick.jpg"))
# label1 = Label( root, image = bg)
# label1.grid(row = 0, column = 0)

# root.wm_attributes("-transparentcolor")



# UPPER FRAME
uf = Frame(root, bg = background)
uf.grid(row = 0, column = 0,  columnspan = 2)
title = Label(uf, text = "Ongoin Match", justify = CENTER, font = fontStyle1)
image = Label(uf, image = hero_img, justify = CENTER)
imageQ = Label(uf, image = imgQ)
imageW = Label(uf, image = imgW)
imageE = Label(uf, image = imgE)
imageR = Label(uf, image = imgR)
imageP = Label(uf, image = imgP)
player = Label(uf, text = "Active player : TOMMY_BHAI", font = fontStyle2)
champion_name = Label(uf, text = "Ahri : " + "Level 3", font = fontStyle2)
qlbl = Label(uf, text = "Q : " + "2", font = tkFont.Font(family=fontfam, size=10))
wlbl = Label(uf, text = "W : " + "3", font = tkFont.Font(family=fontfam, size=10))
elbl = Label(uf, text = "E : " + "3", font = tkFont.Font(family=fontfam, size=10))
rlbl = Label(uf, text = "R : " + "3", font = tkFont.Font(family=fontfam, size=10))
plbl = Label(uf, text = "P : " + "3", font = tkFont.Font(family=fontfam, size=10))
lane_suggestion = Label(uf, text = "Suggested Lane", font = tkFont.Font(family=fontfam, size=13))



# blank = Label(root, text = "\n", bg = background)
# blank.grid(row = 1, column = 0, sticky = W+E+N+S, columnspan = 2)
champion_abilities = Label(uf, text = "Champion Abilities", font = fontStyle2, justify = CENTER)



# LOWER FRAME
lf = Frame(root, bg = background)
lf.grid(row = 2, column = 0,  columnspan = 2, pady = (20, 0))

stats_label = Label(lf, text = "Stats", font = tkFont.Font(family = fontfam, size = 16))

total_kills = Label(lf, text = "Kills", font = fontStyle2)
deaths = Label(lf, text = "Deaths", font = fontStyle2)
assist = Label(lf, text = "Total Assists", font = fontStyle2)
minion = Label(lf, text = "Total Minions Killed", font = fontStyle2)
prediction = Label(lf, text = "Win Percentage", font = fontStyle2)

# Values
n_kills = Label(lf, text = "4", font = fontStyle2)
n_deaths = Label(lf, text = "1", font = fontStyle2)
n_assist = Label(lf, text = "3", font = fontStyle2)
n_minions = Label(lf, text = "60", font = fontStyle2)
n_win = Label(lf, text = "80.23", font = fontStyle2)


# CONFIGURING COLORS
wlist_upper = uf.winfo_children()
wlist_lower = lf.winfo_children()

for wid in wlist_upper:
    wid.configure(fg = foreground, bg = background)
for wid in wlist_lower:
    wid.configure(fg = foreground, bg = background)

n_kills = Label(lf, text = "4", font = fontStyle2, fg = 'light green', bg = background)
n_deaths = Label(lf, text = "1", font = fontStyle2, fg = 'dark orange', bg = background)
n_assist = Label(lf, text = "3", font = fontStyle2, fg = 'aqua', bg = background)
if(80 > 50):
    ween_c = 'light green'
else:
    ween_c = 'dark orange'
n_win = Label(lf, text = "80.23", font = fontStyle2, fg = ween_c, bg = background)


# Packing

# UPPER FRAME
title.grid(row = 0, column = 0, columnspan = 5, sticky=E+W+N+S, padx = 50, pady=(20, 0))

player.grid(row = 1, column = 0, sticky=E+W+N+S, columnspan = 5, pady = 20)
champion_name.grid(row = 2, column = 0, sticky=E+W+N+S, columnspan = 5)
image.grid(row = 3, column = 0, padx = 50, pady = 20, sticky=E+W+N+S, columnspan = 5)
# champion_abilities.grid(row = 4, column = 0, columnspan = 5, pady = 20, sticky = E+W+N+S)
imageQ.grid(row = 4, column = 0, padx = 5, pady = 20)
imageW.grid(row = 4, column = 1, padx = 5, pady = 20)
imageE.grid(row = 4, column = 2, padx = 5, pady = 20)
imageR.grid(row = 4, column = 3, padx = 5, pady = 20)
imageP.grid(row = 4, column = 4, padx = 5, pady = 20)
qlbl.grid(row = 5, column = 0, padx = 5)
wlbl.grid(row = 5, column = 1, padx = 5)
elbl.grid(row = 5, column = 2, padx = 5)
rlbl.grid(row = 5, column = 3, padx = 5)
plbl.grid(row = 5, column = 4, padx = 5)
lane_suggestion.grid(row = 6, column = 0, columnspan = 5, pady = 10)



# LOWER FRMAE
stats_label.grid(row = 0, column = 0, columnspan = 2, sticky=E+W+N+S, pady = (0,30))

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



root.mainloop()