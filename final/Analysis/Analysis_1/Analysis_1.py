#1) Find the average number of flights delayed for every year and sort them in descending order.
import pandas as pd
import numpy as np
from datetime import datetime
import time
import calendar
loc= '/Users/Sneha/Downloads/Final_dataset.csv'
data = pd.read_csv(loc)
#print(data.head())
#print(data.dtypes)
#To convert the dataype from float to int
data['DepTime'].fillna(0,inplace=True)
data['ArrTime'].fillna(0,inplace=True)

data.DepTime=data.DepTime.astype(int)
data.ArrTime=data.DepTime.astype(int)
#print(data.head())

#for the year 2016
#x1=data[data['Year']==1987]
#df.astype(str).apply(lambda x: pd.to_datetime(x, format='%Y%m%d'))

#data['ArrTime'] = pd.to_datetime(data['ArrTime'])
#data['ArrTime'] =  pd.to_datetime(data['ArrTime'], format='%H:%M')

#x=data[['Year','Month','DayofMonth','FlightNum']]
#print(x.head())
#y=x.groupby(['Year','FlightNum']).size().reset_index().groupby('Year').max().rename(columns={0:'count'})
#print(y)

#c=data['ArrTime']
#print(c.head())
#m=pd.to_datetime(b, format='%H%M')
#print(m.head())


#data['ArrTime'] = pd.to_datetime(data['hour'] + data['min'])
#df = data.set_index('ArrTime')
#data['ArrTime'] = pd.to_datetime(data['ArrTime'], format='%H%M')
#df=data['ArrTime']
#print (df)
#df = data.set_index(pd.DatetimeIndex(data['DepTime']))
#print(df.head())
#hours=data['ArrTime']
    #pd.concat([sales, pd.DataFrame(hours, index=sales.index)], axis = 1)
#data['DepTime'] = pd.to_datetime(data['DepTime'])
#data['hour']  = data['DepTime'].dt.hour
#data['min'] = data['DepTime'].dt.minute


#x=data[['hour','min','FlightNum']]

#data['DepTime'] = data.DepTime.dt.hour
#train['Month'] = train.Dates.dt.month

data['ArrTime'] = pd.to_datetime(data['ArrTime'], unit='s')
###str_time=hours.apply(lambda x: datetime.strptime(str(x), "%H:%M"))
#k=pd.to_datetime(hours, '%H:%M')
print(data['ArrTime'])
#str_time = datetime.strptime(hours, "%H:%M")
###print(str_time)

#hours=data['ArrTime']
#data['ArrTime'] = pd.to_datetime(hours, format='%H:%M').dt.hour