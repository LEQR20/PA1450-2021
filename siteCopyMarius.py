import pandas as pd
import numpy as np
#from urllib.request import urlretrieve
import csv
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff


def home():
    """Downloads the csv-file of the data"""
    df=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    return(df)

def tableSorter(df):
    """Creates a new DF of the Country-column and the total cases column"""
    index = list(df.columns) #Creates a list of all column-names for use as index
    countryList = df.iloc[:, [1,-1]] #Creates a DF of the country- and total cases-column
    sortedList = countryList.sort_values(index[-1], axis=0, ascending=False) #Sorts the new DF in descending order based on total cases
    return(sortedList)


df = home()
table = tableSorter(df)
#print(table)


index = list(df.columns) #Creates a list of all column-names for use as index
date = index[-1]

(mo, da, ye) = date.split('/')
date = da+'/'+mo+'/'+ye

tableDateFixed = table.rename(columns = {index[-1]: date}, inplace = False)

fig2 = ff.create_table(tableDateFixed)

fig = px.bar(df, x ='Country/Region', y=index[-1])

fig = fig.to_html()
fig2 = fig2.to_html()

html_str = ''' <DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style> 
    .h1{
        text-align:center;
    }
</style>
</head>
<body> 
<h1>Corona statistics</h1>
<p> ''' + fig +''' </p>
<p> ''' + fig2 + ''' </p>
</body>
</html>'''

html_file = open('2.html','w')
html_file.write(html_str)
html_file.close()