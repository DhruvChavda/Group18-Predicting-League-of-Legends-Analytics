import json
import requests
import numpy as np
import pandas as pd
import csv
import time
from lol_frontend.variable import *
from lol_frontend.models import summonerDetails

#API_KEY = 'RGAPI-2aba161a-00a5-4b81-a1a2-1f0898283562'


def detailsfromDB(summnorname, data):
    details = {}
    details['id'] = data['summonerid']
    details['accountId'] = data['accountid']
    details['name'] = data['summonername']
    return details

def getBySummonerName(region, SummnorName):
    SummnorName = SummnorName.lower()   #so comapre value with our database
    SummnorName = SummnorName.lstrip()
    
    try:
        fetchdb = list(summonerDetails.objects.filter(region=region, summonername=SummnorName).values())
        if len(fetchdb) != 0:
            return detailsfromDB(SummnorName, fetchdb[0])
    except:
        pass
    
    SummnorName = SummnorName.replace(" ", "%20") #riot API uses no space 
    # put rate api limit
    time.sleep(1.3)
    
    url = 'https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + SummnorName + '?api_key=' + API_KEY
    responce = requests.get(url)
    if  responce.status_code == 200:
        details = responce.json()
        
        try:
            dbpush = summonerDetails(summonername=details['name'].lower(),
                                    region=region,
                                    summonerid=details['id'],
                                    accountid=details['accountId'])
            dbpush.save()
        except:
            pass

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
    
    players = {}
    laneDetails = {}
    roleDetails = {}
    cnt = 0

    #iterate all the player id get all info
    for list_arr in PlayerList:
        Accountid = list_arr[0]
        
        # get match list played by summnor
        playerMatchList = getPlayerMatchList(region, Accountid)
        matchListSize = len(playerMatchList)

        #set Accountid as a key in a all map
        players.setdefault(Accountid, {})
        laneDetails.setdefault(Accountid, {})
        roleDetails.setdefault(Accountid, {})

        #now iterate all the matchid and count champion and lane details and also get role 
        for match in playerMatchList:

            #fetch champion , lane, role name for current gameid
            champion = match['champion']
            lane = match['lane']
            role = match['role']

            if champion in players[Accountid]:
                players[Accountid][champion] += 1.0
            else:
                players[Accountid][champion] = 1.0
            
            if lane in laneDetails[Accountid]:
                laneDetails[Accountid][lane] += 1.0
            else:
                laneDetails[Accountid][lane] = 1.0

            if role in roleDetails[Accountid]:
                roleDetails[Accountid][role] += 1.0
            else:
                roleDetails[Accountid][role] = 1.0

        # for rate limit of riot api        
        time.sleep(1.3)

    return players, laneDetails, roleDetails

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
        add['leaguePoints'] = row['leaguePoints']
        add['tier'] = row['tier']
        add['rank'] = row['rank']
        add['wins'] = row['wins']
        add['losses'] = row['losses']
        league.append(add)
    return league


def compare(regionList, summnorNameList):
    
    #championId = pd.read_csv("lol_frontend/functionality/champion.csv", usecols = ["key"], squeeze = True).to_numpy()
    #championName = pd.read_csv("lol_frontend/functionality/champion.csv", usecols = ["name"], squeeze = True).to_numpy()
    
    # map champion name to champion id
    #mapper = {}
    #for i in range(championId.size):
    #  mapper[championId[i]] = championName[i]


    compareList = {}

    for i in range(len(summnorNameList)):
        try:
            username = summnorNameList[i]
            region = regionList[i]
        except:
            username = summnorNameList[i]
            region = 'br1'
        
        #return_username = (username.replace(" ", "%20")).lower() #riot API uses no space lower case verison of username as key

        # find Account id by summonerName
        details = getBySummonerName(region, username)
        if details == None:
            continue

        compareList.setdefault(username, {})
        compareList[username]['AccountId'] = details['accountId']
        compareList[username]['SummnorId'] = details['id']

        # get all details about champion, lane, role 
        arr = [[details['accountId']]]
        userChampionsList, laneList, roleList  = getPlayerChampionDict(region, arr)
        userChampionsList = userChampionsList[details['accountId']]   
        laneList = laneList[details['accountId']]   
        roleList = roleList[details['accountId']]   

        
        #all thing sort to select 1st, 2nd, 3rd pref.
        userChampions = []
        lane = []
        role = []

        #convert map to 2D arrays
        for key,value in userChampionsList.items():
            userChampions.append([key, value])

        for key,value in laneList.items():
            lane.append([key, value])
        
        for key,value in roleList.items():
            role.append([key, value])

        
        #sort all the things based how many times used in the match
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

    return compareList
