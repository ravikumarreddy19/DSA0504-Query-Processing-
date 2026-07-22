import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("Alphabet_stock_data.csv")

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Select data between two dates
data = df[(df["Date"] >= "2020-01-01") &
          (df["Date"] <= "2020-02-28")]

# Create line plot
plt.figure(figsize=(10,5))
plt.plot(data["Date"], data["Close"], marker='o')

plt.title("Alphabet Inc. Historical Stock Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()
