import requests
import pandas as pd
url = "https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1"
api_key = "RGAPI-78657f3e-6124-4b45-a708-104b66419301"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}

response = requests.get(url, headers=headers)
# print(response.json())


def get_challenges(api_key):
    url = "https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page=1"
    response = requests.get(url, headers=headers)
    return response.json()


data = get_challenges(api_key)

# Convert data to DataFrame
df = pd.DataFrame(data)
# print(df.columns)
# print(df)
# print(df["summonerId"])
summonerName = df["summonerName"]


# Save DataFrame to CSV
# df.to_csv("challenges.csv")
