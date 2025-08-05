import pandas as pd
try:
    df=pd.read_csv("hospital_data.csv")
    series=df['bill']
    print("orignal hospital bill")
    print(series)
    
    #user manual input
    print("enter patient id to update")
    patient_id=input().strip()
    print("enter new bill for {patient_id}:")
    new_cost=float(input())
    
    # update bill series and save
    if patient_id in df['patient_id'].values:
        index=df[df[patient_id]==patient_id].index[0]
        series[index]=new_cost
        print("updated medical bill series.")
        print(series)
    # update dataframe and save
        df['bill']=series
        df.to_csv("hospital_data.csv",index=False)
        print("updated csv saved to 'hospital_data.csv'.")
    else:
        print(f"Error:p_id {patient_id} not found.")
except FileNotFoundError:
    print(f"Error: 'hospital_data.csv' not found.")