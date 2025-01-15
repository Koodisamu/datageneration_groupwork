import numpy as np
from faker import Faker
import pandas as pd


#Generating user ID's and signup datesn
num_users = 100
user_ids = np.arange(1, num_users+1)

start_date = np.datetime64('2023-01-01')
end_date = np.datetime64('2025-01-15') 
ordered_dates = np.arange(start_date, end_date, dtype='datetime64[D]')
ordered_dates = np.random.choice(ordered_dates, size=num_users) 
ordered_dates = np.sort(ordered_dates)



# Generating the name and email part of the user data using Faker library 

fake = Faker()
namelist =[]
emaillist = []


for _ in range(100):  
    profile = fake.profile()
    name = profile['name']
    namelist.append(name)
    first_name, last_name = name.split(" ", 1)  
    email = f"{first_name.lower()}.{last_name.lower()}@{fake.domain_name()}" 
    emaillist.append(email)

df = pd.DataFrame({'user_id': user_ids, 'signup_date': ordered_dates, 'name': namelist, 'email': emaillist})

# Insert 10 empty values to emails

missing_indices = np.random.choice(df.index, size=10, replace=False)  
df.loc[missing_indices, 'email'] = np.nan 

df.to_csv('userdata.csv', index=False)

print(df)