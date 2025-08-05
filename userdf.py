import pandas as pd 
n=int(input("enter number of profiles:"))
names=[]
ages=[]
branches=[]
for i in range(n):
    print(f"-------enter {i+1}-------")
    name=input("enter name:")
    age=input("enter age:")
    branch=input("enter your branch:")
    names.append(name)
    ages.append(age)
    branches.append(branch)
data={'Name':names,'age':ages,'branch':branches}
df=pd.DataFrame(data)
print("\nDataFrame created...........")
print(df)
    
    