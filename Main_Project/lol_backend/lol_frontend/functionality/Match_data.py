import requests
import json
import time
from lol_frontend.variable import *
from lol_frontend.models import summonerDetails, MatchDataByGameId

#API_KEY='RGAPI-6af592dd-645d-4440-91f7-4d0adf3a4e9e'

def detailsfromDB(summnorname, data):
    details = {}
    details['id'] = data['summonerid']
    details['accountId'] = data['accountid']
    details['name'] = data['summonername']
    return details

def getsummonername(region, SummnorName):
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


def get_match(region, AccountId):
    url = 'https://' + region + '.api.riotgames.com/lol/match/v4/matchlists/by-account/' + AccountId + '?api_key=' + API_KEY
    playerMatchListId = []
    responce = requests.get(url)
    if responce.status_code == 200:
        arr = responce.json()
        playerMatchList = [item['gameId'] for item in arr['matches']]
    return playerMatchList


def dbtodata(summnorname, data):
    
    matchdata = {}
    matchdata['matchid'] = data['matchId']
    matchdata['death'] = 0
    matchdata['kill'] = 0
    matchdata['assist'] = 0
    matchdata['role'] = 'DUO'
    matchdata['lane'] = 'MIDDLE'
    matchdata['win'] = False
    team1 = []
    team2 = []

    for key in data:
        val = data[key]
        if key == 'id' or key == 'matchId' or key == 'region':
            continue

        res = val.split('@')
        res[0] = res[0].lstrip()
        if res[0].lower() == summnorname.lower():
            matchdata['death'] = int(res[1])
            matchdata['kill'] = int(res[2])
            matchdata['assist'] = int(res[3])
            matchdata['role'] = res[5]
            matchdata['lane'] = res[6]
            if res[4] == 'True':
                matchdata['win'] = True
            else:
                matchdata['win'] = False

        id = int(key[6:])
        if id > 5:
            team2.append(res[0])
        else:
            team1.append(res[0])
    matchdata['team1'] = team1
    matchdata['team2'] = team2
    return matchdata


def getMatchdataBymatchid(region, summnorname, match_id):    
    
    try:
        fetchdb = list(MatchDataByGameId.objects.filter(region=region, matchId=match_id).values())
        if len(fetchdb) != 0:
            return dbtodata(summnorname, fetchdb[0])
    except:
        pass
    
    time.sleep(1.3)
    url = 'https://'+ region + '.api.riotgames.com/lol/match/v4/matches/' + str(match_id) + '?api_key=' + API_KEY
    responce = requests.get(url)

    if responce.status_code != 200:
        return None
    
    data = responce.json()
    player_id = 1
    team1 = []
    team2 = []
    uploaddata = {}

    for res in data['participantIdentities']:
        if res['participantId'] > 5 :
            team2.append(res['player']['summonerName'])
        else:
            team1.append(res['player']['summonerName']) 
        if res['player']['summonerName'].lower() == summnorname.lower():
            player_id = res['participantId']

        uploaddata[res['participantId']] = res['player']['summonerName']

    match_data = {}
    match_data['matchid'] = match_id

    for res in data['participants']:
        death = res['stats']['deaths']
        kill = res['stats']['kills']
        assist = res['stats']['assists']
        win = res['stats']['win']
        role = res['timeline']['role']
        lane = res['timeline']['lane']

        if res['participantId'] == player_id:
            match_data['death'] = death
            match_data['kill'] = kill
            match_data['assist'] = assist
            match_data['role'] = role
            match_data['lane'] = lane
            match_data['win'] = win
      
        uploaddata[res['participantId']] = uploaddata[res['participantId']] + '@' + str(death) + '@' + str(kill) + '@' + str(assist) + '@' + str(win) + '@' + str(role) + '@' + str(lane)

    try:
        dbdata = MatchDataByGameId(matchId = match_id,
                                    region = region,
                                    player1= uploaddata[1],
                                    player2= uploaddata[2],
                                    player3= uploaddata[3],
                                    player4= uploaddata[4],
                                    player5= uploaddata[5],
                                    player6= uploaddata[6],
                                    player7= uploaddata[7],
                                    player8= uploaddata[8],
                                    player9= uploaddata[9],
                                    player10=uploaddata[10],
                                    )
        dbdata.save()
    except:
        pass

    match_data['team1'] = team1
    match_data['team2'] = team2
    
    return match_data


def getmatchdata(region, summnorname):
    
    playerdata = {}
    playerdata['matchdata'] = []
    playerdata['winrate'] = []

    details = getsummonername(region, summnorname)
    
    if details == None:
        return playerdata
    
    AccId = details['accountId']
    Match_List = get_match(region, AccId)

    All_match_data = []
    winCnt = 0
    cnt = 0

    for match_id in Match_List:
        if cnt > 10:
            break
        matchdata = getMatchdataBymatchid(region, summnorname, match_id)
        if matchdata == None:
            continue
        All_match_data.append(matchdata)
        if matchdata['win']:
            winCnt = winCnt + 1
        cnt = cnt + 1
    
    playerdata = {}
    playerdata['matchdata'] = All_match_data
    
    try:
        playerdata['winrate'] = round(winCnt/cnt * 100, 2)
    except:
        playerdata['winrate'] = 0

    return playerdata


