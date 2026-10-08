import pandas as pd
# import openpyxl

#read_csv --> used to import contents of a csv files onto a dataframe
df=pd.read_csv("data/sample_data.csv")
#Dataframe is a datatype which consists of rows and columns along with headers
# print(df)

# print(df['Age'])  #Only display particular column(s)

# print(df.head(20)) #By default prints the top 5 data, we can also give how many we want to print from the top

# print(df.tail(20))
# print(df['Name'].head(3))

# print(df.loc[1:4,'Name']) #--> Displays a range of data (displays details of a particular data if single-value argument is passed)
#loc takes two arguments --> row range, column range

# print(df.iloc[1:4,0])
#iloc also takes two arguments --> row range, column range (however, it demands indexes of the columns rather than name)

# print(df.shape)
#gives (row_count,column_count)

# print(df['Name'].describe())
# describe give basic statistical analysis of the dataset/series

# print(df.info())
#info gives information regarding data_type, null_count, length

# print(df['Name'].value_counts())
#value_counts groups duplicate data for a particular column and gives its count(number of occurence)

# print(df.isna().sum())
#this statement is used to count how many null data is in the dataframe

print(df)

df.loc[2:4,'Age']=25

print(df)