# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:28:44 2020

@author: Lenovo
"""


import pandas as pd
#Bikedata['Start_Time_type'] = np.where(pd.to_datetime(Bikedata['Start date']).dt.hour <= 9,'Morning')

from Bikedata import Bikedata
Bikedata = Bikedata()
#print(Bikedata.head())
number_of_bikes_used_perday = Bikedata.groupby(['Start station','Start date']).agg({'Bike number':['count'],'Duration':['sum']})
#print (number_of_bikes_used_perday.sort_values(by = 'Start date', ascending = True))
number_of_bikes_used_perday= number_of_bikes_used_perday.reset_index()
number_of_bikes_used_perday.columns = ['Start station','Start date','count','sum']