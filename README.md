## End-to-End Customer Churn Analysis & Insights for Banking Sector (EDA + Power BI)

![Customer Churn Dashboard](https://github.com/Jyoti7890/Customer_Churn_Project/blob/main/Customer_Churn_dashboard.png)

## Project Overview

This is an **end-to-end data analytics project** that combines **Exploratory Data Analysis (EDA)** and **Power BI dashboarding** to analyze customer churn and extract actionable business insights.
This project focuses on **Customer Churn Analysis** using **Bank Customer Data**. The goal is to identify churn patterns, analyze customer behavior, and derive insights that help businesses reduce customer attrition.

An interactive **Power BI Dashboard** has been built using cleaned and transformed data through **Power Query**, along with **Exploratory Data Analysis (EDA)** performed in **Google Colab**.

---

##  Objectives

* Analyze customer churn behavior
* Identify key factors influencing churn
* Visualize churn trends across demographics and financial attributes
* Support data-driven decision-making

---

## Tools & Technologies Used

* **Power BI** – Dashboard creation & visualization
* **Power Query** – Data cleaning and transformation
* **Python (Google Colab)** – Exploratory Data Analysis (EDA)
* **Pandas, NumPy, Matplotlib, Seaborn** – Data analysis & visualization

---

##  Dataset Description

The dataset contains bank customer information including:

* Gender
* Age
* Country
* Credit Score
* Account Balance
* Products Used
* Credit Card Status
* Activity Status
* Churn Status

---

##  Data Processing Steps

### 1. Data Cleaning (Power Query)

* Removed null and duplicate values
* Renamed columns for clarity
* Converted data types
* Created calculated columns

### 2. Exploratory Data Analysis (EDA)

EDA was performed in **Google Colab** using Python libraries to understand churn patterns and feature relationships.

**EDA Visualizations Performed:**

* Customer Churn Distribution (Count Plot)
* Gender vs Churn
* Country vs Churn
* Activity Status vs Churn
* Number of Products vs Churn
* Age Distribution
* Credit Score Distribution
* Age vs Churn (Box Plot)
* Account Balance vs Churn (Box Plot)
* Correlation Heatmap of Numerical Features

**Libraries Used:**

* Pandas, NumPy
* Matplotlib
* Seaborn

---

## Dashboard Features

The Power BI dashboard includes interactive and insight-driven visuals:

* **Total Customers Overview (10K Customers)**
* **Overall Churn Rate (20.4%)**
* Customers by:

  * Gender
  * Activity Status
  * Credit Card Status
  * Country
  * Products Used
* Churn analysis by:

  * Age Groups
  * Credit Scores
  * Account Balance
* Interactive filters for **Churned / Not Churned Customers**

---

## 📊 Key Insights

* Higher churn observed in middle-aged customers
* Customers with lower credit scores show higher churn rates
* Inactive customers are more likely to churn
* Account balance significantly impacts churn behavior

---

##  How to Use the Dashboard

1. Open the **Power BI (.pbix)** file
2. Use slicers to filter churned vs non-churned customers
3. Interact with charts for deeper insights
4. Analyze trends across different customer segments

---

##  Project Structure

```
Customer-Churn-Analysis/
│
├── Customer Churn Dashboard.pbix   # Power BI dashboard file
├── Customer_churn_dashboard.pdf   # Dashboard export (PDF)
├── bank_churn.csv                  # Dataset used for analysis
├── customer_churn_eda.ipynb        # EDA performed in Google Colab
├── README.md                       # Project documentation

```

## Conclusion
This project demonstrates how **Power BI**, **Power Query**, and **EDA** can be effectively combined to analyze customer churn and extract meaningful business insights.

---

##  Author
**Jyoti**  
Data Analytics | Power BI | Python

---
 If you like this project, feel free to give it a star!

```


