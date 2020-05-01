# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:45:43 2020

@author: Lenovo
"""
import json
from pandas.io.json import json_normalize
import pandas as pd
import csv
import pprint


with open('station_information.json') as json_file1: 
    data_1 = json.load(json_file1)   
station_data = data_1['data'] 
x = []
for i in (station_data.values()):
    x.append(i)
df_station_data = pd.json_normalize(x[0])
df_station_data = df_station_data.set_index('station_id')
print(df_station_data.index)
with open('station_status.json') as json_file2: 
    data_2 = json.load(json_file2)
y= []    
station_status =data_2['data'] 
for j in (station_status.values()):
    y.append(j)
df_station_status = pd.json_normalize(y[0])
df_station_status = df_station_status.set_index('station_id')
print (df_station_status.columns)

dataset = pd.merge(df_station_data,df_station_status, left_index =True, right_index = True)

dataset['last_reported'] = pd.to_datetime(dataset['last_reported'], unit='s')
print (dataset)
#dataset.to_csv(r'C:\Users\Lenovo\Desktop\Data set\Bike Share system\Station_information.csv', index = False)
