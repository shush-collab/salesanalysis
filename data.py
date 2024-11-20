import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_mock_data(rows=100):
    data = {
        "Customer ID": [fake.unique.random_int(1000, 9999) for _ in range(rows)],
        "Name": [fake.name() for _ in range(rows)],
        "Email": [fake.email() for _ in range(rows)],
        "Sales Amount": [round(random.uniform(100, 10000), 2) for _ in range(rows)],
        "Purchase Date": [fake.date_this_year() for _ in range(rows)],
        "Region": [random.choice(["North", "South", "East", "West"]) for _ in range(rows)],
    }
    return pd.DataFrame(data)

num = 10000
mock_data = generate_mock_data(num)#num = number of rows of data to produce
mock_data.to_excel("data/crm_data.xlsx", index=False)
print("Mock data saved to 'data/crm_data.xlsx'")

