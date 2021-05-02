import pandas as pd
import numpy as np

def home():
    df=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    return(df)

def tableSorter(df):
    index = list(df.columns)
    countryList = df.iloc[:, [1,-1]]
    sortedList = countryList.sort_values(index[-1], axis=0, ascending=False)
    return(sortedList)


df = home()
table = tableSorter(df)
print(table)