# Bike_sharing_system

Bike sharing system is very popular in many parts of the world. It is economical and healthy way of transport for people traveling short distances. 
Yet there are many factors to be addressed to keep the service more efficient. 

Scope of this project is to identify the Inflow and Outflow per station where inflow is number of bikes entering the station while Outflow is number of bikes moving out of the station at a given time. 
This helps us understand the bike traffic at a certain station at a given time. The hotspots and peak hours could be identified.
This helps service provider to plan strategy on the availability of bikes and docking stations at each location.

Data Sources: Excel, Json 
Programming: Python(Pandas, numpy)

Files Usage:

Bikedata.py: It has various user defined functions to concatenate different csv’s, and clean it for further analysis. 

Bike_frequency_PerDay.py: It is an overall view of the bike traffic at each station. Data is grouped by start date and start station to view the bike count and duration. It uses Bikedata.py to import the data as needed.

BSS_Station_IF_OF.py: this program identifies the inflow and outflow count per station at a particular time based on the bike movement. The results are exported as CSV file as well.

Inflow_group.csv is the output for the BSS_Station_IF_OF.py

Station_information.json, Station_status.json, Station_region.json are various datasource files. Readjson.py reads the data in the Json files and exports them as csv file for further analysis.
 

