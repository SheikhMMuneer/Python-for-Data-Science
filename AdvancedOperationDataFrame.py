import pandas as pd
import os


#Basic Operation with DataFrames
stats = pd.read_csv('F:\\DemographicData.csv')
print(stats.head())


stats.columns = ['CountryName','CountryCode','Birthrate','Internetusers','IncomeGroup']
print(stats[['CountryCode','Birthrate','Internetusers']][4:8])

#Mathematical Operations
result = stats.Birthrate * stats.Internetusers
print(result.head())

#Add Column
stats['MyCalc'] =  stats.Birthrate * stats.Internetusers
print(stats.head())


#Drop a Column
stats = stats.drop('MyCalc',1)
print(stats.head())


#Filtering a Data Frame
filter =   stats.Internetusers < 2
#print(filter)
print(stats[filter])

filter_Birth = stats.Birthrate > 40
print(stats[filter_Birth])

# And in Filter
print(filter & filter_Birth)
print(stats[filter & filter_Birth])
print(stats[( stats.Internetusers < 2) & ( stats.Birthrate > 40)])
print(stats[stats.IncomeGroup == 'High income'])

# How to get unique categories
print(stats.IncomeGroup.unique())

#Find out everything about Malta
print(stats[stats.CountryName == 'Malta'])

#.at  for labels
#.iat  foe Integers Location
print(stats.head())
print(stats.iat[3,4])  # row,col
print(stats.iat[0,1])


print(stats.at[2,"Birthrate"])  # RowNumner  and Birthdate
sub10 = stats[::10]

print(sub10)
print("By iat Method" , sub10.iat[10,0])
print("By at Method" , sub10.at[10,"CountryName"])  # 10 is Label 10 and CountryName

