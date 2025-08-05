import pandas as pd
import datetime 
try: 
    df = pd.read_csv("hospital_data.csv")
    series = df['admission_date']
    print("\nOriginal Admission_Date series")
    print(series)
    print("\n convert admission dateformat from y/m/d:")
    confirm=input().strip().lower()
    if confirm =='yes':
    # Convert string to datetime
       date_series = pd.to_datetime(series, format='%Y-%m-%d')
       print("\nAdmission Date series after converting to datetime:") 
       print(date_series)

    # Update and save the dataframe
    df['admission_date'] = date_series 
    df.to_csv('hospital_data.csv', index=False)
    print("\nUpdated CSV saved to 'hospital_data.csv'")

except FileNotFoundError:
    print("Error: 'hospital_data.csv' not found.")
