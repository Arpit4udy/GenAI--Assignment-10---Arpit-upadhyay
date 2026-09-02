import pandas as pd
sales={
    'Day':['Mon','Tue','Wed','Thu','Fri'],
    'Revenue':[1200,1500,900,2000,1800]
}
df=pd.DataFrame(sales)
print(f"Total Revenue: {df['Revenue'].sum()}")
print(f"Average Revenue: {df['Revenue'].mean()}")

maximum= df['Revenue'].max()

print(f"Day with Highest Revenue: {df.loc[df['Revenue'] == maximum, 'Day'].values[0]}")

print(f"Days having more than average Revenue:\n{df[df['Revenue']>df['Revenue'].mean()]['Day']}")

df.plot.bar(x='Day', y='Revenue', title='Revenue vs Day')
