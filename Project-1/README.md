# Brazilian E-Commerce Analysis (Olist Dataset)

## Overview

This project presents an end-to-end Exploratory Data Analysis (EDA) of the Brazilian E-Commerce Public Dataset by Olist. The objective is to understand customer behavior, sales performance, product trends, delivery operations, and overall business performance through data-driven analysis.

The project follows a structured analytics workflow consisting of:

1. Data Understanding
2. Data Quality Assessment
3. Data Preparation & Feature Engineering
4. Exploratory Data Analysis (EDA)
5. Statistical Analysis
6. Business Insights & Recommendations

---

## Dataset

Dataset Used:

- Brazilian E-Commerce Public Dataset by Olist

The dataset contains information about:

- Orders
- Customers
- Products
- Sellers
- Payments
- Reviews
- Geolocation

The data represents real e-commerce transactions made in Brazil.

---

## Project Objectives

The primary objectives of this analysis are:

- Understand customer purchasing behavior.
- Analyze revenue trends and sales performance.
- Evaluate product and seller performance.
- Study delivery efficiency and customer satisfaction.
- Identify geographic sales patterns.
- Detect outliers and statistical relationships within the data.
- Generate actionable business insights.

---

## Data Processing Workflow

### 1. Data Understanding

- Studied all available tables.
- Identified primary and foreign keys.
- Understood relationships between datasets.
- Mapped the overall data model.

### 2. Data Quality Assessment

- Missing value analysis.
- Duplicate record detection.
- Data type verification.
- Consistency checks.
- Data completeness assessment.

### 3. Data Preparation

Created analytical datasets at different levels of granularity:

#### Order-Level Dataset

One row represents one order.

Features engineered:

- Revenue
- Delivery Time
- Delivery Delay
- Product Volume
- Product Weight
- Number of Unique Products
- Number of Unique Sellers
- Number of Unique Categories

#### Item-Level Dataset

One row represents one product item within an order.

Used for:

- Product Analysis
- Category Analysis
- Seller Analysis

### Feature Engineering

Created additional business metrics such as:

- Revenue
- Product Volume
- Delivery Time
- Delivery Delay

---

## Exploratory Data Analysis

The analysis focused on:

### Revenue Analysis

- Revenue distribution
- Revenue trends
- High-value orders

### Customer Analysis

- Customer distribution
- Customer purchasing behavior
- Geographic customer patterns

### Product Analysis

- Top-performing categories
- Product characteristics
- Product popularity

### Seller Analysis

- Seller contribution
- Seller distribution

### Delivery Analysis

- Delivery times
- Delivery delays
- Operational performance

### Review Analysis

- Review score distribution
- Relationship between delivery performance and customer satisfaction

---

## Statistical Analysis

Performed:

### Distribution Analysis

- Revenue
- Delivery metrics
- Product attributes

### Outlier Detection

Used the IQR (Interquartile Range) method to identify extreme observations.

### Correlation Analysis

Examined relationships between:

- Revenue
- Product characteristics
- Delivery metrics
- Review scores

### Trend Analysis

Analyzed temporal patterns using order purchase dates.

---

## Key Findings

- Revenue exhibits a highly right-skewed distribution.
- A small number of orders contribute disproportionately to total revenue.
- Product and seller performance is concentrated among a subset of categories and sellers.
- Delivery performance varies significantly across orders.
- Customer satisfaction is influenced by operational performance metrics.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Project Structure

```text
Brazilian-Ecommerce-EDA/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── ecommerce_eda.ipynb
│
├── README.md
```

---

## Limitations

The Olist dataset does not provide:

- Marketing campaign data
- Advertising spend
- Product cost information
- Profit margins

As a result:

- Profit cannot be calculated accurately.
- Customer Lifetime Value (CLV) can only be estimated.
- Marketing effectiveness analysis cannot be performed.

---

## Future Enhancements

Potential extensions include:

- Customer Segmentation
- Sales Forecasting
- Customer Retention Analysis
- Recommendation Systems
- Review Sentiment Analysis (NLP)
- Machine Learning Models

---

## Conclusion

This project demonstrates a complete Exploratory Data Analysis workflow on a real-world e-commerce dataset. The analysis provides insights into customer behavior, sales performance, delivery operations, and product trends while establishing a strong foundation for future machine learning and business intelligence applications.

---

## Author

**Shivansh Pandey**

Data Analytics & Machine Learning Enthusiast
