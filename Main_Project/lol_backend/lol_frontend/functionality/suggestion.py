import json
import requests
from scipy.stats import linregress
import numpy as np
import pandas as pd
import csv
import time
from lol_frontend.variable import *
from lol_frontend.models import summonerDetails

#API_KEY = 'RGAPI-cb7a554d-39e5-4a73-9422-9a6c16715b95'


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

def getPlayerList(region):
    
    PlayerList = []
    tier_arr = ['DIAMOND', 'PLATINUM', 'GOLD', 'SILVER']
    division = 'I'
    
    for tier in tier_arr:
        url = 'https://' + region + '.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/' + tier + '/' + division + '?page=1&api_key=' + DEV_API
        responce = requests.get(url)
        if responce.status_code == 200:
            list_arr = responce.json()
            newplayer_arr = [ [i['summonerId'], i['summonerName'], i['tier'], region] for i in list_arr]
            PlayerList = PlayerList + newplayer_arr

    return PlayerList

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
                players[Accountid][champion] += 1.0/matchListSize
            else:
                players[Accountid][champion] = 1.0/matchListSize
            
            if lane in laneDetails[Accountid]:
                laneDetails[Accountid][lane] += 1.0/matchListSize
            else:
                laneDetails[Accountid][lane] = 1.0/matchListSize

            if role in roleDetails[Accountid]:
                roleDetails[Accountid][role] += 1.0/matchListSize
            else:
                roleDetails[Accountid][role] = 1.0/matchListSize
            
        time.sleep(1.4)
        
        #cnt = cnt + 1
        #if cnt % 20 == 0:
        #    print('fetching continue: ', cnt)
    
    return players, laneDetails, roleDetails


def getRecommendations(userChampionsList, AccountId, all_region_data):
    similarityList = [{} for _ in range(len(all_region_data))]

    for i in range(len(all_region_data)):
        cnt = 1
        for id, player_matches in all_region_data[i].items():

            if id != AccountId:
                x = [] 
                y = []
                for champion in userChampionsList[AccountId].keys():  #champion in int format
                    if str(champion) in player_matches.keys(): # in player_matches champion in str format
                        x.append(userChampionsList[AccountId][champion])
                        y.append(player_matches[str(champion)])
                
                if len(x)>9 and max(y) > 0.01:
                    similarityList[i][id] = linregress(x,y)[2]    
            

    totals = {}
    similaritySums = {}
    for i in range(len(all_region_data)):
        for id, player_matches in all_region_data[i].items():
            if id == str(AccountId) or id not in similarityList[i].keys():
                continue
            player_similarity = similarityList[i][id]
            if player_similarity < 0:
                continue
            
            for champion, proportion in player_matches.items():
                if int(champion) not in userChampionsList.keys() or (int(champion) in userChampionsList.keys() and userChampionsList[int(champion)] < 0.01):
                    #print(champion)
                    totals.setdefault(champion, 0)
                    totals[champion] += player_similarity * player_matches[str(champion)]
                    similaritySums.setdefault(champion, 0)
                    similaritySums[champion] += player_similarity

    #by calculating the total of player_similarity*player_proportion/sum_of_similarity, we can get predicted proportion
    predicted_proportions = [(champion, total/similaritySums[champion]) for champion, total in totals.items()]
    predicted_proportions.sort(key = lambda x: x[1], reverse = True) #sort using the the second term in 2-tuple
    return predicted_proportions



def fetch_data():
    region_arr = ['br1', ]#'eun1', 'euw1', 'jp1', 
                    #'kr', 'la1', 'la2', 'na1',
                    #'oc1', 'ru', 'tr1', ]

    player_list = {}
    arr_list = []
    SummnorDetails = []

    for region_name in region_arr:
        
        #all the summnor name fetch tier wise
        arr = getPlayerList(region_name)
        player_list[region_name + '_playerList'] = arr    
        print(region_name ,' list crated')
        time.sleep(3) 

        lis = []
        #now fetch summnor account id for getting player matchlist
        for player in arr:
            SummnorName = player[1]
            tier = player[2]
            details = getBySummonerName(region_name, SummnorName)
            
            if details is None:
                continue    
            lis = lis + [ [details['accountId'], details['id'], details['name'], details['summonerLevel'], tier, region_name]]

        SummnorDetails = SummnorDetails + lis
        userChampionsList, laneList, roleList = getPlayerChampionDict(region_name, lis)
        
        print(region_name, ' player champion list created')
        file_name = region_name + 'sample.json'
        with open(file_name, "w") as outfile:
            json.dump(userChampionsList, outfile)
        
    df = pd.DataFrame(SummnorDetails) 
    df.to_csv('SummnorDetails.csv')

    

def generatesuggestion(region, username):

    # for returen this variable
    suggestion = {}
    suggestion['recommand'] = []
    suggestion['used'] = []

    recommand = [] 
    used = []
    
    #return_username = (username.replace(" ", "%20")).lower() #riot API uses no space lower case verison of username as key
    #print("Username: ", username)
    #print('usenename  : ', return_username)

    details = getBySummonerName(region, username)
    if details == None:
        return suggestion
    

    arr = [[details['accountId']]]
    #get player champion propotins info
    userChampionsList, _, _ = getPlayerChampionDict(region, arr)
   
    all_region_data = [br1_DATA]
    recommendations = getRecommendations(userChampionsList,
                                         details['accountId'],
                                         all_region_data)
    
    
    sortUserChamp = sorted(userChampionsList[details['accountId']].items(), key = lambda x: x[1], reverse=True)

    
    #map champion id to its name    
    for res in recommendations:
        try:
            champ = mapper[int(res[0])]
        except:
            champ = 'None'
        recommand.append([champ, res[1]] )

    for res in sortUserChamp:
        try:
            champ = mapper[int(res[0])]
        except:
            champ = 'None'
        used.append([champ, res[1]] )
    
    
    try:
        suggestion['recommand'] = recommand[0:11]
    except:
        suggestion['recommand'] = recommand

    try:    
        suggestion['used'] = used[0:11]
    except:
        suggestion['used'] = used

    return suggestion

