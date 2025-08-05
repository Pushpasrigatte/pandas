import pandas as pd
try:
    df=pd.read_csv("hospital_data.csv")
    print("\n Hospital DataFrame:")
    print(df)
#Display basic info
    print("\n DataFrame INFO:")
    print(df.info())
    print("\n summary statistics:")
    print(df.describe())
except FileNotFoundError:
    print(f"Error:'hospital_data.csv' not found.") 