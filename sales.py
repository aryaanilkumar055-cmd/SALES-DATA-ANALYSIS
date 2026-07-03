import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_excel(r"C:\Users\ukf\Downloads\SalesDataAnalysis.xlsx") 


print("----- SALES DATA -----") 
print(df) 


df["Sales"] = df["Quantity_Sold"] * df["Price"]

print(df) 


total_sales = df["Sales"].sum() 

print("\nTotal Sales:", total_sales) 


product_sales = df.groupby("Product")["Quantity_Sold"].sum()

best_product = product_sales.idxmax()
print("\nBest Selling Product:", best_product)

monthly_sales = df.groupby("Month")["Sales"].sum() 

print(monthly_sales) 


category_sales = df.groupby("Category")["Sales"].sum() 
print(category_sales) 


plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True) 
plt.show() 


plt.figure(figsize=(10,5))

plt.bar(product_sales.index, product_sales.values)
plt.title("Product-wise Sales")
plt.xlabel("Product") 
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.show() 


plt.figure(figsize=(6,6))
plt.pie(category_sales.values,labels=category_sales.index, autopct='%1.1f%%')
plt.title("Category-wise Revenue Contribution") 
plt.show() 