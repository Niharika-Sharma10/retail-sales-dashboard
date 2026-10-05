# Superstore Sales Analysis

This project is an exploratory data analysis (EDA) of the Superstore retail dataset 
using Python (Pandas, NumPy, and Matplotlib), covering data quality checks, outlier 
detection, business analysis, and data visualization.

## What This Project Covers
- **Data Quality Checks**: Verified the dataset for missing values, duplicates, and 
  infinite values.
- **Outlier Detection**: Used the IQR method to identify outliers in Sales, Quantity, 
  Profit, and Discount.
- **Business Analysis**:
  - Percentage of orders resulting in a loss
  - Categories and sub-categories generating the highest losses
  - Relationship between Discount and Profit
- **Visualization Dashboard**: Built a 6-chart dashboard using bar, line, histogram, 
  pie, horizontal bar, and scatter plots.

## Key Insights

1. **Discount vs. Profit**: Loss-making orders had an average discount of **48.09%**, 
   compared to just **8.14%** for profitable orders. This suggests a strong association 
   between higher discounts and negative profit, although discount alone cannot be 
   established as the cause of the losses.

2. **Outliers in the Technology Category**: During outlier detection on the Sales, 
   Quantity, Profit, and Discount columns, the Technology category stood out with the 
   highest number of outliers in both Sales and Profit. Notably, Profit outliers in 
   Technology included both extreme positive and extreme negative values — indicating 
   that this category has the widest swings between highly profitable and 
   highly loss-making orders.

## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib

## Dataset
[Sample Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) (Kaggle)

## Note
This project was built for practice and learning purposes.
