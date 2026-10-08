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

print(df.head(10))


#quantity=value, 
# condition=(

# )


