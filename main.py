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

#print(merged_df_user_trans.head(20))

merged_df_product_trans = pd.merge(df_product, df_trans, on='product_id', how='inner')

#merged_df_all = pd.merge(merged_df_user_trans, merged_df_product_trans, on='transaction_id', how='inner')

# print(merged_df_product_trans.head(20))

#print(merged_df_all)

# summa = merged_df_product_trans.groupby('user_id').apply(lambda x: (x['price'] * x['quantity']).sum())

#print(summa)