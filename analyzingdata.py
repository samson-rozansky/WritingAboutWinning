from sklearn.preprocessing import MinMaxScaler

import pandas as pd

data = pd.read_csv("TheDataWeCaveAbout.csv")

diction = dict()

for index, row in data.iterrows():
    diction[row[1][:4]] = [0] * 20
    
for index, row in data.iterrows():
    for i in range(20):
        diction[row[1][:4]][i] += row[2+i]

for key in diction:
    for i in range(20):
        diction[key][i] = diction[key][i]/20



print(diction)
