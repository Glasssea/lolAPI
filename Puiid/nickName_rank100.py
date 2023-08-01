import requests
import json
import time
import pandas as pd
import csv

global req_count
req_count = 0

q_list = ['RANKED_SOLO_5x5', 'RANKED_TFT', 'RANKED_FLEX_SR', 'RANKED_FLEX_TT']
t_list = ['CHALLENGER', 'GRANDMASTER', 'MASTER', 'DIAMOND', 'EMERALD', 'PLATINUM', 'GOLD', 'SILVER', 'BRONZE', 'IRON']
d_list = ['I', 'II', 'III', 'IV']

API = "RGAPI-75e43c80-d90b-497a-8d62-ce46aea39748"
address_csv = 'C:\\Users\\User\\Desktop\\학교\\K디지털\\puuid\\'

def get_gameName(q, t, d, p, api_key):
    URL = f'https://kr.api.riotgames.com/lol/league-exp/v4/entries/{q_list[q-1]}/{t_list[t-1]}/{d_list[d-1]}'

    #rank = 1
    data = {
        #'rank' : [],
        'summonerName' : [],
    }

    page = p
    params = {
        'page' : page,
    }

    res = requests.get(URL, params=params, headers={"X-Riot-Token": api_key})
    #req_count += 1
    if res.status_code == 200 and res.text:
        resbody = json.loads(res.text)

    while resbody:
        #data['rank'].append(rank)
        data['summonerName'].append(resbody[0]['summonerName'])

        #if rank == r:
        #    break

        #rank += 1
        del resbody[0]

    return data

df = pd.DataFrame(get_gameName(1, 1, 1, 1, API))
df2 = pd.DataFrame(get_gameName(1, 2, 1, 1, API))
df_final = pd.concat([df, df2], ignore_index=True)
df_final.drop(df_final.index[100:], inplace=True)
df_final.to_csv(path_or_buf=address_csv+'nickName_rank100.csv')