import pandas as pd
import numpy as np


file_path = r"C:\Users\patle\Downloads\ICRISAT_Enhanced_Dataset_with_Weather_Production_Inventory.csv"
data = pd.read_csv(file_path)


print("Initial Data Info:")
data.info()
print("\nFirst few rows of data:")
print(data.head())


data.columns = data.columns.str.lower().str.replace(' ', '_')


numeric_columns = ['rice_harvest_price_(rs_per_quintal)', 
                   'paddy_harvest_price_(rs_per_quintal)', 
                   'wheat_harvest_price_(rs_per_quintal)', 
                   'sorghum_harvest_price_(rs_per_quintal)', 
                   'sugarcane_gur_harvest_price_(rs_per_quintal)']


data[numeric_columns] = data[numeric_columns].replace(-1, np.nan)


print("\nData Info after Cleaning:")
data.info()
print("\nFirst few rows of cleaned d5ata:")
print(data.head())


data.to_csv('enhanced_cleaned_file.csv', index=False)
print("\nCleaned data saved to 'enhanced_cleaned_file.csv'")
