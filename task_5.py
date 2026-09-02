import pandas as pd

students={
    'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}

df=pd.DataFrame(students)

print(df.info())
print(df.describe())
print(df.head())
print(df.tail())

df=df.sort_values(by='Marks',ascending=False)
print(df)


# Resetting Index -
df = df.reset_index(drop=True)
print(df)