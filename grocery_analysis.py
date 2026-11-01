import pandas as pd
import matplotlib.pyplot as plt

# 1. Grocery sales dataset
data = {
    "Product": [
        "Rice", "Milk", "Sugar", "Cooking Oil", "Wheat Flour",
        "Biscuits", "Eggs", "Bread", "Fruits", "Vegetables"
    ],
    "January": [5000, 3000, 2000, 4500, 2500, 1800, 2200, 1500, 2800, 3200],
    "February": [6000, 3500, 2300, 4800, 2700, 2000, 2400, 1700, 3000, 3500],
    "March": [7000, 4000, 2500, 5200, 3000, 2200, 2600, 1900, 3400, 3800],
    "April": [6500, 4500, 2700, 5500, 3200, 2500, 2800, 2100, 3600, 4000]
}

df = pd.DataFrame(data)
months = ["January", "February", "March", "April"]

# 2. Calculate total sales for each product
df["Total Sales"] = df[months].sum(axis=1)

print("GROCERY SALES DATA")
print(df.to_string(index=False))

print("\nTOTAL SALES: Rs.", df["Total Sales"].sum())
print("BEST SELLING PRODUCT:",
      df.loc[df["Total Sales"].idxmax(), "Product"])
print("LOWEST SELLING PRODUCT:",
      df.loc[df["Total Sales"].idxmin(), "Product"])

# 3. Calculate category sales
categories = {
    "Staples": ["Rice", "Sugar", "Cooking Oil", "Wheat Flour"],
    "Dairy": ["Milk", "Eggs"],
    "Snacks": ["Biscuits"],
    "Bakery": ["Bread"],
    "Fresh Food": ["Fruits", "Vegetables"]
}

category_sales = {
    category: df[df["Product"].isin(products)]["Total Sales"].sum()
    for category, products in categories.items()
}

monthly_sales = df[months].sum()

# 4. Create four charts
fig, axes = plt.subplots(2, 2, figsize=(16, 11))

# Bar chart: Compare all products
sorted_df = df.sort_values("Total Sales")
axes[0, 0].barh(
    sorted_df["Product"], sorted_df["Total Sales"]
)
axes[0, 0].set_title("Sales Comparison of 10 Products")
axes[0, 0].set_xlabel("Sales (Rs.)")

# Line chart: Monthly sales
axes[0, 1].plot(
    months, monthly_sales.values, marker="o"
)
axes[0, 1].set_title("Monthly Sales Trend")
axes[0, 1].set_ylabel("Sales (Rs.)")
axes[0, 1].grid(True)

# Pie chart: Product sales share
axes[1, 0].pie(
    df["Total Sales"],
    labels=df["Product"],
    autopct="%1.1f%%",
    textprops={"fontsize": 8}
)
axes[1, 0].set_title("Sales Share by Product")

# Bar chart: Category comparison
axes[1, 1].bar(
    list(category_sales.keys()),
    list(category_sales.values())
)
axes[1, 1].set_title("Sales by Category")
axes[1, 1].set_ylabel("Sales (Rs.)")
axes[1, 1].tick_params(axis="x", rotation=20)

fig.suptitle(
    "GROCERY STORE SALES ANALYSIS DASHBOARD",
    fontsize=17
)
plt.tight_layout()

# 5. Save and display dashboard
plt.savefig("grocery_sales_dashboard.png", dpi=150)
plt.show()

print("\nMonthly Sales:")
print(monthly_sales)
print("\nCategory Sales:")
print(pd.Series(category_sales))
print("\nDashboard saved as grocery_sales_dashboard.png")