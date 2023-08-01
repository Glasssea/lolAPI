import requests
import json
import time
import pandas as pd
import csv

def get_MatchID(puuid, api_key):
    URL = f'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids'   #API 주소

    matchId_info = {
        "puuid": puuid,
        "matchId": []
    }

    start = 0
    count = 100

    params = {
            "type": "ranked",
            "start": start,
            "count": count,
        }

    res = requests.get(URL, params=params, headers={"X-Riot-Token": api_key})
    if res.status_code == 200:
        resbody = json.loads(res.text)
        
        matchId_info["matchId"].extend(resbody)

    return matchId_info

def csv_to_list(filename):
    file = open(filename, 'r')
    csvfile = csv.reader(file)
    lists = []

    for item in csvfile:
        lists.append(item)

    puuid_list = []
    for i in range(1, len(lists)):
        puuid_list.append(lists[i][1])

    return puuid_list

API = "RGAPI-5c33a302-3415-4f70-8a50-af7e952699d1"

address_puuid = 'C:\\Users\\User\\Desktop\\학교\\K디지털\\puuid\\' #puuid.csv 경로 입력
address_csv = 'C:\\Users\\User\\Desktop\\학교\\K디지털\\puuid\\' #저장할 경로 입력

puuid = csv_to_list(address_puuid+"puuidsCH.csv")  

#matchID = get_MatchID(temp, API)
#df = pd.DataFrame(matchID)
#df.to_csv(path_or_buf=address+"test.csv")

df_final = pd.DataFrame()

for i in range(len(puuid)):
    matchID = get_MatchID(puuid[i], API)
    df = pd.DataFrame(matchID)
    #name = f'{i+1}. {puuid[i]}.csv'
    #df.to_csv(path_or_buf=address_csv+name)
    df_final = pd.concat([df_final, df], ignore_index=True)
    time.sleep(120)

df_final.to_csv(path_or_buf=address_csv+'get_match_id(CH).csv') #csv 파일로 저장