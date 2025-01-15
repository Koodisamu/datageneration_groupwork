from faker import Faker
import pandas as pd
import numpy as np
import random

fake = Faker()
categories = ['Power Tools', 'Hand Tools', 'Plumbing', 'Electrical', 'Building Materials']
num_products = 20

hardware_words = {
    'Power Tools': ['Drill', 'Saw', 'Sander', 'Grinder', 'Nail Gun'],
    'Hand Tools': ['Hammer', 'Screwdriver', 'Wrench', 'Pliers', 'Tape Measure'],
    'Plumbing': ['Pipe', 'Valve', 'Faucet', 'Fitting', 'Connector'],
    'Electrical': ['Wire', 'Switch', 'Outlet', 'Breaker', 'Fixture'],
    'Building Materials': ['Wood', 'Cement', 'Brick', 'Tile', 'Insulation']
}

product_data = []
for i in range(1, num_products + 1):
    category = np.random.choice(categories)
    product_words = random.sample(hardware_words[category], 2)
    product_name = ' '.join(product_words) + ' ' + fake.company_suffix()

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
        price = fake.pyfloat(right_digits=2, positive=True, min_value=1, max_value=1000)

    product_data.append({
        'Product ID': i,
        'Product Name': product_name,
        'Category': category,
        'Price': price
    })

df_product = pd.DataFrame(product_data)
print(df_product)

df_product.to_csv('productdata.csv', index=False)