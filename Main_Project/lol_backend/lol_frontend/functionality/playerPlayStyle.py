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
        time.sleep(0.5)

    return players, laneDetails, roleDetails



def playStyle(region, username):
    
    #championId = pd.read_csv("lol_frontend/functionality/champion.csv", usecols = ["key"], squeeze = True).to_numpy()
    #championName = pd.read_csv("lol_frontend/functionality/champion.csv", usecols = ["name"], squeeze = True).to_numpy()
    
    # map champion name to champion id
    #mapper = {}
    #for i in range(championId.size):
    #  mapper[championId[i]] = championName[i]

    all_data = {}
    all_data['champion'] = []
    #all_data['championCnt'] = []
    all_data['lane'] = []
    #all_data['laneCnt'] = []
    all_data['role'] = []
    #all_data['roleCnt'] = []

    #return_username = (username.replace(" ", "%20")).lower() #riot API uses no space lower case verison of username as key
    #print("Username: ", username)
    #print('usenename  : ', return_username)

    #find account id by summonerName
    details = getBySummonerName(region, username)

    if details == None:
        return all_data    
    
    # get all details about champion, lane, role 
    arr = [[details['accountId']]]
    userChampionsList, laneList, roleList  = getPlayerChampionDict(region, arr)
    userChampionsList = userChampionsList[details['accountId']]   
    laneList = laneList[details['accountId']]   
    roleList = roleList[details['accountId']] 


    champ = list(userChampionsList.keys())
    # for mapping champion id to champion name
    champname = []
    for i in champ:
        try:
            champname.append(mapper[i])
        except:
            champname.append('Lol')
    # champname = [mapper[i] for i in champ]
    champMatch = list(userChampionsList.values())

    champdata = []
    for i in range(len(champname)):
        champdata.append([champname[i], champMatch[i]])
    champdata = sorted(champdata, key = lambda x: x[1], reverse=True)

    lane = list(laneList.keys())
    laneCnt = list(laneList.values())

    lanedata = []
    for i in range(len(lane)):
        lanedata.append([lane[i], laneCnt[i]])
    lanedata = sorted(lanedata, key = lambda x: x[1], reverse=True)

    role = list(roleList.keys())
    roleCnt = list(roleList.values())

    roledata = []
    for i in range(len(role)):
        roledata.append([role[i], roleCnt[i]])
    roledata = sorted(roledata, key = lambda x: x[1], reverse=True)

    
    all_data['champion'] = champdata
    all_data['role'] = roledata
    all_data['lane'] = lanedata

    return all_data
