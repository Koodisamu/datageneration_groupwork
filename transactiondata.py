import numpy as np
from faker import Faker
import pandas as pd

num_taransactions = 1000
trans_user_ids = np.random.randint(1, 101, num_taransactions)

trans_ids = np.arange(1, num_taransactions + 1)

trans_product_ids = np.random.randint(1, 21, num_taransactions)

trans_quantity = np.random.randint(1,10, num_taransactions)

start_date = np.datetime64('2023-01-01')
end_date = np.datetime64('2025-01-15') 
ordered_dates = np.arange(start_date, end_date, dtype='datetime64[D]')
ordered_dates = np.random.choice(ordered_dates, size=1000) 
trans_ordered_dates = np.sort(ordered_dates)

df_trans = pd.DataFrame({'transaction_id': trans_ids, 'user_id': trans_user_ids, 'product_id': trans_product_ids, 'quantity': trans_quantity, 'transaction_date':trans_ordered_dates})

df_trans.to_csv('transactiondata.csv', index=False)