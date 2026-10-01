import pandas as pd

# Load the dataset
data = pd.read_excel("../Dataset/ApexPlanet_DataAnalytics_Dataset.xlsx")

# Display first 5 rows
# print(data.head())

# Dataset shape
# print("Shape:", data.shape)

# Column names
# print("\nColumns:")
# print(data.columns)

# Data types
# print("\nData Types:")
# print(data.dtypes)

# Missing values
# print("\nMissing Values:")
# print(data.isnull().sum())

# Duplicate rows
# print("\nDuplicate Rows:")
# print(data.duplicated().sum())


# Unique values in categorical columns

# print("\nGender Unique Values:")
# print(data["Gender"].unique())

# print("\nCategory Unique Values:")
# print(data["Category"].unique())

# print("\nProduct Unique Values:")
# print(data["Product"].unique())

# print("\nCity Unique Values:")
# print(data["City"].unique())

# print("\nNumeric Summary:")
# print(data[["Age", "Quantity", "Unit_Price", "Total_Sales"]].describe())


# Check Total Sales calculation

# data["Calculated_Sales"] = data["Quantity"] * data["Unit_Price"]

# data["Sales_Difference"] = (
#     data["Total_Sales"] - data["Calculated_Sales"]
# )

# print("\nSales Calculation Check:")
# print(data["Sales_Difference"].describe())

# print("\nRows with Sales Difference:")
# print((data["Sales_Difference"].abs() > 0.01).sum())


# print("\nOrder Date Data Type:")
# print(data["Order_Date"].dtype)

# print("\nOrder Date Sample:")
# print(data["Order_Date"].head())

# print("\nDate Range:")
# print(data["Order_Date"].min())
# print(data["Order_Date"].max())


# Convert Order_Date temporarily for validation

# date_check = pd.to_datetime(data["Order_Date"], errors="coerce")

# print("\nInvalid Dates:")
# print(date_check.isnull().sum())

# print("\nEarliest Date:")
# print(date_check.min())

# print("\nLatest Date:")
# print(date_check.max())

# print("\nNumber of Dates in 2026:")
# print((date_check.dt.year == 2026).sum())


# Outlier Detection using IQR

# numeric_columns = ["Age", "Quantity", "Unit_Price", "Total_Sales"]

# for column in numeric_columns:
#     Q1 = data[column].quantile(0.25)
#     Q3 = data[column].quantile(0.75)

#     IQR = Q3 - Q1

#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR

#     outliers = data[
#         (data[column] < lower_bound) |
#         (data[column] > upper_bound)
#     ]

#     print(f"\n--- {column} ---")
#     print("Q1:", Q1)
#     print("Q3:", Q3)
#     print("IQR:", IQR)
#     print("Lower Bound:", lower_bound)
#     print("Upper Bound:", upper_bound)
#     print("Number of Outliers:", len(outliers))


# Inspect Total_Sales outliers

# Q1 = data["Total_Sales"].quantile(0.25)
# Q3 = data["Total_Sales"].quantile(0.75)

# IQR = Q3 - Q1

# upper_bound = Q3 + 1.5 * IQR

# sales_outliers = data[data["Total_Sales"] > upper_bound]

# print("\nTotal Sales Outlier Records:")
# print(
#     sales_outliers[
#         [
#             "Order_ID",
#             "Order_Date",
#             "Customer_ID",
#             "Product",
#             "Category",
#             "Quantity",
#             "Unit_Price",
#             "Total_Sales"
#         ]
#     ].to_string(index=False)
# )



# print("\nMissing Values in Sales Outliers:")
# print(sales_outliers[["Age", "City"]].isnull().sum())



# Inspect missing Age and City records

# print("\nRecords with Missing Age:")
# print(data[data["Age"].isnull()].to_string(index=False))

# print("\nRecords with Missing City:")
# print(data[data["City"].isnull()].to_string(index=False))



# # Count missing values by row

# missing_rows = data[data.isnull().any(axis=1)]

# print("\nRows containing missing values:")
# print(missing_rows.shape[0])

# print("\nMissing-value records:")
# print(
#     missing_rows[
#         [
#             "Order_ID",
#             "Age",
#             "City",
#             "Product",
#             "Category",
#             "Quantity",
#             "Unit_Price",
#             "Total_Sales"
#         ]
#     ].to_string(index=False)
# )


# print("\nOverall Age Median:")
# print(data["Age"].median())

# print("\nAge Median by Gender:")
# print(data.groupby("Gender")["Age"].median())

# print("\nAge Count by Gender:")
# print(data.groupby("Gender")["Age"].count())


# print("\nMissing Age by Gender:")
# print(data[data["Age"].isnull()]["Gender"].value_counts())

# Handle missing Age values using gender-wise median

# male_median_age = data.loc[data["Gender"] == "Male", "Age"].median()
# female_median_age = data.loc[data["Gender"] == "Female", "Age"].median()

# data.loc[
#     (data["Gender"] == "Male") & (data["Age"].isnull()),
#     "Age"
# ] = male_median_age

# data.loc[
#     (data["Gender"] == "Female") & (data["Age"].isnull()),
#     "Age"
# ] = female_median_age

# print("\nMissing Age after imputation:")
# print(data["Age"].isnull().sum())


# print("\nRecords with Missing Age after imputation:")
# print(data[(data["Gender"] == "Male") & (data["Age"].isnull())].shape[0])

# missing_city = data[data["City"].isnull()]

# print("\nMissing City by Gender:")
# print(missing_city["Gender"].value_counts())

# print("\nMissing City by Category:")
# print(missing_city["Category"].value_counts())

# print("\nMissing City by Product:")
# print(missing_city["Product"].value_counts())


# Handle missing City values

# data["City"] = data["City"].fillna("Unknown")

# print("\nMissing City after imputation:")
# print(data["City"].isnull().sum())

# print("\nCity values after cleaning:")
# print(data["City"].value_counts())


# print("\n========== FINAL DATA QUALITY CHECK ==========")

# # 1. Missing values
# print("\nMissing Values:")
# print(data.isnull().sum())

# # 2. Duplicate rows
# print("\nDuplicate Rows:")
# print(data.duplicated().sum())

# # 3. Age range
# print("\nAge Range:")
# print("Minimum Age:", data["Age"].min())
# print("Maximum Age:", data["Age"].max())

# # 4. Quantity range
# print("\nQuantity Range:")
# print("Minimum Quantity:", data["Quantity"].min())
# print("Maximum Quantity:", data["Quantity"].max())

# # 5. Negative values
# print("\nNegative Unit Price:")
# print((data["Unit_Price"] < 0).sum())

# print("\nNegative Total Sales:")
# print((data["Total_Sales"] < 0).sum())

# # 6. Date validation
# final_dates = pd.to_datetime(data["Order_Date"], errors="coerce")

# print("\nInvalid Dates:")
# print(final_dates.isnull().sum())

# # 7. Sales calculation validation
# data["Calculated_Sales"] = data["Quantity"] * data["Unit_Price"]

# data["Sales_Difference"] = (
#     data["Total_Sales"] - data["Calculated_Sales"]
# )

# print("\nSales Calculation Errors:")
# print((data["Sales_Difference"].abs() > 0.01).sum())


# print("\nCurrent Missing Values:")
# print(data[["Age", "City"]].isnull().sum())

# print("\nSample of Age and City:")
# print(data[["Order_ID", "Age", "Gender", "City"]].head(15))

