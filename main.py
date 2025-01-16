import numpy as np
from faker import Faker
import pandas as pd

# Load the .csv files to dataframes
df_user = pd.read_csv('userdata.csv') 

df_product = pd.read_csv('productdata.csv')

df_trans = pd.read_csv('transactiondata.csv')

#Data cleaning
df_user = df_user.fillna({'email': 'Missing'})

# Merge datasets
# Merging user and transaction data
merged_df_user_trans = pd.merge(df_user, df_trans, on='user_id', how='inner')

# Merging product and transaction data
merged_df_product_trans = pd.merge(df_product, df_trans, on='product_id', how='inner')

# Merging all datasets
merged_df_all = pd.merge(merged_df_product_trans, df_user[['user_id', 'name','email','signup_date']], on='user_id', how='inner')

# Top 5 most popular products
df_product_sum = merged_df_all.groupby(['user_id','name']).apply(lambda x: (x['price'] * x['quantity']).sum())

df_product_top5 = merged_df_all.groupby(['product_id','product_name','price']).apply(lambda x: (x['price'] * x['quantity']).sum())
df_product_top5 = df_product_top5.reset_index(name='total_sales') 
df_product_top5 = df_product_top5.sort_values('total_sales', ascending=False)
df_product_top5 = df_product_top5.head(5)
df_product_top5 = df_product_top5.set_index('product_id')

averageprice_top5 = round(df_product_top5['price'].mean())

print(f"Top 5 products: \n{df_product_top5}")
print(f"\nRounded average price of top 5 products: {averageprice_top5} € \n")


# Top category by quantity sold
df_category = merged_df_all.groupby(['category'])['quantity'].sum()
df_category = df_category.sort_values(ascending=False)
df_category = df_category.reset_index(name='total_quantity')
print(f"Categories listed by popularity: \n{df_category}")
print(f"\nCategory with the most quantity sold: {df_category['category'].iloc[0]}")

# Export merged dataset to .json
merged_df_all.to_json("merged_data.json", orient='table') # Test orient=""s

# Import the dataset back to a dataframe
df_from_json = pd.read_json("merged_data.json", orient="table")
#print(df_from_json)