import numpy as np
from faker import Faker
import pandas as pd


#Generating user ID's and signup datesn
num_users = 100
user_ids = np.arange(1, num_users+1)
print(user_ids)

start_date = np.datetime64('2023-01-01')
end_date = np.datetime64('2025-01-01') 
ordered_dates = np.arange(start_date, end_date, dtype='datetime64[D]')
ordered_dates = np.random.choice(ordered_dates, size=num_users, replace=False) 
ordered_dates = np.sort(ordered_dates)


#print(ordered_dates)


# Generating the name and email part of the user data using Faker library 

fake = Faker()
fake_data = []
namelist =[]
emaillist = []


for _ in range(100):  
    profile = fake.profile()
    name = profile['name']
    namelist.append(name)
    first_name, last_name = name.split(" ", 1)  
    email = f"{first_name.lower()}.{last_name.lower()}@{fake.domain_name()}" 
    emaillist.append(email)
    fake_data.append({'name': name, 'email': email})


# df_fake = pd.DataFrame(fake_data)
# print(df_fake)


df = pd.DataFrame({'user_id': user_ids, 'signup_date': ordered_dates, 'name': namelist, 'email': emaillist})

print(df.head(20))







# Generating the product catalogue with Hardware store theme and sem

categories = ['Power Tools', 'Hand Tools', 'Plumbing', 'Electrical', 'Building Materials']
num_products = 20

product_data = []
for i in range(1, num_products + 1):
    category = np.random.choice(categories)
    product_name = fake.bs().title()  # semi-realistic product names

    if category == 'Power Tools':
        price = fake.pyfloat(right_digits=2, positive=True, min_value=50, max_value=500)
    elif category == 'Hand Tools':
        price = fake.pyfloat(right_digits=2, positive=True, min_value=5, max_value=100)
    elif category == 'Plumbing':
        price = fake.pyfloat(right_digits=2, positive=True, min_value=10, max_value=200)
    elif category == 'Electrical':
        price = fake.pyfloat(right_digits=2, positive=True, min_value=2, max_value=50)
    elif category == 'Building Materials':
        price = fake.pyfloat(right_digits=2, positive=True, min_value=20, max_value=300)
    else:
        price = fake.pyfloat(right_digits=2, positive=True, min_value=1, max_value=1000)  # Default range

    product_data.append({
        'Product ID': i,
        'Product Name': product_name,
        'Category': category,
        'Price': price
    })

df_product = pd.DataFrame(product_data)
print(df_product)