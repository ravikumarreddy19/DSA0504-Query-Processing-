import pandas as pd

# Read Excel file
df = pd.read_excel("jobs.xlsx")

print("Jobs Dataset")
print(df)

# Sort by JOB_TITLE in descending order
result = df.sort_values(by="JOB_TITLE", ascending=False)

print("\nJobs in Descending Order of Job Title")
print(result)
