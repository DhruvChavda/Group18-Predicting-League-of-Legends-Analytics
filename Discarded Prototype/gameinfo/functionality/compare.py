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
    url = 'https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + SummnorName + '?api_key=' + API_KEY
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
    laneDetails = {}
    roleDetails = {}
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
            laneDetails.setdefault(Accountid, {})
            roleDetails.setdefault(Accountid, {})
            for match in playerMatchList:
                champion = match['champion']
                if champion in players[Accountid]:#.has_key(champion):
                    players[Accountid][champion] += 1.0
                else:
                    players[Accountid][champion] = 1.0
                
                lane = match['lane']
                role = match['role']

                if lane in laneDetails[Accountid]:
                    laneDetails[Accountid][lane] += 1.0
                else:
                    laneDetails[Accountid][lane] = 1.0

                if role in roleDetails[Accountid]:
                    roleDetails[Accountid][role] += 1.0
                else:
                    roleDetails[Accountid][role] = 1.0
        else:
            pass
        
        time.sleep(0.1)
        cnt = cnt + 1
        if cnt % 20 == 0:
            print('fetching continue: ', cnt)
    
    return players, laneDetails, roleDetails, SummnorDetails

def leagueInfo(region, summnorId):
    url = 'https://' + region + '.api.riotgames.com/lol/league/v4/entries/by-summoner/' + summnorId + '?api_key=' + API_KEY
    responce = requests.get(url)
    league = []

    if responce.status_code != 200:
        return league
    
    responce = responce.json()
    for row in responce:
        add = {}
        add['leagueId'] = row['leagueId']
        add['queueType'] = row['queueType']
        add['tier'] = row['tier']
        add['rank'] = row['rank']
        add['wins'] = row['wins']
        add['losses'] = row['losses']
        league.append(add)
    return league

def main(regionList, summnorNameList):
    
    championId = pd.read_csv("champion.csv", usecols = ["key"], squeeze = True).to_numpy()
    championName = pd.read_csv("champion.csv", usecols = ["name"], squeeze = True).to_numpy()
    
    mapper = {}
    for i in range(championId.size):
      mapper[championId[i]] = championName[i]

    compareList = {}

    for i in range(len(summnorNameList)):
        try:
            username = summnorNameList[i]
            region = regionList[i]
        except:
            username = summnorNameList[i]
            region = 'br1'
        
        return_username = (username.replace(" ", "%20")).lower() #riot API uses no space lower case verison of username as key

        # find Account id by summonerName
        details = getBySummonerName(region, return_username)
        if details == None:
            continue

        compareList.setdefault(username, {})
        compareList[username]['AccountId'] = details['accountId']
        compareList[username]['SummnorId'] = details['id']

        # get all details about champion, lane, role 
        arr = [[details['id']]]
        userChampionsList, laneList, roleList,  _ = getPlayerChampionDict(region, arr)
        userChampionsList = userChampionsList[details['accountId']]   
        laneList = laneList[details['accountId']]   
        roleList = roleList[details['accountId']]   

        
        #all thing sort to select 1st, 2nd, 3rd pref.
        userChampions = []
        lane = []
        role = []
        for key,value in userChampionsList.items():
            userChampions.append([key, value])
        for key,value in laneList.items():
            lane.append([key, value])
        for key,value in roleList.items():
            role.append([key, value])

        userChampions = sorted(userChampions, key = lambda x: x[1], reverse=True)
        lane = sorted(lane, key = lambda x: x[1], reverse=True)
        role = sorted(role, key = lambda x: x[1], reverse=True)

        try:
            compareList[username]['1st_Champion'] =  mapper[userChampions[0][0]]
        except:
            compareList[username]['1st_Champion'] = None
            
        try:
            compareList[username]['2nd_Champion'] = mapper[userChampions[1][0]]
        except:
            compareList[username]['2nd_Champion'] = None
        
        try:
            compareList[username]['3rd_Champion'] = mapper[userChampions[2][0]]
        except:
            compareList[username]['3rd_Champion'] = None

        try:
            compareList[username]['1st_lane'] = lane[0][0]
        except:
            compareList[username]['1st_lane'] = None
        try:
            compareList[username]['2nd_lane'] = lane[1][0]
        except:
            compareList[username]['2nd_lane'] = None

        try:
            compareList[username]['1st_role'] = role[0][0]
        except:
            compareList[username]['1st_role'] = None

        try:
            compareList[username]['2nd_role'] = role[1][0]
        except:
            compareList[username]['2nd_role'] = None

        league = leagueInfo(region, details['id'])
        compareList[username]['league'] = league
        time.sleep(1)


    for row in compareList:
        print('...............')
        print(row)
        print(compareList[row])
        print('...............')
        print()

    #print(compareList)


main(['na1'], ['Doublelift'])
print()
main(['na1', 'br1', 'la1', 'oc1'], ['Doublelift', 'just gap mid', 'Faststroke', 'C1ock'])

#{   "region":  ["na1", "br1", "la1", "oc1"] , "player" : ["Doublelift", "just gap mid", "Faststroke", "C1ock"]  }