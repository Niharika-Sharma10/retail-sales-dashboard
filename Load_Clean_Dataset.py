import pandas as pd 
import numpy as np
df=pd.read_csv(r"Sample - Superstore.csv",encoding='latin1')

# The dataset is free of duplicates, missing values, and infinite values.

# Extracted only the numbers from the dataset.
print(df.select_dtypes(include='number').columns)
print((df[['Row ID','Postal Code','Sales','Quantity','Profit']]<0).sum())

# Explore the Profit Negative values

# How many orders are resulting in a loss?
print((df['Profit'] < 0).sum() / len(df) * 100)

# Which category is suffering the highest losses?
print(df[df['Profit'] < 0].groupby('Category')['Profit'].sum())

# Which sub-category is incurring the highest loss?
print(df[df['Profit'] < 0].groupby('Sub-Category')['Profit'].sum().sort_values())

# Discount Connection and Comparsion between Profit Discount and Loss Disocunt 
print(df[df['Profit'] < 0]['Discount'].describe())
print(df[df['Profit'] >= 0]['Discount'].describe())

# Outlier Detection 
for col in ['Sales', 'Quantity', 'Profit', 'Discount']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"{col}: {outliers.shape[0]} outliers")

# Explore Sales Outliers 
Q1= df["Sales"].quantile(0.25)
Q3= df["Sales"].quantile(0.75)
IQR=Q3-Q1
upper= Q3+1.5*IQR
high_sales=df[df["Sales"]>upper].sort_values("Sales",ascending=False)
print(high_sales[['Product Name', 'Sales', 'Quantity', 'Category']].head(10))

# Explore Profit Outliers 
Q1=df["Profit"].quantile(0.25)
Q3=df["Profit"].quantile(0.75)
IQR=Q3-Q1
lower=Q1-1.5*IQR
upper=Q3+1.5*IQR
low_profit=df[df["Profit"]<lower].sort_values("Profit")
high_profit=df[df["Profit"]>upper].sort_values("Profit",ascending=False)
print(low_profit[['Product Name', 'Profit', 'Quantity', 'Category']].head(10))
print(high_profit[['Product Name', 'Profit', 'Quantity', 'Category']].head(10))

# Explore Quantity Outliers
Q1= df["Quantity"].quantile(0.25)
Q3= df["Quantity"].quantile(0.75)
IQR=Q3-Q1
upper= Q3+1.5*IQR
high_sales=df[df["Quantity"]>upper].sort_values("Quantity",ascending=False)
print(high_sales[['Product Name', 'Sales', 'Quantity', 'Category']].head(10))

# Explore Discount Outliers
Q1= df["Discount"].quantile(0.25)
Q3= df["Discount"].quantile(0.75)
IQR=Q3-Q1
upper= Q3+1.5*IQR
high_sales=df[df["Discount"]>upper].sort_values("Discount",ascending=False)
print(high_sales[['Product Name', 'Discount', 'Quantity', 'Category']].head(10))

df.to_csv("cleaned_superstore.csv", index=False)

