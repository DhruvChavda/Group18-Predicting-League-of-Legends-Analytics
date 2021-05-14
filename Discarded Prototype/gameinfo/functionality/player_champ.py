import json
import requests
from scipy.stats import linregress
import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt
import bisect
import csv
import time
import sys


API_KEY = 'Enter your API KEY'



def getBySummonerName(region, SummnorName):
    url = 'https://' + region + '.api.riotgames.com/tft/summoner/v1/summoners/by-name/' + SummnorName + '?api_key=' + API_KEY
    responce = requests.get(url)
    if  responce.status_code == 200:
        details = responce.json()
        return details
    else:
        return None


def getPlayerMatchList(region, AccountId):
    url = 'https://' + region + '.api.riotgames.com/lol/match/v4/matchlists/by-account/' + AccountId + '?api_key=' + API_KEY
    playerMatchList = []
    responce = requests.get(url)
    if responce.status_code == 200:
        arr = responce.json()
        playerMatchList = arr['matches']
    return playerMatchList

def getPlayerChampionDict(region, PlayerList):
    print()
    print("player wise champion information collecting start...")
    
    players = {}
    SummnorDetails = []
    cnt = 0
    for list_arr in PlayerList:
        summnorId = list_arr[0]
        
        url = 'https://' + region + '.api.riotgames.com/tft/summoner/v1/summoners/' + summnorId + '?api_key=' + API_KEY
        responce = requests.get(url)
        if responce.status_code == 200:
            details = responce.json()
            Accountid = details['accountId']
            SummnorDetails = SummnorDetails + [ [details['accountId'], details['id'], details['name'], details['summonerLevel'], region]]

            playerMatchList = getPlayerMatchList(region, Accountid)
            
            matchListSize = len(playerMatchList)
            players.setdefault(Accountid, {})
            #lane.setdefault(Accountid, {})
            for match in playerMatchList:
                champion = match['champion']
                if champion in players[Accountid]:#.has_key(champion):
                    players[Accountid][champion] += 1.0
                else:
                    players[Accountid][champion] = 1.0
                
        else:
            pass
        #time.sleep(0.1)
        cnt = cnt + 1
        if cnt % 20 == 0:
            print('fetching continue: ', cnt)
    
    return players, SummnorDetails

def main(region, username):
    if username is None:
        print("A username is required")
        sys.exit()

    return_username = (username.replace(" ", "%20")).lower() #riot API uses no space lower case verison of username as key
    print("Username: ", username)
    print('usenename  : ', return_username)

    details = getBySummonerName(region, return_username)
    if details == None:
        print('this summnor name does not exits')
        sys.exit()
    
    arr = [[details['id']]]
    userChampionsList, _ = getPlayerChampionDict(region, arr)
    userChampionsList = userChampionsList[details['accountId']]    
    champ = list(userChampionsList.keys())
    champMatch = list(userChampionsList.values())


    championId = pd.read_csv("champion.csv", usecols = ["key"], squeeze = True).to_numpy()
    championName = pd.read_csv("champion.csv", usecols = ["name"], squeeze = True).to_numpy()
    
    mapper = {}
    for i in range(championId.size):
      mapper[championId[i]] = championName[i]
    champname = [mapper[i] for i in champ]
    

    #plot 1
    fig = plt.figure(figsize = (10, 5))
    plt.bar(champname, champMatch, width = 0.4)
    plt.xlabel("champion name", rotation='vertical')   
    plt.ylabel("No. of match")
    plt.show()

    #plot 2
    fig, ax = plt.subplots(figsize =(16, 9))
    ax.barh(champname, champMatch)
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_tick_params(pad = 5)
    ax.yaxis.set_tick_params(pad = 10)
    ax.grid(b = True, color ='grey',
            linestyle ='-.', linewidth = 0.5,
            alpha = 0.2)
    ax.invert_yaxis()
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                str(round((i.get_width()), 2)),
                fontsize = 10, fontweight ='bold',
                color ='grey')
    ax.set_title('champion played by player',
                loc ='left', )
    fig.text(0.9, 0.15, 'Lol', fontsize = 12,
            color ='grey', ha ='right', va ='bottom',
            alpha = 0.7)
    
    # Show Plot
    plt.show()

main('na1', 'Doublelift')