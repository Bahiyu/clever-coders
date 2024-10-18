import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
import xgboost as xgb

# Load the enhanced dataset
data_path = "C:\\Users\\patle\\pred\\enhanced_cleaned_file.csv"
df = pd.read_csv(data_path)

# Normalize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# # Convert categorical columns (state and district) into categorical data types
# df['state_name'] = df['state_name'].astype('category')
# df['dist_name'] = df['dist_name'].astype('category')

crop_column_map = {
    'rice': 'rice_harvest_price_(rs_per_quintal)',
    'paddy': 'paddy_harvest_price_(rs_per_quintal)',
    'wheat': 'wheat_harvest_price_(rs_per_quintal)',
    'sorghum': 'sorghum_harvest_price_(rs_per_quintal)',
    'sugarcane': 'sugarcane_gur_harvest_price_(rs_per_quintal)'
}

numeric_columns = list(crop_column_map.values())

additional_features = ['rainfall_mm', 'avg_temperature_c', 'humidity_percent', 
                       'area_ha', 'yield_quintal_per_ha',
                       'stock_rice_quintal', 'stock_wheat_quintal', 
                       'stock_sorghum_quintal', 'stock_sugarcane_quintal']
df[numeric_columns + additional_features] = df[numeric_columns + additional_features].replace(-1, np.nan)
df.dropna(inplace=True)

df['area_yield_interaction'] = df['area_ha'] * df['yield_quintal_per_ha']

for feature in additional_features[:3]:  # Applying only to weather features (rainfall, temperature, humidity)
    df[f'{feature}_rolling_avg'] = df.groupby('dist_name')[feature].transform(lambda x: x.rolling(window=2).mean())

df.dropna(inplace=True)    

# Convert categorical columns (state and district) into categorical data types
df['state_name'] = df['state_name'].astype('category')
df['dist_name'] = df['dist_name'].astype('category')

# One-hot encode categorical columns
df = pd.get_dummies(df, columns=['state_name', 'dist_name'], drop_first=True)

# List of crop columns and additional features (for feature engineering)
# crop_column_map = {
#     'rice': 'rice_harvest_price_(rs_per_quintal)',
#     'paddy': 'paddy_harvest_price_(rs_per_quintal)',
#     'wheat': 'wheat_harvest_price_(rs_per_quintal)',
#     'sorghum': 'sorghum_harvest_price_(rs_per_quintal)',
#     'sugarcane': 'sugarcane_gur_harvest_price_(rs_per_quintal)'
# }


# Replace negative values (-1) with NaN and drop NaNs
# numeric_columns = list(crop_column_map.values())
# additional_features = ['rainfall_mm', 'avg_temperature_c', 'humidity_percent', 
#                        'area_ha', 'yield_quintal_per_ha',
#                        'stock_rice_quintal', 'stock_wheat_quintal', 
#                        'stock_sorghum_quintal', 'stock_sugarcane_quintal']
# df[numeric_columns + additional_features] = df[numeric_columns + additional_features].replace(-1, np.nan)
# df.dropna(inplace=True)

# Feature Engineering Step 1: Interaction Features (e.g., area * yield)
# df['area_yield_interaction'] = df['area_ha'] * df['yield_quintal_per_ha']

# Feature Engineering Step 2: Rolling Averages for weather data (3-year rolling average)
# for feature in additional_features[:3]:  # Applying only to weather features (rainfall, temperature, humidity)
#     df[f'{feature}_rolling_avg'] = df.groupby('dist_name')[feature].transform(lambda x: x.rolling(window=3).mean())

# Drop rows with NaNs generated by rolling averages and interaction terms
# df.dropna(inplace=True)


# Function to predict prices for a specific crop and future year
def predict_crop_price_for_year(crop_name, future_year):
    if crop_name not in crop_column_map:
        print(f"Invalid crop name. Choose from: {list(crop_column_map.keys())}.")
        return

    target_column = crop_column_map[crop_name]
    
    # Separate features (X) and target variable (y)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train an XGBoost regressor model
    xg_reg = xgb.XGBRegressor(objective='reg:squarederror', 
                              colsample_bytree=0.3, 
                              learning_rate=0.1,
                              max_depth=5, 
                              alpha=10, 
                              n_estimators=100)

    xg_reg.fit(X_train, y_train)

    # Make predictions on the test set to evaluate model performance
    y_test_pred =xg_reg.predict(X_test)
    rmse = root_mean_squared_error(y_test, y_test_pred)
    print (f"RMSE for {crop_name.capitalize()} Price Prediction (using historical data): {rmse}\n")

    # Generate feature data for the future year
    future_data = X_train[X_train['year'] == X_train['year'].max()].copy()
    future_data['year'] = future_year

    # Make predictions for the future year
    future_pred = xg_reg.predict(future_data)
    print(f"Predicted Price for {crop_name.capitalize()} in the year {future_year}: {future_pred[0]}")


# Get user input for crop name and year
crop_name_input = input(f"Enter the crop name ({', '.join(crop_column_map.keys())}): ").strip().lower()
year_input = int(input("Enter the year for prediction (e.g., 2025): "))

# Call the prediction function with user input
predict_crop_price_for_year(crop_name_input, year_input)





