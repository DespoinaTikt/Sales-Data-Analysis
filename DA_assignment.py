import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_csv('finance_liquor_sales.csv')

# Filter relevant columns for each task
filtered_df = df[['zip_code', 'item_number', 'bottles_sold', 'store_name', 'sale_dollars']]

# Task 1: Max Bottles Sold per Zip Code

# Group by zip_code and item_number, summing bottles_sold for each pair
bottles_sold = filtered_df.groupby(["zip_code", "item_number"])["bottles_sold"].sum().reset_index()

# Convert zip_code to integer for better ordering in the plot
bottles_sold["zip_code"] = bottles_sold["zip_code"].astype(int)

# Find the item with the max bottles sold for each zip_code
idx = bottles_sold.groupby("zip_code")["bottles_sold"].idxmax()
max_bottles = bottles_sold.loc[idx].reset_index(drop=True)

# Sort by bottles_sold in descending order and keep the top 20
sorted_values = max_bottles.sort_values(by="bottles_sold", ascending=False).head(20)

# Plot the results
plt.figure(figsize=(10, 6))
plt.bar(sorted_values["zip_code"].astype(str), sorted_values["bottles_sold"], color="skyblue")
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.title("Max bottles sold per zip code")
plt.xticks(rotation=45)
plt.show()

# Task 2: Compute Sales Percentage per Store

# Calculate the total sales amount
total_sales = filtered_df["sale_dollars"].sum()

# Group by store_name to get total sale_dollars for each store
sales = filtered_df.groupby("store_name")["sale_dollars"].sum()

# Calculate the percentage of each store's sales
percentage_sales = (sales * 100 / total_sales).round(2)

# Sort in ascending order and select the top 15 stores
percentage_sorted_sales = percentage_sales.sort_values(ascending=True).tail(15)

# Plot the results as a horizontal bar chart
plt.figure(figsize=(8, 6))
p = plt.barh(percentage_sorted_sales.index, percentage_sorted_sales.values, color="salmon", height=0.7)
plt.title("Sales Percentage by Store")
plt.xlabel("% Sales", fontsize=12)
plt.bar_label(p, fmt="%.2f")
plt.xlim([0, 20])
plt.show()
