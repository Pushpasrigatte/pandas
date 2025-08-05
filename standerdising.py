import pandas as pd
try:
    df=pd.read_csv('hospital_data.csv')
    series=df['Name']
    print("\n orginal name series")
    print(series)
    clean_series=series.str.title().str.strip()
    print("name series after standardizing with (titlecase,strripped space:):")
    print(clean_series)
    # saving to csv dataframe
    df['Name']=clean_series
    df.to_csv('hospital_data.csv',index=False)
    print("data saved to csv file")
except FileNotFoundError:
    print(f"Error: 'hospital_data.csv' not found.")
    
    