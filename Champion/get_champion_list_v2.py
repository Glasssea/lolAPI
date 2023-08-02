import requests
import json
import time
import pandas as pd
import csv

address_csv = 'C:\\Users\\User\\Desktop\\학교\\K디지털\\puuid\\'
URL = 'https://ddragon.leagueoflegends.com/cdn/13.14.1/data/ko_KR/champion.json'

res = requests.get(URL)
resbody = json.loads(res.text)
resbody2 = resbody['data']

data = {
    'id' : [],
    'name': [],
    'info': [],
    'tags': [],
    #'image':[],
    'stats':[],
}

df = pd.DataFrame(resbody2)
for column in df:
    data['id'].append(df[column]['id'])
    data['name'].append(df[column]['name'])
    data['info'].append(df[column]['info'])
    data['tags'].append(df[column]['tags'])
    #data['image'].append(df[column]['image'])
    data['stats'].append(df[column]['stats'])

df_final = pd.DataFrame(data)

info = {
    'attack': [],
    'defense': [],
    'magic': [],
    'difficulty': [],
}

stats = {
    "hp": [],
    "hpperlevel": [],
    "mp": [],
    "mpperlevel": [],
    "movespeed": [],
    "armor": [],
    "armorperlevel": [],
    "spellblock": [],
    "spellblockperlevel": [],
    "attackrange": [],
    "hpregen": [],
    "hpregenperlevel": [],
    "mpregen": [],
    "mpregenperlevel": [],
    "crit": [],
    "critperlevel": [],
    "attackdamage": [],
    "attackdamageperlevel": [],
    "attackspeedperlevel": [],
    "attackspeed": [],
}

#df_final.to_csv(path_or_buf=address_csv+'champion_list.csv')

'''tag_list = []
max = 0
for i in df_final['tags']:
    print(i)
    for j in i:
        if j not in tag_list:
            tag_list.append(j)'''

category = {
    'Assassin': [],
    'Fighter': [],
    'Mage': [],
    'Marksman': [],
    'Support': [],
    'Tank': [],
}

'''for index, i in df_final.iterrows():
    if 'Assassin' in i['tags']:
        category['Assassin'].append(i['id'])
    else:
        category['Assassin'].append('')

    if 'Fighter' in i['tags']:
        category['Fighter'].append(i['id'])
    else:
        category['Fighter'].append('')

    if 'Mage' in i['tags']:
        category['Mage'].append(i['id'])
    else:
        category['Mage'].append('')

    if 'Marksman' in i['tags']:
        category['Marksman'].append(i['id'])
    else:
        category['Marksman'].append('')

    if 'Support' in i['tags']:
        category['Support'].append(i['id'])
    else:
        category['Support'].append('')

    if 'Tank' in i['tags']:
        category['Tank'].append(i['id'])
    else:
        category['Tank'].append('')'''


'''for index, i in df_final.iterrows():
    if 'Assassin' in i['tags']:
        category['Assassin'].append(i['name'])
    else:
        category['Assassin'].append('')

    if 'Fighter' in i['tags']:
        category['Fighter'].append(i['name'])
    else:
        category['Fighter'].append('')

    if 'Mage' in i['tags']:
        category['Mage'].append(i['name'])
    else:
        category['Mage'].append('')

    if 'Marksman' in i['tags']:
        category['Marksman'].append(i['name'])
    else:
        category['Marksman'].append('')

    if 'Support' in i['tags']:
        category['Support'].append(i['name'])
    else:
        category['Support'].append('')

    if 'Tank' in i['tags']:
        category['Tank'].append(i['name'])
    else:
        category['Tank'].append('')'''

for index, i in df_final.iterrows():
    if 'Assassin' in i['tags']:
        category['Assassin'].append(1)
    else:
        category['Assassin'].append(0)

    if 'Fighter' in i['tags']:
        category['Fighter'].append(1)
    else:
        category['Fighter'].append(0)

    if 'Mage' in i['tags']:
        category['Mage'].append(1)
    else:
        category['Mage'].append(0)

    if 'Marksman' in i['tags']:
        category['Marksman'].append(1)
    else:
        category['Marksman'].append(0)

    if 'Support' in i['tags']:
        category['Support'].append(1)
    else:
        category['Support'].append(0)

    if 'Tank' in i['tags']:
        category['Tank'].append(1)
    else:
        category['Tank'].append(0)

df_index = pd.DataFrame(data['id'])
df_index.columns = ['id']

df1 = pd.DataFrame(category['Assassin'])
df2 = pd.DataFrame(category['Fighter'])
df3 = pd.DataFrame(category['Mage'])
df4 = pd.DataFrame(category['Marksman'])
df5 = pd.DataFrame(category['Support'])
df6 = pd.DataFrame(category['Tank'])

df_category = pd.concat([df_index, df1, df2, df3, df4, df5, df6], axis=1)
df_category.columns = ['id', 'Assassin', 'Fighter', 'Mage', 'Marksman', 'Support', 'Tank']
df_category.set_index(keys=df_category['id'], inplace=True)
df_category = df_category.drop(['id'], axis=1)
df_category.to_csv(path_or_buf=address_csv+'champion_category(US)1.csv')

df_info = pd.DataFrame(df_final['info'].to_dict()).transpose()
df_stats = pd.DataFrame(df_final['stats'].to_dict()).transpose()
df_cat2 = pd.concat([df1, df2, df3, df4, df5, df6], axis=1)
df_cat2.columns = ['Assassin', 'Fighter', 'Mage', 'Marksman', 'Support', 'Tank']

df_final2 = pd.concat([df_index, df_cat2, df_info, df_stats], axis=1)
df_final2.set_index(keys=df_final2['id'], inplace=True)
df_final2 = df_final2.drop(['id'], axis=1)
df_final2.to_csv(path_or_buf=address_csv+'champion_category(US)_2.csv')
