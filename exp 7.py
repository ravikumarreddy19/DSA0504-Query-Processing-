import pandas as pd

# Read CSV file
df = pd.read_csv("sales_data.csv")

# Create Pivot Table
pivot = pd.pivot_table(
    df,
    values="Sale_Value",
    index="Item",
    aggfunc=["max", "min"]
)

print("Maximum and Minimum Sale Value of Items")
print(pivot)
