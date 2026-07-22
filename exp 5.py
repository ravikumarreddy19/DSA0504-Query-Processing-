import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("Alphabet_stock_data.csv")

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Select data between two dates
data = df[(df["Date"] >= "2020-01-01") &
          (df["Date"] <= "2020-02-28")]

# Create bar plot
plt.figure(figsize=(10,5))
plt.bar(data["Date"], data["Volume"])

plt.title("Alphabet Inc. Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.xticks(rotation=45)

plt.show()
