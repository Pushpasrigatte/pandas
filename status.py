import pandas as pd
try:
    df=pd.read_csv("hospital_data.csv")
    print("orignal hospital dataframe")
    print(df)
#add a status column , based on age
    df['status']=df['Age'].apply(lambda x:'senior' if x>=50 else "adult" if x>=18 else 'unknown')
    print("data frame with status column")
    print(df)
    df.to_csv("hospital_data_updated.csv",index=True)
    print("new data updated sucessfully as hospital_data_updated.csv")
except FileNotFoundError:
    print(f"Error: 'hospital_data.csv' not found.")
