
import pandas as pd

# Load dataset
data = pd.read_csv("sanju_sales_data.csv")

# Create Total Sales column
data["Total_Sales"] = data["Quantity"] * data["Price"]

# Monthly Sales
data["Date"] = pd.to_datetime(data["Date"])
data["Month"] = data["Date"].dt.month

monthly_sales = data.groupby("Month")["Total_Sales"].sum()
print("Monthly Sales:")
print(monthly_sales)

# Top 5 Products
top_products = data.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
print("\nTop Products:")
print(top_products.head())
