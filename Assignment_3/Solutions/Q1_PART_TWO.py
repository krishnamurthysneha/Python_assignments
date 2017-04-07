import pandas as pd
loc= '/Users/Sneha/Documents/material_for_python/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/vehicle_collisions.csv'
data = pd.read_csv(loc)
#data=data['BOROUGH']
#rdata['VEHICLE 1 TYPE'].isnull()
count = 0
#data[data['VEHICLE 1 TYPE'].notnull() & data['VEHICLE 2 TYPE'].notnull() & data['VEHICLE 3 TYPE'].notnull() & data['VEHICLE 4 TYPE'].notnull() & data['VEHICLE 4 TYPE'].notnull() ]
if data['VEHICLE 1 TYPE'].notnull():
    count=count+1
if data['VEHICLE 2 TYPE'].notnull():
    count=count+1
if data['VEHICLE 3 TYPE'].notnull():
    count=count+1
if data['VEHICLE 4 TYPE'].notnull():
    count=count+1
if data['VEHICLE 5 TYPE'].notnull():
    count=count+1

print(data.head())