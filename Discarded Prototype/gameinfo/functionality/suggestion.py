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


def getMasterPlayers(region):
    pass

def getChallengerPlayers(region):
    pass

def getBySummonerName(region, SummnorName):
    url = 'https://' + region + '.api.riotgames.com/tft/summoner/v1/summoners/by-name/' + SummnorName + '?api_key=' + API_KEY
    responce = requests.get(url)
    if  responce.status_code == 200:
        details = responce.json()
        return details
    else:
        return None

def getPlayerList(region):
    #masterPlayersList = getMasterPlayers(region)
    #challengerPlayersList = getChallengerPlayers(region)

    PlayerList = []

    tier_arr = ['DIAMOND', 'PLATINUM', 'GOLD', 'SILVER']
    division = 'I'
    for tier in tier_arr:
        url = 'https://' + region + '.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/' + tier + '/' + division + '?page=1&api_key=' + API_KEY
        responce = requests.get(url)
        if responce.status_code == 200:
            list_arr = responce.json()
            newplayer_arr = [ [i['summonerId'], i['summonerName'], i['tier'], region] for i in list_arr]
            PlayerList = PlayerList + newplayer_arr
            print("Get player list" , region, ' ' , tier, '  Done')
        else:
            print("Get player list" , region, ' ' , tier, ' ',responce.status_code)

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
            for match in playerMatchList:
                champion = match['champion']
                if champion in players[Accountid]:#.has_key(champion):
                    players[Accountid][champion] += 1.0/matchListSize
                else:
                    players[Accountid][champion] = 1.0/matchListSize
        else:
            pass
        #time.sleep(0.1)
        cnt = cnt + 1
        if cnt % 20 == 0:
            print('fetching continue: ', cnt)
    
    return players, SummnorDetails

def readFile(region):
    file_name = region + 'sample.json'
    data = {}
    try:
        file = open(file_name, 'r')
        data = json.loads(file.read())
        #data = json.loads(file)
        file.close()
    except:
        print("File could not open: " , file_name)
    return data

def mapperTOchampidToName():
    championId = pd.read_csv("champion.csv", usecols = ["key"], squeeze = True).to_numpy()
    championName = pd.read_csv("champion.csv", usecols = ["name"], squeeze = True).to_numpy()
    mapper = {}
    for i in range(championId.size):
      mapper[championId[i]] = championName[i]
    return mapper

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


def printReCommendations(recommendations, userChampionsList, AccountId, n):
    mapper = mapperTOchampidToName()
    sortUserChamp = sorted(userChampionsList[AccountId].items(), key = lambda x: x[1], reverse=True)
    
    Champ_Names = []
    Champ_names_pro = []
    Champ_Pro = []

    for i in sortUserChamp:
        try:
            nn = mapper[i[0]]
        except:
            nn = 'LOL'
        Champ_Names.append(nn)
        Champ_names_pro.append([nn, i[1]*100])
        Champ_Pro.append(i[1]*100)
    
    if len(recommendations) == 0:
        print('not enough match play to give suggesion')
        return
    
    
    bar_names = [i for i in Champ_Names]
    bar_prop = [i for i in Champ_Pro]
    bar_prop.sort()
    recommend_index = []


    N = n if n < len(recommendations) else len(recommendations)
    print('recommendations champion: ')

    for i in range(N):
        try:
            nn = mapper[int(recommendations[i][0])]
        except:
            nn = 'LOL'
        proportion = recommendations[i][1]
        print(nn, ': with proportion :', proportion)

        index = bisect.bisect(bar_prop, proportion * 100)
        bisect.insort(bar_prop, proportion * 100)

        bar_names.insert(len(bar_prop) - index - 1, nn)
        recommend_index.append(len(bar_prop) - index - 1)

    recomm_name = []
    recomm_pro = []
    for i in range(min(len(recommendations), 20)):
        try:
            nn = mapper[int(recommendations[i][0])]
        except:
            nn = 'LOL'
        proportion = recommendations[i][1]
        recomm_name.append(nn)
        recomm_pro.append(proportion)

    bar_prop.reverse()

    plt.figure(0)
    patches, texts = plt.pie(Champ_Pro, shadow = True, startangle = 90, radius = 0.7)
    plt.legend(patches, Champ_names_pro, loc="center left", bbox_to_anchor=(-0.18, 0.5), fontsize = 12)
    plt.title('Your current champion proportions')
    #bar chart of recommended champions
    plt.figure(1, figsize=(20,10))
    barlist = plt.bar(range(len(bar_prop)), bar_prop, 0.8, color = 'y')
    plt.xticks(np.arange(len(bar_prop)) + 0.8/2.0, bar_names, rotation='vertical', fontsize=8)
    plt.title("Recommended Champions with Predicted Proportions")
    plt.ylabel('Percent of Ranked Games (%)')
    plt.xlabel('Champion Name')
    #highlight recommendations
    for i in recommend_index:
        barlist[i].set_color('r')
    plt.show()
    
    
    
    #plot 2
    fig, ax = plt.subplots(figsize =(16, 9))
    ax.barh(Champ_Names, Champ_Pro)
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
    

    fig, ax = plt.subplots(figsize =(16, 9))
    ax.barh(recomm_name, recomm_pro)
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
    ax.set_title('Recommended Champions with Predicted Proportions',
                loc ='left', )
    fig.text(0.9, 0.15, 'Lol', fontsize = 12,
            color ='grey', ha ='right', va ='bottom',
            alpha = 0.7)
    
    # Show Plot
    plt.show()
    
    pass

def main(n , username, region):
    fetch_data = False

    if fetch_data:
        region_arr = ['br1', ]#'eun1', 'euw1', 'jp1', 
                      #'kr', 'la1', 'la2', 'na1',
                      #'oc1', 'ru', 'tr1', ]
        
        player_list = {}
        arr_list = []
        #playersChamp = {}
        SummnorDetails = []
        for region_name in region_arr:
            arr = getPlayerList(region_name)
            player_list[region_name + '_playerList'] = arr
            print(region_name ,' list crated')
            print()
            arr_list = arr_list + arr
            time.sleep(5) 

            champ_players, Details = getPlayerChampionDict(region_name, arr)
            #playersChamp = playersChamp + champ_players
            SummnorDetails = SummnorDetails + Details
            print(region_name, ' player champion list created')

            file_name = region_name + 'sample.txt'
            with open(file_name, 'w') as outfile:
                json.dump(champ_players, outfile)
            file_name = region_name + 'sample.json'
            with open(file_name, "w") as outfile:
                json.dump(champ_players, outfile)
        

        df = pd.DataFrame(arr_list) 
        df.to_csv('idOfPlayers.csv') 
        
        #df = pd.DataFrame(playersChamp) 
        #df.to_csv('playersChamp.csv') 
        
        df = pd.DataFrame(SummnorDetails) 
        df.to_csv('SummnorDetails.csv') 
            
    else:
        br1_players = readFile('br1')

    
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
    #print(userChampionsList)
    all_region_data = [br1_players]
    recommendations = getRecommendations(userChampionsList,
                                         details['accountId'],
                                         all_region_data)
    
    printReCommendations(recommendations, 
                         userChampionsList, 
                         details['accountId'],
                         n)



if __name__ == '__main__':
    main(5, 'doublelift', 'na1')