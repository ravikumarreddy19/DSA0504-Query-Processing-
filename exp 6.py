import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("GOOGL.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Select data between two dates
filtered_data = df[
    (df["Date"] >= "2022-01-03") &
    (df["Date"] <= "2022-03-11")
]

# Scatter Plot
plt.figure(figsize=(10,5))

plt.scatter(
    filtered_data["Close"],
    filtered_data["Volume"],
    color="red"
)

plt.title("Alphabet Inc. Stock Price vs Trading Volume")
plt.xlabel("Closing Price")
plt.ylabel("Trading Volume")
plt.grid(True)

plt.show()
