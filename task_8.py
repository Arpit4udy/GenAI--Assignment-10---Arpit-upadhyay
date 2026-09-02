import pandas as pd


students={
    'Name':['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}
df=pd.DataFrame(students)
df.plot.bar(x='Name',y='Marks')
df.plot.line(y='Marks')
df['Marks'].plot.hist()