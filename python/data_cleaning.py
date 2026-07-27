import os
import pandas as pd

print("Current folder:")
print(os.getcwd())

print("\nFiles in current folder:")
print(os.listdir())

file_path = r"C:\Users\gumma\OneDrive\Desktop\Ecommerce-Sales-Analytics\data\cleaned\cleaned_superstore.csv"

print("\nChecking file:")
print(os.path.exists(file_path))

df = pd.read_csv(file_path)

print("\nCSV loaded successfully!")
print(df.head())
print(df.shape)