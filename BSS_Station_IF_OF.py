# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:32:44 2020

@author: Lenovo
"For net flow in a particular day for a particular station"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', 50)

from Bikedata import Bikedata_function
from Bikedata import BikeDataAna
# To Identify the hotspots Iflow and OutFlow for each station is needed
# Importing the data and Inflow and OutFlow Functions

Bikedata = Bikedata_function()

# Geting the list of dates from Bike data 
unique_start_dates = pd.to_datetime(Bikedata['Start date']).dt.date.unique()
unique_end_dates = pd.to_datetime(Bikedata['End date']).dt.date.unique()

list_of_Start_dates = []
list_of_End_dates   = []

for i in unique_start_dates:
    i = str(i.strftime('%Y-%m-%d'))
    list_of_Start_dates.append(i)
    
for i in unique_end_dates:
    i = str(i.strftime('%Y-%m-%d'))
    list_of_End_dates.append(i)
    
list_of_dates = list(set(list_of_Start_dates)&set(list_of_End_dates))
list_of_dates = sorted(list_of_dates, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))

#getting the list of Stations

list_of_stations = [ 31000, 31001, 31002, 31003, 31004, 31005, 31006, 31007, 31009, 31010, 31011, 
                    31012, 31013, 31014, 31015, 31016, 31017, 31018, 31019, 31020, 31021, 31022, 
                    31023, 31024, 31025, 31026, 31027, 31028, 31029, 31030, 31031, 31032, 31033, 31034,
                    31035, 31036, 31037, 31038, 31039, 31040, 31041, 31042, 31043, 31044, 31045, 31046, 31047, 
                    31048, 31049, 31050, 31051, 31052, 31053, 31054, 31055, 31056, 31057, 31058, 31059, 31060, 31061, 
                    31062, 31063, 31064, 31065, 31066, 31067, 31068, 31069, 31070, 31071, 31072, 31073, 31074, 31075, 31076, 
                    31077, 31078, 31079, 31080, 31081, 31082, 31083, 31084, 31085, 31086, 31087, 31088, 31089, 31090, 31091, 31092, 
                    31093, 31094, 31095, 31096, 31097, 31098, 31099, 31100, 31101, 31102, 31103, 31104, 31105, 31106, 31107, 31108, 31109, 
                    31110, 31111, 31112, 31113, 31114, 31115, 31116, 31117, 31118, 31119, 31120, 31121, 31122, 31123, 31124, 31125, 31126, 
                    31127, 31128, 31129, 31130, 31131, 31200, 31201, 31202, 31203, 31204, 31205, 31206, 31207, 31208, 31209, 31211, 31212,
                    31213, 31214, 31215, 31216, 31217, 31218, 31219, 31220, 31221, 31222, 31223, 31224, 31225, 31226, 31227, 31228, 31229, 
                    31230, 31231, 31232, 31233, 31234, 31235, 31236, 31237, 31238, 31239, 31240, 31241, 31242, 31243, 31244, 31245, 31246, 
                    31247, 31248, 31249, 31250, 31251, 31252, 31253, 31254, 31255, 31256, 31257, 31258, 31259, 31260, 31261, 31262, 31263, 
                    31264, 31265, 31266, 31267, 31268, 31269, 31270, 31271, 31272, 31273, 31274, 31275, 31276, 31277, 31278, 31279, 31280]

returnDataAna = []

# looping the Bikedata to get inflow and outflow for each station fro each day

for i in range(0,len(list_of_dates)):
      for j in range(0,len(list_of_stations)):
          returnDataAna.append(BikeDataAna(Bikedata,list_of_dates[i],list_of_stations[j]))

Dataframe= pd.DataFrame(np.concatenate(returnDataAna))
Dataframe.to_csv(r'C:\Users\Lenovo\Desktop\Data set\Bike Share system\Inflow_group.csv', index = False)
print(returnDataAna)


#Debug individually.....
# list_of_end_stations = Bikedata['End station number'].unique().astype(list)
# list_of_start_stations = Bikedata['Start station number'].unique().astype(list)
#   list_of_stations = list(set(list_of_start_stations) & set(list_of_end_stations))
#returnDataAna = BikeDataAna(Bikedata,list_of_dates[0],list_of_stations[0])
#print(returnDataAna[1])

#BikeDataAna(Bikedata,'2019-11-05',31009)
#print('Printing third combination\n')
#BikeDataAna(Bikedata,list_of_dates[1],list_of_stations[0])
#print('Printing fourth combination\n')
#BikeDataAna(Bikedata,list_of_dates[1],list_of_stations[1])
