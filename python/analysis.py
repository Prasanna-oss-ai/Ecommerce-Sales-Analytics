import pandas as pd

file_path = r"C:\Users\gumma\OneDrive\Desktop\Ecommerce-Sales-Analytics\data\cleaned\cleaned_superstore.csv"

df = pd.read_csv(file_path)

# Basic Information
print("Dataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())


# KPIs
print("\n----- KPIs -----")

print("Total Sales:", round(df["Sales"].sum(),2))
print("Total Profit:", round(df["Profit"].sum(),2))
print("Total Orders:", df["Order ID"].nunique())
print("Total Customers:", df["Customer ID"].nunique())


# Best Category
category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Category")
print(category)


# Best Region
region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Region")
print(region)


# Top Products
products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products")
print(products)