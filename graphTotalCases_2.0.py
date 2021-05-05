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

    list_of_countries = (df.iloc[:, 1]).tolist()

    list_of_countries = [str(item) for item in list_of_countries]


    x, y = (list_of_countries, (df.iloc[:, -1]).tolist())



    ax.bar(x, y)
    plt.xticks(rotation = 90) #roterar x axelns värden 90 grader
    fig.autofmt_xdate()
    #mng = plt.get_current_fig_manager()
    #mng.resize(*mng.window.maxsize()) #maximerar pop up rutan
    fig_html = mpld3.fig_to_html(fig)
    return fig_html #returnerar figuren

def create_html_index(graph):
    html_str = '''<DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    </head>
    <body>''' + graph + '''</body>
    </html>'''

    html_file = open("index.html", "w")
    html_file.write(html_str)
    html_file.close()



df = home()
table = tableSorter(df)
print(table)
countrytograph(df)

create_html_index(countrytograph(df))