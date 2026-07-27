import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/cleaned/cleaned_superstore.csv")
# Top 10 Products by Sales
print("\nTop 10 Products by Sales")
print(
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

# Top 10 Customers by Sales
print("\nTop 10 Customers by Sales")
print(
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)