import pandas as pd

# Load the two datasets
file_path_price = "C:\\Users\\patle\\Downloads\\cleaned_datasetprice.csv"
file_path_main = "C:\\Users\\patle\\Downloads\\cleaned_dataset.csv"

df_price = pd.read_csv(file_path_price)
df_main = pd.read_csv(file_path_main)

# Merge the datasets on the common columns
df_merged = pd.merge(df_main, df_price, on=['dist_code', 'year', 'state_code', 'state_name', 'dist_name'])

# Clean up column names to ensure consistency
df_merged.columns = df_merged.columns.str.lower().str.replace(' ', '_')

# Replace negative values (-1) with NaN and drop NaNs
df_merged.replace(-1, pd.NA, inplace=True)
df_merged.dropna(inplace=True)

# Save the merged dataframe to a new CSV file
merged_file_path = 'C:/Users/patle/Downloads/merged_dataset.csv'
df_merged.to_csv(merged_file_path, index=False)

print(f'Merged dataset saved to: {merged_file_path}')

