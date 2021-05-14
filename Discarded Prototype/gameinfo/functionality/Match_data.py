import requests
import json
import time

API_KEY='Enter your API KEY'


def getsummonername(region, SummnorName):
    url = 'https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + SummnorName + '?api_key=' + API_KEY
    responce = requests.get(url)
    if  responce.status_code == 200:
        details = responce.json()
        return details
    else:
        return None, None

def get_match(region, AccountId):
    url = 'https://' + region + '.api.riotgames.com/lol/match/v4/matchlists/by-account/' + AccountId + '?api_key=' + API_KEY
    playerMatchListId = []
    responce = requests.get(url)
    if responce.status_code == 200:
        arr = responce.json()
        playerMatchList = [item['gameId'] for item in arr['matches']]
    return playerMatchList


def getMatchdataBymatchid(region, summnorname, match_id):    
    url = 'https://'+ region + '.api.riotgames.com/lol/match/v4/matches/' + str(match_id) + '?api_key=' + API_KEY
    responce = requests.get(url)

    if responce.status_code != 200:
        return None

    data = responce.json()
    player_id = 1
    team1 = []
    team2 = []
    for res in data['participantIdentities']:
        if res['participantId'] > 5 :
            team2.append(res['player']['summonerName'])
        else:
            team1.append(res['player']['summonerName']) 
        if res['player']['summonerName'].lower() == summnorname.lower():
            player_id = res['participantId']

    for res in data['participants']:
        if res['participantId'] == player_id:
            death = res['stats']['deaths']
            kill = res['stats']['kills']
            assist = res['stats']['assists']
            win = res['stats']['win']
            role = res['timeline']['role']
            lane = res['timeline']['lane']
            break

    match_data = {}
    match_data['matchid'] = match_id
    match_data['death'] = death
    match_data['kill'] = kill
    match_data['assist'] = assist
    match_data['role'] = role
    match_data['lane'] = lane
    match_data['win'] = win
    match_data['team1'] = team1
    match_data['team2'] = team2

    return match_data, win

def getmatchdata(region, summnorname):
    
    name = (summnorname.replace(" ", "%20")).lower()
    details = getsummonername(region, name)
    AccId = details['accountId']
    Match_List = get_match(region, AccId)

    print(len(Match_List))
    All_match_data = []
    winCnt = 0
    cnt = 0

    for match_id in Match_List:
        if cnt > 20:
            break
        matchdata, win = getMatchdataBymatchid(region, summnorname, match_id)
        if matchdata == None:
            time.sleep(1.3)
            continue
        All_match_data.append(matchdata)
        if win:
            winCnt = winCnt + 1
        cnt = cnt + 1
        time.sleep(1.3)
    
    playerdata = {}
    playerdata['matchdata'] = All_match_data
    
    try:
        playerdata['winrate'] = winCnt/cnt
    except:
        playerdata['winrate'] = winCnt/cnt

    return playerdata


