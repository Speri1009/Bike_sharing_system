# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:32:44 2020

@author: Lenovo
"For net flow in a particular day for a particular station"""
import pandas as pd
import matplotlib.pyplot as plt
from Bikedata import Bikedata_function
from Bikedata import BikeDataAna

Bikedata = Bikedata_function()

list_of_dates    = ['2019-11-05','2019-11-04']
list_of_stations = [31030,31009]

for i in range(0,len(list_of_dates)):
     for j in range(0,len(list_of_stations)):
         print (i,j)
         BikeDataAna(Bikedata,list_of_dates[i],list_of_stations[j])

#Debug individually.....

#BikeDataAna(Bikedata,list_of_dates[0],list_of_stations[0])
#print('Printing second combination\n')
#BikeDataAna(Bikedata,'2019-11-05',31009)
#print('Printing third combination\n')
#BikeDataAna(Bikedata,list_of_dates[1],list_of_stations[0])
#print('Printing fourth combination\n')
#BikeDataAna(Bikedata,list_of_dates[1],list_of_stations[1])
