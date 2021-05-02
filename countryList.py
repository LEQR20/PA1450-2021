import pandas as pd
import numpy as np

def home():
    df=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    #print(df.head())
    return(df)

df = home()
#land = np.array([df.iloc[:,-1]])
land = [df.iloc[:,-1]]
print(land)
landnamn = df["Country/Region"]#.to_numpy()
print(landnamn)

print(type(landnamn))

# dictonary = {}

# for i in land:
#     for j in landnamn:
#         dictonary[str(j)]=int(i)
# print(dictonary)
"""
print(df.iloc[:,-1])
print("\n")
test = df[df["Country/Region"]=="Afghanistan"]
print(test.iloc[:,-1])
b = int(test.iloc[:,-1])
print(b, "b")
print("\n")
print(test)
#print(df)
"""