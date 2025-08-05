import pandas as pd
try:
    df=pd.read_csv("hospital_data.csv")
    print("orignal series")
    print(df)
    # grouping by department
    grouped=df.groupby('Department')['bill'].mean()
    print("\n average medical cost by department")
    print(grouped)
except FileNotFoundError:
    print("csv file not found")