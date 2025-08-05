import pandas as pd

try:
    df = pd.read_csv('hospital_data.csv')
    print("\nOriginal hospital dataframe:")
    print(df)

    # Check missing values
    print("\nMissing values:")
    print(df.isna())

    # Fill missing values: 'Name' by 'Unknown', numerical columns by 0
    df_filled = df.copy()
    df_filled['Name'] = df_filled['Name'].fillna('Unknown')
    df_filled = df_filled.fillna(0)

    print("\nDataframe after filling missing values:")
    print(df_filled)

except FileNotFoundError:
    print(f"Error: 'hospital_data.csv' not found.")
