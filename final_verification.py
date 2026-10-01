import pandas as pd

# Load cleaned dataset
cleaned_data = pd.read_excel(
    "../Output/ApexPlanet_Cleaned_Dataset.xlsx"
)

print("\n========== FINAL SAVED DATASET VERIFICATION ==========")

print("\nDataset Shape:")
print(cleaned_data.shape)

print("\nMissing Values:")
print(cleaned_data.isnull().sum())

print("\nDuplicate Rows:")
print(cleaned_data.duplicated().sum())

print("\nColumn Names:")
print(cleaned_data.columns.tolist())

print("\nData Types:")
print(cleaned_data.dtypes)