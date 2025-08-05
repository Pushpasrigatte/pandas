import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})
print(df)
print(df.iloc[0])
print(df.iloc[0, 1])
