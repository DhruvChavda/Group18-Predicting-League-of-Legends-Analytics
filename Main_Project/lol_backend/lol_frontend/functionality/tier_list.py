import json
with open('champion_pick_ban.json', 'r') as fd:
    champ_dict = json.load(fd)
champ = sorted(champ_dict, key=lambda x:x["pick"], reverse=True)
#print(champ)
with open('tier_list.json',"w") as fd:
    json.dump(champ,fd)