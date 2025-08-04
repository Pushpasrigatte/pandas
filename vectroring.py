import pandas as pd 
print("enter 4 numbers,space seperated:")
numbers=input().strip().split()
numbers=[float(num) for num in numbers]
try:
    if len(numbers)!=5:
        raise ValueError("give 4 numbers only!!!")
    series=pd.Series(numbers,index=['a','b','c','d','e'])
    print("\noriginal series:")
    print(series)
# doubling vector operations
    doubled=series*2
    print("\nseries after doubloing series:")
    print(doubled)
# addding 100 to all values vector operations
    added=series+100
    print("\nseries after adding series:")
    print(added)
except ValueError as e:
     print(f"Error: {e}")