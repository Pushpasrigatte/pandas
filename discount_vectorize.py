import pandas as pd
try:
    df=pd.read_csv("hospital_data.csv")
    print("orignal series")
    print(df)
    #add discount_cost column(10% discount)
    df['discount']=df['bill']*0.9
    #sorting by bill
    sorted_df=df.sort_values('bill',ascending=False)
    print("\n sorted by medical bills(decending_order):")
    print(sorted_df)
except FileNotFoundError:
    print(f"Error: 'hospital_data.csv' not found.")

    