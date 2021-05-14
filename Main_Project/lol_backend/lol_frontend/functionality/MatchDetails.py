import requests,json
import csv
import time
API_KEY='RGAPI-f33d988c-039e-424e-9f28-82e6b2c327e4'
json_arr=[]
def MatchDetails(match_id):
    url = 'https://na1.api.riotgames.com/lol/match/v4/matches/'+str(match_id)+'?api_key=' + API_KEY
    response = requests.get(url)
    data = json.loads(response.text)
    data1={
        "Game_ID": match_id,
        "t1_ban1": data["teams"][0]["bans"][0]["championId"],
        "t1_ban2": data["teams"][0]["bans"][1]["championId"],
        "t1_ban3": data["teams"][0]["bans"][2]["championId"],
        "t1_ban4": data["teams"][0]["bans"][3]["championId"],
        "t1_ban5": data["teams"][0]["bans"][4]["championId"],
        "t2_ban1": data["teams"][1]["bans"][0]["championId"],
        "t2_ban2": data["teams"][1]["bans"][1]["championId"],
        "t2_ban3": data["teams"][1]["bans"][2]["championId"],
        "t2_ban4": data["teams"][1]["bans"][3]["championId"],
        "t2_ban5": data["teams"][1]["bans"][4]["championId"],
        "t1_pick1":data["participants"][0]["championId"],
        "t1_pick2": data["participants"][1]["championId"],
        "t1_pick3": data["participants"][2]["championId"],
        "t1_pick4": data["participants"][3]["championId"],
        "t1_pick5": data["participants"][4]["championId"],
        "t2_pick1": data["participants"][5]["championId"],
        "t2_pick2": data["participants"][6]["championId"],
        "t2_pick3": data["participants"][7]["championId"],
        "t2_pick4": data["participants"][8]["championId"],
        "t2_pick5": data["participants"][9]["championId"],
        "t1_win":   data["teams"][0]["win"],
        "t2_win":   data["teams"][1]["win"]
}



    return data1

def main():
    response = requests.get("https://canisback.com/matchId/matchlist_na1.json")
    matchData = json.loads(response.text)
    '''print(MatchDetails(3867779264))
    MatchDetails(3867182674)'''

    for i in matchData[7407:]:
        '''data1=MatchDetails(i)
        print(data1)
        json_arr.append(data1)
        # data2=json.dumps(data4,indent = 4)
        with open("sample1.json", "w") as outfile:
            json.dump(json_arr, outfile)
            print("done")
        time.sleep(1.3)'''
        print(i)




if __name__ == '__main__':
    main()