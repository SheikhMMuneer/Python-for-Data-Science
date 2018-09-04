import pandas as pd
import  os

# Specify Full path to File 1st Method
stats = pd.read_csv('F:\\DemographicData.csv')
print(stats)
print("Lenght of Data " , len(stats))  # means 195 rows imported


cols = stats.columns
print("Columns are " , cols)
print("Length of Columns  " , len(cols))


# Change Working Directory  2nd Method
print(os.getcwd())  # It will get Current Working Directory
os.chdir('C:\\Users\\MUNEER\\Desktop')  # It will get Current Working Directory
print(os.getcwd())


# for top rows
print(stats.head())


# for top rows
print(stats.head(6))

# for bottom rows
print(stats.tail())

# for bottom rows
print(stats.tail(15))


# Information on the columns
print(stats.info())

# stats on the columns
print(stats.describe())

# stats on the columns Tranpose  Horizontally
trans = stats.describe().transpose()
print(trans)


print(stats.head())
print(stats.columns)

# To change columns
stats.columns = ['a','b','c','d','e']
print(stats.head())


stats.columns = ['CountryName','CountryCode','Birthrate','Internetusers','IncomeGroup']
print(stats.head())


#Subsetting dataFrames in Pandas
print(stats.head())

# Three parts - Rows Cols , Combine the two
print(stats[21:26])   # to print values from rows 21 to 26
print(stats[100:110])
print(stats[:])
print(stats[185:])
print(stats[:10])


#Reverse the Data Frame
print(stats[::-1])
print(stats[::20])  # Get every 20th country

#Get only one Column
print(stats.columns)
print(stats['CountryName'].head())
print(stats[['CountryName','Birthrate']].head())
print(stats[['Birthrate','CountryName']].head())


#Quick Access of Column
#print(stats['Birthrate'])
print(stats.Birthrate)
print(stats.Birthrate.head())

#Combining Rows and Column

print(stats[4:8][['CountryName','Birthrate']])  # Both are same
print(stats[['CountryName','Birthrate']][4:8])