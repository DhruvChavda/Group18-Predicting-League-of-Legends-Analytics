import requests,json
import csv
def pick_ban(match_dict,id,v):
    k = 0
    json_arr=[]
    for i in id:
        ban = 0

        pick = 0
        for j in match_dict:
            if i == str(j['t1_ban1']) or i == str(j['t1_ban2']) or i == str(j['t1_ban3']) or i == str(
                    j['t1_ban4']) or i == str(j['t1_ban5']) or i == str(j['t2_ban1']) or i == str(
                    j['t2_ban2']) or i == str(j['t2_ban3']) or i == str(j['t2_ban4']) or i == str(j['t2_ban5']):
                ban += 1
                # print("*")
            if i == str(j['t1_pick1']) or i == str(j['t1_pick2']) or i == str(j['t1_pick3']) or i == str(
                    j['t1_pick4']) or i == str(j['t1_pick5']) or i == str(j['t2_pick1']) or i == str(
                    j['t2_pick2']) or i == str(j['t2_pick3']) or i == str(j['t2_pick4']) or i == str(j['t2_pick2']):
                pick += 1
                # print("+")
        #print(ban, " ban", pick, "pick")
        f = {
            "name": v[k],
            "id": i,
            "pick": "{:.2f}".format((pick/7406)*100),
            "ban": "{:.2f}".format((ban/7406)*100),
            "total_Matches": (pick+ban)*100
        }
        k+=1
        json_arr.append(f)
        with open("champion_pick_ban.json","w") as outfile:
            json.dump(json_arr, outfile)
            print("done")

    #print(type(json_arr))


def csv_f():
    with open("champion_p_b.csv", "w")as f:
        writer = csv.writer(f)
        writer.writerow(['Champ_id', 'Pick', 'Ban'])
    return writer
def main():
    #csv_f()
    '''with open('champion_info_2.json', 'r') as f:
        champ_dict = json.load(f)'''
    url = 'http://ddragon.leagueoflegends.com/cdn/11.9.1/data/en_US/champion.json'
    response=requests.get(url)
    data=response.json()
    data1=json.loads(response.text)
    data1=data1["data"]
    v=[]
    for i in data1:
       v.append(i)
    #print(v)
    i=0
    id=[]
    name=[]
    for j in range(0,len(v)):
        id.append(data["data"][v[j]]["key"])
    #print(id)


    with open('sample2.json', 'r') as fd:
        match_dict = json.load(fd)
    pick_ban(match_dict,id,v)
    #print(data1)






if __name__ == '__main__':
    main()