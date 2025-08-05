import pandas as pd
import numpy as np

try:
    df = pd.read_csv('hospital_data.csv')
    series=df['Age']
    print("\nOriginal age series:")
    print(series)
    #replace invalid ages.<0 or >120 with NaN
    clean_series=series.where((series>=0) & (series<=120),np.nan)
    print("\n age series after replacing invalid ages with NaN:")
    print(clean_series)
    df['age']=clean_series
    df.to_csv("hospital_data.csv",index=False)
    print("file updated succesfully")
except FileNotFoundError:
    print(f"Error: 'hospital_data.csv' not found.")

