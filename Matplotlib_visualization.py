import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv(r"cleaned_superstore.csv")

# Bar Garph Comparison between categories, which has the highest/lowest Sales 
Category_sales = df.groupby("Category")["Sales"].sum()
fig,ax=plt.subplots(3,2,figsize=(16,18))
ax[0,0].bar(Category_sales.index,Category_sales.values,color="blue")
ax[0,0].set_title("Comparsion Between Categories according to Sales")
ax[0,0].set_xlabel("Category")
ax[0,0].set_ylabel("Sales")

# Line plot to check Profit Trend 
df["Order Date"]=pd.to_datetime(df["Order Date"])
Profit_year=df.groupby(df["Order Date"].dt.year)["Profit"].sum()
ax[0,1].plot(Profit_year.index,Profit_year.values,marker='o',color="red")
ax[0,1].set_title("Profit Trend")
ax[0,1].set_xlabel("Years")
ax[0,1].set_ylabel("Profit")

# Histogram of Quantity Distribution 
Quantity_count=df["Quantity"]
ax[1,0].hist(Quantity_count,bins=5,color="purple",edgecolor="black")
ax[1,0].set_title("Quantity Distribution Histogram")
ax[1,0].set_xlabel("Quantity")
ax[1,0].set_ylabel("Frequency")

# Pie Chart of Sales From Each Region 
Region_Sales=df.groupby(df["Region"])["Sales"].sum()
ax[1,1].pie(Region_Sales.values,labels=Region_Sales.index,autopct="%1.1f%%",colors=["Pink","Blue","Red","Orange"])
ax[1,1].set_title("Percentage Of Sales From Each Region")

# Horizontal Bar Chart Of Sub-Category Comparison
SubCat_Sales=df.groupby(df["Sub-Category"])["Sales"].sum()
ax[2,0].barh(SubCat_Sales.index,SubCat_Sales.values,color="Maroon")
ax[2,0].set_title("Horizontal Bar Chart Of Sub-Category")
ax[2,0].set_xlabel("Sales")
ax[2,0].set_ylabel("Values")
ax[2,0].tick_params(axis='y', labelsize=7)

# Scatter Plot To find the Relationship between Discount & Profit  
ax[2,1].scatter(df["Discount"],df["Profit"],marker="*",color="Green",)
ax[2,1].grid(True)
ax[2,1].set_title("Scatter Plot Of Discount & Profit")
ax[2,1].set_xlabel("Discount")
ax[2,1].set_ylabel("Profit")

plt.tight_layout()
fig.suptitle("Superstore Data Visualization", fontsize=16)
plt.subplots_adjust(top=0.90, hspace=0.5)  
plt.savefig('Superstore_Visualization.png', dpi=150, bbox_inches='tight')
plt.show()