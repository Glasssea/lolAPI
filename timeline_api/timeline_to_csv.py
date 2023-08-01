import requests
import pandas as pd
region = "asia"
match_id = "KR_6612520499"
api_key = "RGAPI-6a47a8a9-b030-4c2d-91a2-552c028d255b"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}
def get_match_timeline(match_id, api_key):
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline"
    response = requests.get(url, headers=headers)
    return response.json()


data = get_match_timeline(match_id, api_key)

# Convert data to DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv(f"{match_id}.csv")