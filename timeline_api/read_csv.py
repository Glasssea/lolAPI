import pandas as pd

# Replace 'file.csv' with the name of your CSV file.
data = pd.read_csv('KR_6612520499.csv')
# print(data)
print(data.keys())
# print(data['Unnamed: 0'])
# print(data['metadata'])
# print(data['info'])


# print('-'*50)
# print(data.loc[0])
# print('-'*50)
# print(data.loc[1])
# print('-'*50)
# print(data.loc[2])
# print('-'*50)
# print(data.loc[3])
# print('-'*50)
# print(data.loc[4])
# print('-'*50)
# print(data.loc[5])
print('-'*50)

a = data.loc[0]
b = data.loc[1]
c = data.loc[2]
d = data.loc[3]
e = data.loc[4]
f = data.loc[5]
# print((a))
# print((b))
# print((c))
# print((d))
# print((e))
# print((f))

# print('len',len(a))
# print(a[0]) 
# print(a[1]) 
# print(a[2]) 

# print('len',len(b)) 
# print(b[0]) #matchId
# print(b[1]) #KR_6612520499
# print(b[2]) #nan

# print('len',len(c))
# print(c[0]) #participants
# print(c[1]) #그냥 puuid만 기록
# print(c[2]) # {'participantId':1, 'puuid':'DFASFSDF', 이런식으로 딕셔너리로 10명}

# print('len',len(d))
# print(d[0]) #frameInterval 
# print(d[1]) #nan
# print(d[2]) #??

print('len',len(e))
# print(e[0]) 
# print(e[1]) 
# print(e[2]) 

champion_state = e[2].split('{')
print(len(champion_state))
for i in range(len(champion_state)):
    print(champion_state[i])

# print('len',len(f))
# print(f[0]) 
# print(f[1]) 
# print(f[2]) 
