import numpy as np
import pandas as pd
import json
import requests
import datetime

API_KEY = 'RGAPI-2aba161a-00a5-4b81-a1a2-1f0898283562'

def generateupcomingLeague():
    region_arr = ['br1','eun1', 'euw1', 'jp1', 
                  'kr', 'la1', 'la2', 'na1',
                  'oc1', 'ru', 'tr1', ]
    
    Leagueinfo = {}
    for region in region_arr:
        url = 'https://' + region + '.api.riotgames.com/lol/clash/v1/tournaments?api_key=' + API_KEY
        responce = requests.get(url)
        if responce.status_code == 200:
            details = responce.json()
            lis = []
            for res in details:
                vec = {}
                vec['tournamentId'] = res['id']
                vec['themeId'] = res['themeId']
                vec['nameKey'] = res['nameKey']
                vec['nameKeySecondary'] = res['nameKeySecondary']
                vec['schedule'] = {}

                # now active tournament phase fetch                
                vec['schedule']['tournamentPhaseId'] =  res['schedule'][0]['id']
                
                # this is for convert time and date in iso format
                ts = datetime.datetime.fromtimestamp(int(res['schedule'][0]['registrationTime']/1000)).isoformat()
                vec['schedule']['registrationTime'] = ts

                # this is for convert time and date in iso format
                ts = datetime.datetime.fromtimestamp(int(res['schedule'][0]['startTime']/1000)).isoformat()
                vec['schedule']['startTime'] = ts

                vec['schedule']['cancelled'] = res['schedule'][0]['cancelled']
                
                lis.append(vec)
            Leagueinfo[region] = lis

        else:
             pass
    
    # read all value in json file 
    file_name = 'upcomingLeagueInfo.json'
    with open(file_name, "w") as outfile:
        json.dump(Leagueinfo, outfile)


generateupcomingLeague()