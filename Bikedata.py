# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:17:35 2020

@author: Lenovo
"""


import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', 50)
import numpy as np
from scipy import stats

# from outflow_inflow import Outflow_Per_Station
# from outflow_inflow import Outflow_Per_Station_Per_Date
# from outflow_inflow import Inflow_Per_Station
# from outflow_inflow import Inflow_Per_Station_Per_Date
# Phase 1
def Bikedata_function():
    df_1 = pd.read_csv('201911-capitalbikeshare-tripdata.csv')
    df_1_data = pd.DataFrame(df_1)
    df_1_data['Start date'] = pd.to_datetime(df_1_data['Start date'])
    df_2 = pd.read_csv('201912-capitalbikeshare-tripdata.csv')
    df_2_data = pd.DataFrame(df_2)
    df_2_data['Start date'] = pd.to_datetime(df_2_data['Start date'],dayfirst=True,)# date issue
    df_2_data['End date'] = pd.to_datetime(df_2_data['End date'],dayfirst=True,)
    df_3 = pd.read_csv('202001-capitalbikeshare-tripdata.csv')
    df_3_data = pd.DataFrame(df_3)
    df_3_data['Start date'] = pd.to_datetime(df_3_data['Start date'])
    df_4= pd.read_csv('202002-capitalbikeshare-tripdata.csv')
    df_4_data = pd.DataFrame(df_4)
    df_4_data['Start date'] = pd.to_datetime(df_4_data['Start date'])
    Bikedata = pd.concat([df_1_data,df_2_data,df_3_data,df_4_data])
    Bikedata['Start_datetime'] = Bikedata['Start date']
    Bikedata['End_datetime'] = Bikedata['End date']
    Bikedata['End_datetime'] = Bikedata['End_datetime'].astype('datetime64[ns]')
    Bikedata['Start_time_hr']= (Bikedata['Start_datetime'].dt.hour)
    Bikedata['Start_time_min'] =(Bikedata['Start_datetime'].dt.minute)
    Bikedata['Start_time_sec'] =(Bikedata['Start_datetime'].dt.second)
    Bikedata['Start_Duration'] = (Bikedata['Start_time_hr'] * 60 + Bikedata['Start_time_min'])*60+Bikedata['Start_time_sec']
    Bikedata['End_time_hr']= (Bikedata['End_datetime'].dt.hour)
    Bikedata['End_time_min'] =(Bikedata['End_datetime'].dt.minute)
    Bikedata['End_time_sec'] =(Bikedata['End_datetime'].dt.second)
    Bikedata['End_Duration'] = (Bikedata['End_time_hr'] * 60 + Bikedata['End_time_min'])*60+Bikedata['End_time_sec']
    Bikedata['Start_Time'] = pd.to_datetime(Bikedata['Start date']).dt.time
    Bikedata['Start date'] = pd.to_datetime(Bikedata['Start date']).dt.date
    Bikedata['End_Time'] = pd.to_datetime(Bikedata['End date']).dt.time
    Bikedata['End date'] = pd.to_datetime(Bikedata['End date']).dt.date
    Bikedata['Weekday'] = pd.to_datetime(Bikedata['Start date']).dt.day_name()
	#Bikedata.to_csv(r'C:\Users\Lenovo\Desktop\Data set\Bike Share system\tripdata.csv', index = False)#Export to csv
    Bikedata['Duration_min']=Bikedata['Duration']*0.0166667
    return Bikedata


#Phase 2

def Outflow_Per_Station(Bikedata,station_num):
    Outflow_Per_Station =Bikedata[Bikedata['Start station number']==station_num]
    Outflow_Per_Station['Flag'] =0
    Outflow_Per_Station.drop(['Duration','Start_time_hr' , 'Start_time_min','Start_time_sec','End_time_min','End_time_hr','End_datetime','End_time_sec','End station number','End station','Member type','End_Time','End_Duration','End date'],axis = 1, inplace = True)
    Outflow_Per_Station = Outflow_Per_Station.rename(columns={'Start_datetime':'Date_time','Start date':'Date','Start station number':'Station_Number','Start station':'Station_Name','Start_Duration':'Duration_total','Start_Time':'Time'})
    Outflow_Per_Station['Date'] = pd.to_datetime(Outflow_Per_Station['Date'])
    Outflow_Per_Station = Outflow_Per_Station.set_index('Date')
    idx = pd.date_range('2019-11-01 ', '2020-03-01')
    idx = pd.DataFrame(idx).set_index(0)
    Outflow_Per_Station_d1 = pd.merge(Outflow_Per_Station,idx, how = 'right', left_index= True,right_index=True)
    Outflow_Per_Station_d1['Duration_total'] = Outflow_Per_Station_d1['Duration_total'].fillna(0)
    Outflow_Per_Station_d1['Flag'] =Outflow_Per_Station_d1['Flag'].fillna(0)
    Outflow_Per_Station_d1['Station_Number'] =Outflow_Per_Station_d1['Station_Number'].fillna(station_num)
    Outflow_Per_Station_d1 = Outflow_Per_Station_d1.reset_index()
    Outflow_Per_Station_d1 = Outflow_Per_Station_d1.rename(columns={'index':'Date'})
    return Outflow_Per_Station_d1

def Outflow_Per_Station_Per_Date(Bikedata,station_num,date):
    Outflow = Outflow_Per_Station(Bikedata,station_num)
    Outflow['Date'] = Outflow['Date'].astype(str)
    Outflow_per_date = Outflow[Outflow['Date']== date]
    #Outflow_per_date = Outflow[Outflow['Date']== '2019-11-03']
    return Outflow_per_date

def Inflow_Per_Station(Bikedata,station_num):
    Inflow_Per_Station = Bikedata[Bikedata['End station number']==station_num]
    #Inflow_Per_Station = Bikedata[Bikedata['End station number']==31012]
    Inflow_Per_Station['Flag']=1
    Inflow_Per_Station.drop(['Duration','Start_time_hr','Start_time_min','Start_time_sec','End_time_min','End_time_hr','Start_datetime','End_datetime','End_time_sec','Start station number','Start station','Member type','Start_Time','Start_Duration','Start date'],axis = 1, inplace = True)
    Inflow_Per_Station = Inflow_Per_Station.rename(columns={'End date':'Date','End station number':'Station_Number','End station':'Station_Name','End_Duration':'Duration_total','End_Time':'Time'})
    Inflow_Per_Station['Date'] = pd.to_datetime(Inflow_Per_Station['Date'])
    Inflow_Per_Station = Inflow_Per_Station.set_index('Date')
    idx = pd.date_range('2019-11-01 ', '2020-03-01')
    idx = pd.DataFrame(idx).set_index(0)
    Inflow_Per_Station_d1= pd.merge(Inflow_Per_Station,idx, how = 'right', left_index= True,right_index=True)
    Inflow_Per_Station_d1['Duration_total'] = Inflow_Per_Station_d1['Duration_total'].fillna(0)
    Inflow_Per_Station_d1['Flag'] =Inflow_Per_Station_d1['Flag'].fillna(1)
    return Inflow_Per_Station_d1

def Inflow_Per_Station_Per_Date(Bikedata,station_num,date):
    Inflow = Inflow_Per_Station(Bikedata,station_num)
    Inflow =Inflow.reset_index()
    Inflow = Inflow.rename(columns={'index':'Date'})
    Inflow['Date'] = Inflow['Date'].astype(str)
    Inflow_per_date = Inflow[Inflow['Date']== date]
    #Outflow_per_date = Outflow[Outflow['Date']== '2019-11-03']
    return Inflow_per_date
#Phase 3
def BikeDataAna(Bikedata,date,station_num):
    #Outflow_per_station_1 =          Outflow_Per_Station(Bikedata,station_num)
    Outflow_Per_Station_Per_Date_1 = Outflow_Per_Station_Per_Date(Bikedata,station_num,date)
    #Inflow_per_station_1 =           Inflow_Per_Station(Bikedata,station_num)
    Inflow_Per_Station_Per_Date_1 =  Inflow_Per_Station_Per_Date(Bikedata,station_num,date)
    total_flow = pd.concat([Outflow_Per_Station_Per_Date_1,Inflow_Per_Station_Per_Date_1],ignore_index=True)
    total_flow = total_flow.reset_index()
    total_flow['Duration_total'] = ((total_flow['Duration_total'])/60).round(0)
    total_flow['Durations_bins']= pd.cut(total_flow['Duration_total'], bins=4)
    
    OF_bins = total_flow['Durations_bins'],total_flow['Flag'],total_flow['Date'][total_flow['Flag']==0]
    IF_bins = total_flow['Durations_bins'],total_flow['Flag'],total_flow['Station_Number'],total_flow['Date'][total_flow['Flag']==1]
    OF_bins = pd.DataFrame(OF_bins).T
    IF_bins = pd.DataFrame(IF_bins).T
    Outflow_group = OF_bins.groupby(['Durations_bins']).agg({'Flag':['count']})
    Inflow_group = IF_bins.groupby(['Station_Number','Date','Durations_bins']).agg({'Flag':['count']})
    Inflow_group.columns.droplevel(level = 0)
    Inflow_group = Inflow_group.reset_index()
    Inflow_group.columns = ['Station_Number','Date','Durations_bins','count']
    Outflow_group.columns.droplevel(level = 0)
    Outflow_group = Outflow_group.reset_index()
    Outflow_group.columns = ['Durations_bins','count']
    Inflow_group['Count_Outflow'] = Outflow_group['count']
    Inflow_group['netflow'] = Inflow_group['count']-Inflow_group['Count_Outflow']
    return Inflow_group
    #print (Inflow_group.columns)


    # Outflow_Per_Station =Bikedata[(Bikedata['Start date']== date) & (Bikedata['Start station number']==station_num)]
    
    # #Outflow_Per_Station = Outflow_Per_Station.reindex(Outflow_Per_Station['Start date'], fill_value=0).reset_index()
    # Outflow_Per_Station['Flag'] =0
    # Outflow_Per_Station.drop(['Duration','Start_time_hr' , 'Start_time_min','Start_time_sec','End_time_min','End_time_hr','Start_datetime','End_datetime','End_time_sec','End station number','End station','Member type','End_Time','End_Duration','End date'],axis = 1, inplace = True)
    # Outflow_Per_Station = Outflow_Per_Station.rename(columns={'Start date':'Date','Start station number':'Station_Number','Start station':'Station_Name','Start_Duration':'Duration_total','Start_Time':'Time'})

    



    # Inflow_Per_Station = Bikedata[(Bikedata['End date']== date) & (Bikedata['End station number']==station_num)]
    # Inflow_Per_Station['Flag']=1
    # #Inflow_Per_Station = Inflow_Per_Station.set_index(['End date']).reindex(Inflow_Per_Station, fill_value=0).reset_index()

    # Inflow_Per_Station.drop(['Duration','Start_time_hr','Start_time_min','Start_time_sec','End_time_min','End_time_hr','Start_datetime','End_datetime','End_time_sec','Start station number','Start station','Member type','Start_Time','Start_Duration','Start date'],axis = 1, inplace = True)
    # Inflow_Per_Station = Inflow_Per_Station.rename(columns={'End date':'Date','End station number':'Station_Number','End station':'Station_Name','End_Duration':'Duration_total','End_Time':'Time'})
    # total_flow = pd.concat([Outflow_Per_Station,Inflow_Per_Station],ignore_index=True)
    
    # total_flow['Duration_total'] = ((total_flow['Duration_total'])/60).round(0)
#     total_flow = total_flow.sort_values(by='Time')
# #print ("Out Flow:------->",Outflow_Per_Station.columns)
# #print ("Inflow:--------->",Inflow_Per_Station.columns)
    
    
    # total_flow['Durations_bins']= pd.cut(total_flow['Duration_total'], bins=4)
    # total_flow['Durations_bins'].resample('3T').asfreq()
    # total_flow = total_flow.reset_index()
    # OF_bins = total_flow['Durations_bins'],total_flow['Flag'],total_flow['Date'][total_flow['Flag']==0]
    # #OF_bins = OF_bins.set_index(['Date']).reindex(OF_bins, fill_value=0).reset_index()
    # IF_bins = total_flow['Durations_bins'],total_flow['Flag'],total_flow['Station_Number'],total_flow['Date'][total_flow['Flag']==1]
    # OF_bins = pd.DataFrame(OF_bins).T
    # IF_bins = pd.DataFrame(IF_bins).T
    # Outflow_group = OF_bins.groupby(['Durations_bins']).agg({'Flag':['count']})
    # Inflow_group = IF_bins.groupby(['Station_Number','Date','Durations_bins']).agg({'Flag':['count']})
    # Inflow_group.columns.droplevel(level = 0)
    # Inflow_group = Inflow_group.reset_index()
    # Inflow_group.columns = ['Station_Number','Date','Durations_bins','count']
    # Outflow_group.columns.droplevel(level = 0)
    # Outflow_group = Outflow_group.reset_index()
    # Outflow_group.columns = ['Durations_bins','count']
    # Inflow_group['Count_Outflow'] = Outflow_group['count']
    # Inflow_group['netflow'] = Inflow_group['count']-Inflow_group['Count_Outflow']
    #return (Outflow_Per_Station)
    
    #Inflow_group.plot(x='Durations_bins', y='netflow')




#Bikedata_function()