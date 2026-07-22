import pandas as pd

# Read the Excel file
df = pd.read_excel("one.xlsx")

# Display the dataset
print("Departments Dataset:")
print(df)

# Select distinct department IDs
distinct_department_ids = df["DEPARTMENT_ID"].drop_duplicates()

# Display the result
print("\nDistinct Department IDs:")
print(distinct_department_ids.to_string(index=False))
