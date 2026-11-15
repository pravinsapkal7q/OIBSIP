# 📊 Customer Segmentation Analysis - Summary & Business Insights

## 📌 Project Overview
This project focuses on segmenting retail customers based on their purchasing behavior (**Total Amount Spent** and **Total Quantity Purchased**) using **K-Means Clustering**. By identifying distinct customer groups, businesses can optimize marketing strategies, improve customer retention, and maximize revenue.

---

## 🔍 Customer Cluster Breakdown ($k=4$)

Based on the K-Means clustering model, the customer base (1,000 total customers) has been segmented into **4 distinct personas**:

| Cluster ID | Segment Name | Customer Count | Avg. Total Spent | Avg. Quantity | Key Behavioral Characteristics |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Cluster 3** | **VIP / High-Value Spenders** | 153 | ₹1,554.25 | 3.67 | Highest revenue generators; purchase premium items in high quantities. |
| **Cluster 0** | **Loyal / Mid-Tier Customers** | 146 | ₹861.64 | 2.42 | Consistent spenders with strong purchasing power and moderate basket sizes. |
| **Cluster 2** | **Budget / Bulk Shoppers** | 289 | ₹126.45 | 3.55 | High purchase volume with low overall spend; highly price-sensitive and discount-driven. |
| **Cluster 1** | **Occasional / Low-Value Shoppers** | 412 | ₹135.57 | 1.39 | Largest customer group; infrequent buyers with small basket sizes and low total spend. |

---

## 💡 Strategic Recommendations

1. **Retain & Reward VIPs (Cluster 3):** 
   - Introduce exclusive loyalty tiers, early access to new collections, and personalized VIP concierge offers to maintain high retention.
2. **Upsell to Loyal Customers (Cluster 0):** 
   - Use targeted product recommendations and bundled offers to transition these steady buyers into the VIP segment.
3. **Volume Promotions for Budget Shoppers (Cluster 2):** 
   - Target with *"Buy More, Save More"* campaigns, combo deals, and seasonal clearance sales to increase their average order value.
4. **Re-engage Occasional Buyers (Cluster 1):** 
   - Deploy automated win-back email campaigns, first-repeat-purchase coupons, and personalized reminders to boost purchase frequency.

---

## 🛠️ Tech Stack Used
- **Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn (StandardScaler, K-Means Clustering)