import pandas as pd
from faker import Faker

#Setting up the Faker()
fake_data = Faker()

#Raw data or import from another .CSV file - df = pd.read_csv('abc.csv')
raw_data = {
    'User_Name': ['Alice Wang', 'Bob Dennis', 'Jenny Batina'],
    'Password': ['Pa$$word123', 'Secr3tP@ss', 'testP@ss123'],
    'Email_ID': ['aliwan@yahoo.com', 'bobden@hotmail.com', 'jenbat@gmail.com']
}

#Putting it in DataFrame
df = pd.DataFrame(raw_data)

#Data Transformation
df['User_Name'] = [fake_data.name() for name in range(len(df))]
df['Password'] = [fake_data.password() for password in range(len(df))]
df['Email_ID'] = [fake_data.email() for email in range(len(df))]

print("--- Data Masked Successfully ---")
print(df)
print("Data is now safe to use in Test environments, maintaining privacy :)")
#Exporting
df.to_csv('masked_data.csv', index=False) #removing index nums