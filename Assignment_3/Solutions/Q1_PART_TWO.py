import pandas as pd
loc= "/Users/Sneha/Documents/material_for_python/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/vehicle_collisions.csv"
data = pd.read_csv(loc)
req_data=data[['BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
def num_of_veh(v1):
    count=0
    if (type(v1[1])==str):
        count+=1
    if (type(v1[2])==str):
        count+=1
    if (type(v1[3])==str):
        count+=1
    if (type(v1[4])==str):
        count+=1
    if (type(v1[5])==str):
        count+=1
    return count
col=['BOROUGH','ONE_VEHICLE_INVOLVED','TWO_VEHICLE_INVOLVED','THREE_VEHICLE_INVOLVED','MORE_VEHICLE_INVOLVED']
df=pd.DataFrame(columns=col)
def trans(a):
    df.loc[len(df)]=[a[0],'0','0','0','0']
def add_val(s):
    if s[1]==1:
        df.loc[df.BOROUGH==s[0],'ONE_VEHICLE_INVOLVED']=s[2]
    if s[1]==2:
        df.loc[df.BOROUGH==s[0],'TWO_VEHICLE_INVOLVED']=s[2]
    if s[1]==3:
        df.loc[df.BOROUGH==s[0],'THREE_VEHICLE_INVOLVED']=s[2]
    if s[1]==4:
        df.loc[df.BOROUGH==s[0],'MORE_VEHICLE_INVOLVED']=s[2]

req_data['Vehicles_involved']=req_data.apply(num_of_veh,axis=1)
r1=req_data.groupby(['BOROUGH','Vehicles_involved']).size().reset_index(name='Count')
r1.loc[:, 'Vehicles_involved'].replace([0, 5], [4, 4], inplace=True)
r2=r1.groupby(['BOROUGH','Vehicles_involved']).sum().reset_index()
r2.apply(trans,axis=1)
df.drop_duplicates('BOROUGH', inplace=True)
r2.apply(add_val,axis=1)
df.to_csv('output_Q1_PART_TWO.csv',index = False)
print(df.head())