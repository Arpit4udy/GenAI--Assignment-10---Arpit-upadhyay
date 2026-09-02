import pandas as pd

marks=pd.Series([78,85,90,66,72])
print(f"Maximum Marks: {marks.max()}")
print(f"Maximum Marks: {marks.min()}")
print(f"Maximum Marks: {marks.sum()}")
print(f"Maximum Marks: {marks.mean()}")

passed=marks.apply(lambda x:x>=70)
print(passed)
print(f"Total Students Passed: {passed.sum()}")