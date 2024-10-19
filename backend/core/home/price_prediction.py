import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import matplotlib.pyplot as plt

# Load the dataset
data_path = "C:\\Users\\Vansh Jain\\clever-coders\\backend\\core\\home\\enhanced_cleaned_file.csv"
df = pd.read_csv(data_path)

# Normalize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

crop_column_map = {
    'rice': 'rice_harvest_price_(rs_per_quintal)',
    'paddy': 'paddy_harvest_price_(rs_per_quintal)',
    'wheat': 'wheat_harvest_price_(rs_per_quintal)',
    'sorghum': 'sorghum_harvest_price_(rs_per_quintal)',
    'sugarcane': 'sugarcane_gur_harvest_price_(rs_per_quintal)'
}

# Replace negative values (-1) with NaN and drop NaNs
numeric_columns = list(crop_column_map.values())
additional_features = ['rainfall_mm', 'avg_temperature_c', 'humidity_percent', 
                       'area_ha', 'yield_quintal_per_ha',
                       'stock_rice_quintal', 'stock_wheat_quintal', 
                       'stock_sorghum_quintal', 'stock_sugarcane_quintal']
df[numeric_columns + additional_features] = df[numeric_columns + additional_features].replace(-1, np.nan)
df.dropna(inplace=True)

# Interaction Feature
df['area_yield_interaction'] = df['area_ha'] * df['yield_quintal_per_ha']

# Create rolling averages for weather-related features
for feature in ['rainfall_mm', 'avg_temperature_c', 'humidity_percent']:
    df[f'{feature}_rolling_avg'] = df.groupby('dist_name')[feature].transform(lambda x: x.rolling(window=2).mean())

# Drop rows with NaN values generated from rolling averages
df.dropna(inplace=True)


### Feature Engineering for Future Predictions
# 1. Lag Features (Lag 1 year for price and weather data)
df['lagged_rainfall'] = df.groupby('dist_name')['rainfall_mm'].shift(1)
df['lagged_price'] = df.groupby('dist_name')[crop_column_map['rice']].shift(1)  # Using rice as an example

# 2. Trend Features (Difference between current and lagged values)
df['rainfall_trend'] = df['rainfall_mm'] - df['lagged_rainfall']
df['price_trend'] = df[crop_column_map['rice']] - df['lagged_price']

# Drop rows with missing values after creating lag features
df.dropna(inplace=True)

# Convert categorical columns into categorical data types
df['state_name'] = df['state_name'].astype('category')
df['dist_name'] = df['dist_name'].astype('category')

# One-hot encoding of categorical columns
df = pd.get_dummies(df, columns=['state_name', 'dist_name'], drop_first=True)

# Define the function to predict crop prices for specific years with visualization
def predict_crop_price_for_year(crop_name, future_years):
    if crop_name not in crop_column_map:
        print(f"Invalid crop name. Choose from: {list(crop_column_map.keys())}.")
        return

    target_column = crop_column_map[crop_name]
    
    # Separate features (X) and target variable (y)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the XGBoost regressor model
    xg_reg = xgb.XGBRegressor(objective='reg:squarederror', 
                              colsample_bytree=0.3, 
                              learning_rate=0.1,
                              max_depth=3, 
                              alpha=10, 
                              n_estimators=150)

    xg_reg.fit(X_train, y_train)

    # Evaluate model performance
    y_test_pred = xg_reg.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
    print(f"RMSE for {crop_name.capitalize()} Price Prediction (using historical data): {rmse}\n")

    # Initialize list to store predictions for future years
    future_prices = []

    # Generate predictions for each future year
    for year in future_years:
        future_data = X_train[X_train['year'] == X_train['year'].max()].copy()
        future_data['year'] = year
        
        # Modify some features for the future (optional, like weather changes)
        future_data['rainfall_mm'] += np.random.normal(0, 5)  # Example: vary rainfall
        future_data['avg_temperature_c'] += np.random.normal(0, 2)  # Example: vary temperature
        
        # Predict future prices
        future_pred = xg_reg.predict(future_data)
        future_prices.append(future_pred[0])
        
        # Print predicted price for each future year
        print(f"Predicted Price for {crop_name.capitalize()} in the year {year}: {future_pred[0]}")
        future_prices_with_year = [(year, future_pred[0]) for year in future_years]
        return future_prices_with_year

    # Plot future price predictions using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(future_years, future_prices, color='blue')
    plt.xlabel('Year')
    plt.ylabel('Predicted Price (Rs per Quintal)')
    plt.title(f'Predicted {crop_name.capitalize()} Prices for Future Years')
    plt.xticks(future_years)  # Ensures correct labeling
    plt.show()

# Get user input for crop name and list of future years
# crop_name_input = input(f"Enter the crop name ({', '.join(crop_column_map.keys())}): ").strip().lower()
# years_input = input("Enter the years for prediction (comma-separated, e.g., 2025, 2026, 2027): ")
# future_years_input = list(map(int, years_input.split(',')))

# Call the prediction function with user input
# predict_crop_price_for_year(crop_name_input, future_years_input)