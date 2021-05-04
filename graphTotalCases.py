import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import matplotlib.dates as dts

def home():
    df=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    return(df)

def tableSorter(df):
    index = list(df.columns)
    countryList = df.iloc[:, [1,-1]]
    sortedList = countryList.sort_values(index[-1], axis=0, ascending=False)
    return(sortedList)

def countrytograph(df):
    fig, ax = plt.subplots()
    ax.set_title("Cases by country") 
    ax.set_ylabel("Cases") 
    ax.set_xlabel("Countries")

    x, y = (df.iloc[:, 1]).tolist(), (df.iloc[:, -1]).tolist()
    


    ax.bar(x, y)
    plt.xticks(rotation = 90) #roterar x axelns vÃ¤rden 90 grader
    fig.autofmt_xdate()
    #mng = plt.get_current_fig_manager()
    #mng.resize(*mng.window.maxsize()) #maximerar pop up rutan
    fig_html = mpld3.fig_to_html(fig)
    return fig_html #returnerar figuren



df = home()
table = tableSorter(df)
print(table)
countrytograph(df)

