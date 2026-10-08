import pandas as pd

df=pd.read_csv("data/dirty_cafe_sales.csv")


#Normalize Header (Price Per Unit --> price_per_unit)
columns_to_be_renamed=df.columns.to_list()

renamed_column_dict={}

for column in columns_to_be_renamed:
    renamed_column_dict[column]=column.lower().replace(" ","_")


df=df.rename(columns=renamed_column_dict)
#dictionary is a mapper --> specific case to this, maps old_column_name to new_column_name

# Changing all the ERROR and UNKNOWN value to None
# df['item']=df['item'].replace(['ERROR','UNKNOWN'],None) For when we want to replace something in a single column only
df=df.replace(['ERROR','UNKNOWN'],None)


#Change datatype of Quantity, Price Per Unit, Total Spent to float
df['quantity']=pd.to_numeric(df['quantity'],errors='coerce')
df['price_per_unit']=pd.to_numeric(df['price_per_unit'],errors='coerce')
df['total_spent']=pd.to_numeric(df['total_spent'],errors='coerce')


df['transaction_date']=pd.to_datetime(df['transaction_date'],errors='coerce')


df['item']=df['item'].astype('str')
df['payment_method']=df['payment_method'].astype('str')
df['location']=df['location'].astype('str')

# print(df['item'].value_counts().sum())


#quantity=value, price_per_unit, total_spent is null


# print(df.head(20))

# print(df.loc[df['total_spent'].isna()])

print(df.loc[df['item'].isna()])


# print(df.loc[df['item'].isna() & df['price_per_unit'].isna()])

#inplace=True makes sure the original dataframe drops the rows as well.
df.drop(df.loc[df['item'].isna() & df['price_per_unit'].isna()].index.to_list(),inplace=True)



# print(df.loc[df['item'].isna() &df['price_per_unit'].isin([3.0,4.0])].index.to_list())

df.drop(df.loc[df['item'].isna() &df['price_per_unit'].isin([3.0,4.0])].index.to_list(),inplace=True)

# print(df.head(20))

# print(df.loc[df['item'].isna(),'price_per_unit'].value_counts())

#Mapper that maps item_name based on the row's price_per_unit
df.loc[df['item'].isna() & df['price_per_unit'].isin([5.0]),'item']="Salad"
df.loc[df['item'].isna() & df['price_per_unit'].isin([2.0]),'item']="Coffee"
df.loc[df['item'].isna() & df['price_per_unit'].isin([1.0]),'item']="Cookie"
df.loc[df['item'].isna() & df['price_per_unit'].isin([1.5]),'item']="Tea"

df.loc[df['price_per_unit'].isna() & df['item'].isin(['Juice','Cake']),'price_per_unit']=3.0
df.loc[df['price_per_unit'].isna() & df['item'].isin(['Sandwich','Smoothie']),'price_per_unit']=4.0
df.loc[df['price_per_unit'].isna() & df['item'].isin(['Coffee']),'price_per_unit']=2.0
df.loc[df['price_per_unit'].isna() & df['item'].isin(['Salad']),'price_per_unit']=5.0
df.loc[df['price_per_unit'].isna() & df['item'].isin(['Cookie']),'price_per_unit']=1.0
df.loc[df['price_per_unit'].isna() & df['item'].isin(['Tea']),'price_per_unit']=1.5


df['quantity']=df['total_spent']/df['price_per_unit']

df.to_csv("data/cleaned_data.csv") #Writes the processed df(dataframe variable) onto a csv file based on the given filepath 
# Juice     3.0               1110
# Coffee    2.0               1108
# Cake      3.0               1085
# Salad     5.0               1082
# Sandwich  4.0               1082
# Smoothie  4.0               1036
# Cookie    1.0               1026
# Tea       1.5               1023