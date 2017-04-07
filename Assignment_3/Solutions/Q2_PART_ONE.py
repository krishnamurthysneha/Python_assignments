import pandas as pd
loc= "/Users/Sneha/Documents/python/Python_assignments/Assignment_3/Data/employee_compensation.csv"
data = pd.read_csv(loc)
req_data= data[['Organization Group','Department','Total Compensation']]
gr= req_data.groupby(['Organization Group','Department'])
mean_fr=gr.mean()
final= mean_fr.sort(['Total Compensation'], ascending=[False])
#Writing to a csv file
final.to_csv('output_Q2_PART_ONE.csv',index = False)
print(final.head())