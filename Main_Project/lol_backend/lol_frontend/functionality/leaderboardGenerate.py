import pandas as pd
import numpy as np
import time
import requests
import json
from lol_frontend.variable import *

#API =  'RGAPI-2aba161a-00a5-4b81-a1a2-1f0898283562'


def generateLeaderBoard(region , league, queue):
    url = 'https://' + region + '.api.riotgames.com/lol/league/v4/'+ league + '/by-queue/' + queue + '?api_key=' + DEV_API
    responce = requests.get(url)
    leaderboard = []
    if responce.status_code != 200:
        print(region , ' ', league, ' ' , queue, ' not done!!')
        return leaderboard
  
    responce = responce.json()
    for row in responce['entries']:
        summonerName = row['summonerName']
        leaguePoints = row['leaguePoints']
        win = row['wins']
        loss = row['losses']
        winrate = win * 100 / (win + loss)
        val =[summonerName, leaguePoints, win, loss, winrate]
        leaderboard.append(val)

    leaderboard = sorted(leaderboard, key = lambda x: x[1], reverse=True)
    return leaderboard


def callTogenerate():
    
    leagues_arr = ['challengerleagues', 
                   'grandmasterleagues',
                   'masterleagues']

    queue_arr = ['RANKED_SOLO_5x5', 
                 'RANKED_FLEX_SR',]
                 #'RANKED_FLEX_TT']  #for this queue in api data not found so now we not generate leaderboard for this queue

    region_arr = ['br1', 'eun1', 'euw1', 'jp1', 
                  'kr', 'la1', 'la2', 'na1',
                  'oc1', 'ru', 'tr1', ]

    leaderboard = {}
    
    for region in region_arr:

        #print('...............')
        #print(region , ' leaderboard generating start !!! ')
        #print('...............')
        
        for league in leagues_arr:
            for queue in queue_arr:
                getleader = generateLeaderBoard(region, league, queue)
                leaderboard[ region + '_'+league + '_' + queue ] = getleader
                time.sleep(1.2)
        time.sleep(3)
    
    #print('...............')
    #print(' all thing done!! ')
    #print('...............')
    
    file_name = 'leaderboard.json'
    with open(file_name, "w") as outfile:
        json.dump(leaderboard, outfile)


#{  "region" : "br1" , "queue": "RANKED_SOLO_5x5" , "league":"challengerleagues" }