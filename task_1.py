import pandas as pd

marks=[78,85,90,66,72]
a=pd.Series(marks)
print(a.values)
print(a.index)
print(a.dtype)
print(f"First Element: {a[0]}")
print(f"Last Two Element: {a.values[:-3:-1]}")