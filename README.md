# ApexPlanet Task 1 — Data Immersion & Wrangling

## Project Overview

This project is part of the **ApexPlanet 60-Day Data Analytics Internship**.

The objective of this task is to understand the provided dataset, identify data quality issues, clean and transform the data, and prepare a final analysis-ready dataset.

The project focuses on:

- Data inspection and profiling
- Data dictionary preparation
- Missing value identification and handling
- Duplicate record detection
- Data type validation
- Date standardization
- Numeric data validation
- Sales calculation validation
- Outlier identification
- Data cleaning and transformation
- Final dataset validation
- Creation of an analysis-ready dataset

---

## Dataset Overview

The dataset contains **1,000 records and 12 columns** related to customer orders and sales transactions.

The dataset provides information about customers, orders, products, categories, quantities, unit prices, and total sales.

### Dataset Columns

- `Order_ID`
- `Order_Date`
- `Customer_ID`
- `Customer_Name`
- `Age`
- `Gender`
- `City`
- `Product`
- `Category`
- `Quantity`
- `Unit_Price`
- `Total_Sales`

---

## Project Structure

```text
ApexPlanet_Task_1/
│
├── ApexPlanet_DataAnalytics_Dataset.xlsx
├── ApexPlanet_Data_Dictionary.xlsx
├── ApexPlanet_Cleaned_Dataset.xlsx
│
├── data_inspection.py
├── data_clean.py
├── final_verification.py
│
└── README.md
