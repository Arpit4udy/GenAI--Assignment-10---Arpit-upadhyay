import pandas as pd

students={
    'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}
df=pd.DataFrame(students)
avg_marks = df.groupby('Subject')['Marks'].mean()

print(avg_marks)
count_1=df.groupby('Subject')['Subject'].count()
print(count_1)
count_2=df.groupby('Subject')['Marks'].max()
print(count_2)
