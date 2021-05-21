import pandas as pd
import numpy as np
#from urllib.request import urlretrieve
import csv
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly

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

def newCases(df):
    """Creates a new cases wich displays the new cases per country"""
    #col_one_list = df['one'].tolist()
    dfIndex = list(df.columns)
    newCasesList = list()
    newTotal = df[dfIndex[-1]].tolist()
    
    oldTotal = df[dfIndex[-2]].tolist()
    
    index = 0
    while index < len(newTotal):
        newCasesList.append(newTotal[index]-oldTotal[index])
        index += 1

    countryList = df.iloc[:,[1]]
    countryList['New Cases'] = newCasesList
    sortedList = countryList.sort_values('New Cases', axis=0, ascending=False)

    sortedList['Total'] = sortedList.groupby(['New Cases'])['New Cases'].transform('sum') #Sums the value of duplicaterows
    sortedList.drop('New Cases', axis='columns', inplace=True) #Drops the old date column
    sortedList = sortedList.drop_duplicates(subset=[dfIndex[1]]) #Drops country duplicates
    sortedList['Total'] = sortedList['Total'].apply('{:,}'.format) #Adds a comma for every 3rd number in totalcases for easier reading

    sortedList = sortedList.rename(columns = {'Total': 'New Cases'}, inplace = False)

    return(sortedList)


df = home()
table = tableSorter(df)
index = list(df.columns) #Creates a list of all column-names for use as index
date = index[-1] #Since the last index in the list is the relevant date it's made into the variable 'date'

table['Total'] = table.groupby([index[1]])[date].transform('sum') #Sums the value of duplicaterows
table.drop(date, axis='columns', inplace=True) #Drops the old date column
table = table.drop_duplicates(subset=[index[1]]) #Drops country duplicates
table = table.sort_values(by='Total', ascending=False) #Sorts the values again after summerising of duplicates
table['Total'] = table['Total'].apply('{:,}'.format) #Adds a comma for every 3rd number in totalcases for easier reading

(mo, da, ye) = date.split('/') #Splits the date into three variables; month, day and year
date = da+'/'+mo+'/'+ye #Puts the date back into one variable but in the correct [;)] order (day, month, year)

tableDateFixed = table.rename(columns = {'Total': date}, inplace = False) #Renames the cmbined cases column frot 'Total' to the correct date

pd.options.display.float_format = '{:,}'.format

fig2 = ff.create_table(tableDateFixed)
fig2.layout.width=400
fig3 = ff.create_table(newCases(df))
fig3.layout.width=400

fig = px.bar(df, x ='Country/Region', y=index[-1],width=800, height=400)


fig = fig.to_html()
fig2 = fig2.to_html()
fig3 = fig3.to_html()

html_str = ''' <DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style> 
h1{color: White;}
h1{text-align:center;}
body {
  background-image: url('corona.jpeg');
}
.meny {
  overflow: hidden;
  background-color: #333;
}

.meny a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.meny a:hover {
  background-color: #ddd;
  color: black;
}

.meny a.active {
  background-color: #04AA6D;
  color: white;
}

</style>
</head>
<body> 
<div class="meny">
  <a class="Coronamenu" href="test.html">CoronaStats</a>
  <a href="test2.html">CoronaShart</a>
  <a href="test3.html">Compare</a>
  <a href="test4.html">something</a>
</div>
<h1>Covid Stats</h1>
<center><p> ''' + fig +''' </p></center>

</body>
</html>'''

html_str2 = ''' <DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style> 
h1{color: White;}
h1{text-align:center;}
body {
  background-image: url('corona.jpeg');
}
.meny {
  overflow: hidden;
  background-color: #333;
}

.meny a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.meny a:hover {
  background-color: #ddd;
  color: black;
}

.meny a.active {
  background-color: #04AA6D;
  color: white;
}
p{
    position: relative;
    left: 800px;
    top: 150px;
}
p2{
    position: relative;
    left: 1480px;
    top: -5857px;
}

</style>
</head>
<body> 
<div class="meny">
  <a class="Coronamenu" href="test.html">CoronaStats</a>
  <a href="test2.html">CoronaChart</a>
  <a href="test3.html">Compare</a>
  <a href="test4.html">something</a>
</div>
<h1>Covid Chart</h1>
<p> ''' + fig2 +''' </p>
<p2> ''' + fig3 +''' </p2>


</body>
</html>'''
Ndf = r'https://raw.githubusercontent.com/ec-jrc/COVID-19/master/data-by-region/jrc-covid-19-all-days-by-regions.csv'
df1 = pd.read_csv(Ndf)
fig5 = px.bar(df1, x="Region", y="CurrentlyPositive")
fig5 = fig5.to_html()

html_str5 = ''' <DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style> 
h1{color: White;}
h1{text-align:center;}
body {
  background-image: url('corona.jpeg');
}
.meny {
  overflow: hidden;
  background-color: #333;
}

.meny a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.meny a:hover {
  background-color: #ddd;
  color: black;
}

.meny a.active {
  background-color: #04AA6D;
  color: white;
}

</style>
</head>
<body> 
<div class="meny">
  <a class="Coronamenu" href="test.html">CoronaStats</a>
  <a href="test2.html">CoronaShart</a>
  <a href="test3.html">Compare</a>
  <a href="test4.html">something</a>
</div>
<h1>Covid Stats</h1>
<center><p> ''' + fig5 +''' </p></center>

</body>
</html>'''


html_str5 = ''' <DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style> 
h1{color: White;}
h1{text-align:center;}
body {
  background-image: url('corona.jpeg');
}
.meny {
  overflow: hidden;
  background-color: #333;
}

.meny a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.meny a:hover {
  background-color: #ddd;
  color: black;
}

.meny a.active {
  background-color: #04AA6D;
  color: white;
}

</style>
</head>
<body> 
<div class="meny">
  <a class="Coronamenu" href="test.html">CoronaStats</a>
  <a href="test2.html">CoronaShart</a>
  <a href="test3.html">Compare</a>
  <a href="test4.html">something</a>
</div>
<h1>Covid Stats</h1>
<center><p> ''' + fig5 +''' </p></center>

</body>
</html>'''

html_file = open('test.html','w')
html_file.write(html_str)
html_file.close()

html_file2 = open('test2.html','w')
html_file2.write(html_str2)
html_file2.close()

html_file5 = open('test3.html','w')
html_file5.write(html_str5)
html_file5.close()

