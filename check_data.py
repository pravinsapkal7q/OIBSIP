
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Load and clean the dataset
# -----------------------------
df = pd.read_csv("retail-sales-dataset.csv")

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.drop_duplicates()

sns.set_theme(style="whitegrid")

print("DATASET OVERVIEW")
print("Shape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())

# -----------------------------
# 2. Descriptive statistics
# -----------------------------
numeric_cols = ["Age", "Quantity", "Price per Unit", "Total Amount"]

print("\nDESCRIPTIVE STATISTICS")
print(df[numeric_cols].describe())

print("\nMean:")
print(df[numeric_cols].mean())

print("\nMedian:")
print(df[numeric_cols].median())

print("\nMode:")
print(df[numeric_cols].mode().iloc[0])

print("\nStandard deviation:")
print(df[numeric_cols].std())

# -----------------------------
# 3. Monthly sales trend
# -----------------------------
df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Total Amount"].sum()
    .sort_index()
)

plt.figure(figsize=(12, 5))
monthly_sales.plot(marker="o")
plt.title("Monthly Retail Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png", dpi=150)
plt.show()

print("\nMonthly sales:")
print(monthly_sales)

# -----------------------------
# 4. Quarterly sales trend
# -----------------------------
df["Quarter"] = df["Date"].dt.to_period("Q")

quarterly_sales = (
    df.groupby("Quarter")["Total Amount"].sum()
    .sort_index()
)

plt.figure(figsize=(9, 5))
quarterly_sales.plot(kind="line", marker="o")
plt.title("Quarterly Retail Sales Trend")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("quarterly_sales.png", dpi=150)
plt.show()

print("\nQuarterly sales:")
print(quarterly_sales)

# -----------------------------
# 5. Customer demographics
# -----------------------------
df["Age Group"] = pd.cut(
    df["Age"],
    bins=[0, 19, 29, 39, 49, 59, 100],
    labels=["Under 20", "20-29", "30-39",
            "40-49", "50-59", "60+"]
)

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Age Group")
plt.title("Customers by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig("age_group.png", dpi=150)
plt.show()

plt.figure(figsize=(6, 5))
sns.countplot(data=df, x="Gender")
plt.title("Transactions by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig("gender_analysis.png", dpi=150)
plt.show()

# -----------------------------
# 6. Product category analysis
# -----------------------------
top_products = (
    df.groupby("Product Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

category_revenue = (
    df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQUANTITY SOLD BY CATEGORY")
print(top_products)

print("\nREVENUE BY CATEGORY")
print(category_revenue)

plt.figure(figsize=(9, 5))
category_revenue.plot(kind="bar")
plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("category_revenue.png", dpi=150)
plt.show()

# -----------------------------
# 7. Correlation heatmap
# -----------------------------
plt.figure(figsize=(8, 6))
correlation = df[numeric_cols].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Numerical Variables")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150)
plt.show()

# -----------------------------
# 8. Additional insight
# -----------------------------
gender_revenue = (
    df.groupby("Gender")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(7, 5))
gender_revenue.plot(kind="bar")
plt.title("Revenue by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("gender_revenue.png", dpi=150)
plt.show()

print("\nREVENUE BY GENDER")
print(gender_revenue)

# -----------------------------
# 9. Business summary
# -----------------------------
print("\nBUSINESS SUMMARY")
print("Total revenue:", df["Total Amount"].sum())
print("Total transactions:", df["Transaction ID"].nunique())
print("Average transaction amount:", df["Total Amount"].mean())
print("Highest revenue category:", category_revenue.idxmax())
print("Highest quantity category:", top_products.idxmax())

print("\nEDA completed successfully!")
