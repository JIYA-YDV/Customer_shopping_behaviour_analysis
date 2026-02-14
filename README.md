Customer Shopping Behavior Analysis

A comprehensive data analytics project analyzing 3,900 customer transactions to uncover spending patterns, customer segments, and actionable business insights.

📋 Project Overview
This project analyzes customer shopping behavior using transactional data from 3,900 purchases across various product categories. The analysis spans the complete data pipeline—from data cleaning and transformation in Python, through structured business analysis in SQL, to interactive visualization in Power BI.
Key Business Question: How can the company leverage consumer shopping data to identify trends, improve customer engagement, and optimize marketing and product strategies?

📊 Dataset Summary

| Attribute          | Details                      |
| ------------------ | ---------------------------- |
| **Total Records**  | 3,900 transactions           |
| **Features**       | 18 columns                   |
| **Missing Values** | 37 values in `Review Rating` |

Features Include:
Demographics: Age, Gender, Location
Purchase Details: Item Purchased, Category, Purchase Amount, Season, Size, Color
Behavioral Metrics: Discount Applied, Previous Purchases, Frequency of Purchases, Review Rating, Shipping Type
Subscription Data: Subscription Status, Payment Method

🛠️ Tech Stack

| Component           | Technology              | Purpose                                       |
| ------------------- | ----------------------- | --------------------------------------------- |
| **Data Processing** | Python (Pandas, NumPy)  | Cleaning, transformation, feature engineering |
| **Database**        | PostgreSQL + SQLAlchemy | Structured storage & complex queries          |
| **Visualization**   | Power BI                | Interactive dashboards & reporting            |
| **Version Control** | Git/GitHub              | Project documentation & collaboration         |

🔧 Data Pipeline
1. Data Preparation & Modeling (Python)
The Python script handles comprehensive data preprocessing:
# Key transformations performed:
✓ Missing value imputation using category-wise median for Review Rating
✓ Column standardization (snake_case conversion)
✓ Feature engineering: age_group bins, purchase_frequency_days mapping
✓ Data consistency verification (discount_applied vs promo_code_used)
✓ PostgreSQL database loading via SQLAlchemy

Engineered Features:
age_group: Categorical bins (Young Adult, Adult, Middle-aged, Senior)
purchase_frequency_days: Numeric conversion from text frequencies
Removed redundant promo_code_used column (100% correlated with discount_applied)

2. Data Analysis (SQL)
Structured PostgreSQL queries addressing 10+ business questions:

| Analysis                         | Business Insight                                              |
| -------------------------------- | ------------------------------------------------------------- |
| **Revenue by Gender**            | Compare male vs. female spending patterns                     |
| **High-Spending Discount Users** | Identify customers using discounts but spending above average |
| **Top Products by Rating**       | Find highest-rated products for quality positioning           |
| **Shipping Preferences**         | Standard vs. Express shipping spend comparison                |
| **Subscriber Analysis**          | Subscription status impact on revenue                         |
| **Customer Segmentation**        | New/Returning/Loyal customer classification                   |
| **Discount Dependency**          | Products most reliant on promotional pricing                  |
| **Repeat Buyer Behavior**        | Correlation between purchase frequency & subscription         |

3. Visualization & Insights (Power BI)
Interactive dashboard featuring:
KPI Cards: Total Revenue, Average Purchase, Customer Count
Demographic Breakdowns: Age group & gender distributions
Product Performance: Category-wise sales & ratings
Behavioral Trends: Discount impact, shipping preferences, subscription rates
Geographic Insights: Location-based purchasing patterns

Built with Python, PostgreSQL, and Power BI
