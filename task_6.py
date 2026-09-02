import pandas as pd

students={
    'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}
df=pd.DataFrame(students)


print(df[df['Marks']>75])
print(df[df['Subject']=='Math'])
print(df[df['Marks']>df['Marks'].mean()])
print(df[df['Marks']<70])