import pandas as pd


# ==================================================
# 1. LOAD RAW DATASET
# ==================================================

data = pd.read_excel(
    "../Dataset/ApexPlanet_DataAnalytics_Dataset.xlsx"
)


# ==================================================
# 2. HANDLE MISSING AGE
#    Gender-wise median imputation
# ==================================================

male_median_age = data.loc[
    data["Gender"] == "Male",
    "Age"
].median()

female_median_age = data.loc[
    data["Gender"] == "Female",
    "Age"
].median()

data.loc[
    (data["Gender"] == "Male") & (data["Age"].isnull()),
    "Age"
] = male_median_age

data.loc[
    (data["Gender"] == "Female") & (data["Age"].isnull()),
    "Age"
] = female_median_age


# ==================================================
# 3. HANDLE MISSING CITY
# ==================================================

data["City"] = data["City"].fillna("Unknown")


# ==================================================
# 4. CONVERT ORDER_DATE TO DATETIME
# ==================================================

data["Order_Date"] = pd.to_datetime(
    data["Order_Date"],
    errors="coerce"
)


# ==================================================
# 5. VALIDATE NUMERIC COLUMNS
# ==================================================

numeric_columns = [
    "Age",
    "Quantity",
    "Unit_Price",
    "Total_Sales"
]

print("\nNumeric Data Types:")
print(data[numeric_columns].dtypes)

print("\nNegative Values Check:")

for column in numeric_columns:
    negative_count = (data[column] < 0).sum()
    print(f"{column}: {negative_count}")


# ==================================================
# 6. VALIDATE TOTAL SALES CALCULATION
# ==================================================

data["Calculated_Sales"] = (
    data["Quantity"] * data["Unit_Price"]
)

data["Sales_Difference"] = (
    data["Total_Sales"] - data["Calculated_Sales"]
)

sales_errors = (
    data["Sales_Difference"].abs() > 0.01
).sum()

print("\nSales Calculation Errors:")
print(sales_errors)


# ==================================================
# 7. REMOVE TEMPORARY VALIDATION COLUMNS
# ==================================================

data.drop(
    columns=[
        "Calculated_Sales",
        "Sales_Difference"
    ],
    inplace=True
)


# ==================================================
# 8. FINAL VALIDATION BEFORE SAVING
# ==================================================

print("\n========== BEFORE SAVING ==========")

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDuplicate Rows:")
print(data.duplicated().sum())

print("\nDataset Shape:")
print(data.shape)


# ==================================================
# 9. SAVE CLEANED DATASET
# ==================================================

output_path = "../Output/ApexPlanet_Cleaned_Dataset.xlsx"

data.to_excel(
    output_path,
    index=False
)

print("\nCleaned dataset saved successfully!")
print("File:", output_path)