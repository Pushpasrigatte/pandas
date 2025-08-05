import pandas as pd
data={'Name':['mark','steve','jenny'],
      'Age':[22,21,22],
      'Branch':['it','csm','eee']}
dframe=pd.DataFrame(data)
print(dframe)
print(dframe[['Name','Branch']])
print(dframe.iloc[2])
print(dframe['Name'])
stiphend=[10000,11000,20000]
print(dframe)
dframe.insert(1,'salary',stiphend)
print(dframe)
dframe.at[2,'age']=25
print(dframe)