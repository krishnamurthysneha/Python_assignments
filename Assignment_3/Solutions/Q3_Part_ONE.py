import pandas as pd
loc = '/Users/Sneha/Documents/material_for_python/DataAnalysis4Python_Spring17/Assignments/Assignment 3/Data/cricket_matches.csv'
data= pd.read_csv(loc)
home_win=data[data['home']== data['winner']]

home_win1=home_win[['home','winner','innings1','innings1_runs','innings2','innings2_runs']]
#print (home_win1.head())
z = home_win1[home_win1['home'] == home_win1['innings1']][['home','innings1_runs']]
y = home_win1[home_win1['home'] == home_win1['innings2']][['home','innings2_runs']]
y=y.rename(columns={'innings2_runs': 'innings1_runs'})
fr= [z,y]
final=pd.concat(fr)
output = final['innings1_runs'].groupby(final['home']).mean()
output.to_csv("output_Q3_PART_ONE.csv",index = False)
print (output.head())