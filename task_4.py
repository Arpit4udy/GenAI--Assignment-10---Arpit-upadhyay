import pandas as pd

students={
    'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}

df=pd.DataFrame(students)
print(df.iloc[0:3])
print(df.iloc[-2:])
print(df.shape)
print(df.columns)
