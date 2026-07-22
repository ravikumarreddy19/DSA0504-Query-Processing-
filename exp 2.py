import pandas as pd

# Read Excel file
df = pd.read_excel("history.xlsx")

print("Employees History")
print(df)

# Employees who have done two or more jobs
result = df["EMPLOYEE_ID"].value_counts()

print("\nEmployees who have done two or more jobs:")
print(result[result >= 2].index.to_list())
