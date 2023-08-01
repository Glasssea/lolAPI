import pandas as pd
import requests
import json
import time
import csv
from collections import Counter



def get_puuid_and_id(summonerName, api_key):
    URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName
    res = requests.get(URL, headers={"X-Riot-Token": api_key})
    if res.status_code == 200:
        resbody = json.loads(res.text)
        return resbody['puuid'], resbody['id']
    else:
        print(f"Error: {res.status_code} {res.reason}")
        return None, None

def get_match_info(puuid, api_key):
    URL = f'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids'
    params = {
        "start": 0,
        "count": 100,  # 최근100판만 가져옴
    }
    res = requests.get(URL, params=params,headers={"X-Riot-Token": api_key})
    if res.status_code == 200:
        matchIds = json.loads(res.text)
        results = []
        for matchId in matchIds:
            match_info_URL = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId}"
            match_res = requests.get(match_info_URL, headers={"X-Riot-Token": api_key})
            if match_res.status_code == 200:
                match_data = json.loads(match_res.text)
                for participant in match_data['info']['participants']:
                    if participant['puuid'] == puuid:
                        result = {
                            'puuid': puuid,
                            'matchId': matchId,
                            'champion': participant['championName'],
                            'win': participant['win']
                        }
                        results.append(result)
        return results
    else:
        print(f"Error: {res.status_code} {res.reason}")
        return None


  
api_key = 'RGAPI-4e400b95-81cd-40f9-bf67-1b540783898c'  # API 키를 입력해야 합니다.

address_puuid = 'C:\\Users\\USER\\Downloads\\롤puuid\\' #puuid.csv 경로 입력
address_csv = 'C:\\Users\\USER\\Downloads\\롤puuid\\' #저장할 경로 입력

puuid_df = pd.read_csv(address_puuid+"test.csv")  # 소환사명 csv파일 

results = []

api_call_count = 0
start_time = time.time()

for i, summonerName in enumerate(puuid_df['summonerName']):
    puuid, _ = get_puuid_and_id(summonerName, api_key)
    api_call_count += 1
    if puuid is not None:
        match_info = get_match_info(puuid, api_key)
        api_call_count += 1
        if match_info is not None:
            results.extend(match_info)
    print(f"Progress: {i+1}/{len(puuid_df['summonerName'])} summoners processed")
    
    # 2분 쉬는 코드
    time.sleep(120)  

df = pd.DataFrame(results)
df.to_csv(address_puuid+"finer.csv")
