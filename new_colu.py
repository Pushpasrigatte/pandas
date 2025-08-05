import pandas as pd
names=pd.Series(['apples','oranges','kiwi'])
df=names.to_frame(name='names')
#add column
df['price']=[40,50,60]
print(df)