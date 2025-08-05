''' syntax=DataFrame(data)
    df.head(n) first n rows
    df.tail(n) last n rows
    df.info() summary -df
    df.describe()-stat summary
    df.shape()-tuple rows and columns
    df.dtypes()-data type(column)
    df.column()-column name  '''
    
import pandas as pd
import numpy as np
data = {
    'patient_id': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006'],
    'Name': ['viajy', 'aloha', 'john', 'doe', 'eswar', None],
    'Age': [34, 30, None, 60, 25, 50],
    'Department': ['corona', 'cardiology', 'orthopedics', 'neurology', 'pediatrics', 'dermatology'],
    'admission_date': ['2025-08-01', '2025-03-02', '2025-04-03', '2025-07-07', '2025-08-05', '2025-08-04'],
    'bill': [2000, 3500, 1500, 5000, 1200, None]
}
df = pd.DataFrame(data)
df.to_csv("hospital_data.csv",index=False)
print("created data sucessfully")

# Print the 'Name' column without index
print(df['Name'].tolist())

#dataframe without series
print(df.to_string(index=False))

