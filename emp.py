import pandas as pd

data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen'],
    'Q1': [25000, 30000, 22000, 27000, 26000, 24000, 28000, 31000],
    'Q2': [27000, 32000, 21000, 26000, 29000, 25000, 30000, 33000],
    'Q3': [29000, 31000, 23000, 28000, 27000, 26000, 32000, 34000],
    'Q4': [30000, 33000, 24000, 29000, 31000, 28000, 33000, 35000]
}

df = pd.DataFrame(data)

# Step 1: Total Sales
df['TotalSales'] = df[['Q1', 'Q2', 'Q3', 'Q4']].sum(axis=1)

# Step 2: Top Salesperson per Region
top_performers = df.loc[df.groupby('Region')['TotalSales'].idxmax()]

# Step 3: Final output
final_df = top_performers[['Region', 'Salesperson', 'TotalSales']].sort_values(by='Region').set_index('Region')

print(final_df)
