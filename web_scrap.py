# Web scrap https://en.wikipedia.org/wiki/List_of_neighbourhoods_in_Toronto#Lists_of_city-designated_neighbourhoods

#import libraries
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd 
import numpy as np
 
# call url to get data 
url = 'https://en.wikipedia.org/wiki/List_of_neighbourhoods_in_Toronto'
# <table class="wikitable sortable jquery-tablesorter">
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(url)
print(response.status_code)
# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
table=soup.findAll('table',{'class':"wikitable"})
rows = table[1].findAll('tr')
# create dataframe 
new_data =pd.read_html(str(table[1]))
# convert list to dataframe
new_data=pd.DataFrame(new_data[0])
print(list(new_data.columns))
#Result: ['CDN number', 'City-designated neighbourhood', 'Former city/borough', 'Neighbourhoods covered', 'Map', 'Unnamed: 5']
print(new_data.head())
# drop unnecessary columns
new_data = new_data.drop(['Neighbourhoods covered','Map', 'Unnamed: 5'], axis=1)
# rename columns for matching
new_data = new_data.rename(columns={'CDN number':'cdn_num', 'City-designated neighbourhood':'neighbourhood_cleansed', 'Former city/borough':'former_city'})
print(list(new_data.columns))
# you can then export new_data to csv
