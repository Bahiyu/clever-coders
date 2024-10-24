import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import matplotlib.pyplot as plt

# Load the dataset
data_path = "C:\\Users\\patle\\Downloads\\merged_dataset.csv"
df = pd.read_csv(data_path)

# Normalize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Replace negative values (-1) with NaN and drop NaNs
numeric_columns = ['rice_harvest_price_(rs_per_quintal)']
df[numeric_columns] = df[numeric_columns].replace(-1, np.nan)
df.dropna(inplace=True)

# Interaction Feature
df['area_yield_interaction'] = df['rice_area_(1000_ha)'] * df['rice_yield_(kg_per_ha)']

# Convert categorical columns into categorical data types
df['state_name'] = df['state_name'].astype('category')
df['dist_name'] = df['dist_name'].astype('category')
df['year'] = df['year'].astype('category')

# One-hot encoding of categorical columns
df = pd.get_dummies(df, columns=['state_name', 'dist_name', 'year'], drop_first=True)

def predict_rice_price_for_state(state_name, future_years):
    # Normalize the state_name input (convert to lower and replace spaces)
    normalized_state_name = state_name.lower().replace(' ', '_')

    # Find the correct column name for the state
    state_columns = [col for col in df.columns if col.startswith('state_name_') and normalized_state_name in col.lower()]

    if not state_columns:
        print(f"Error: State '{state_name}' not found in the dataset.")
        print("Available states:")
        available_states = [col.replace('state_name_', '').replace('_', ' ').title() for col in df.columns if col.startswith('state_name_')]
        for state in available_states:
            print(f"- {state}")
        return

    state_column = state_columns[0]
    print(f"Using column: {state_column}")

    # Filter dataset for the selected state
    filtered_df = df[df[state_column] == 1]

    if filtered_df.empty:
        print(f"No data available for state: {state_name}")
        return

    target_column = 'rice_harvest_price_(rs_per_quintal)'

    # Separate features (X) and target variable (y)
    X = filtered_df.drop(columns=[target_column])
    y = filtered_df[target_column]

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
    print(f"RMSE for Rice Price Prediction (using historical data): {rmse}\n")

    # Initialize list to store predictions for future years
    future_prices = []

    # Get the most recent year in the dataset
    year_columns = [col for col in X.columns if col.startswith('year_')]
    if not year_columns:
        print("Error: No year columns found in the dataset.")
        return
    most_recent_year = int(max(col.split('_')[-1] for col in year_columns))

    # Generate predictions for each future year
    for year in future_years:
        future_data = X_train.iloc[-1:].copy()  # Use the last row as a template
        
        # Set all year columns to 0
        future_data[year_columns] = 0
        
        # Set the correct year column to 1, or use the most recent year if the future year is not in the dataset
        year_column = f'year_{year}' if f'year_{year}' in future_data.columns else f'year_{most_recent_year}'
        if year_column not in future_data.columns:
            print(f"Warning: Year {year} not found in the dataset. Using the most recent year ({most_recent_year}).")
        future_data[year_column] = 1
        
        # Modify features for the future year dynamically
        years_difference = year - most_recent_year
        growth_factor_area = 1 + np.random.uniform(0.005, 0.015) * years_difference  # Random growth factor for area
        growth_factor_yield = 1 + np.random.uniform(0.01, 0.03) * years_difference  # Random growth factor for yield

        future_data['rice_area_(1000_ha)'] *= growth_factor_area  # Simulate growth in area
        future_data['rice_yield_(kg_per_ha)'] *= growth_factor_yield  # Simulate growth in yield

        # Interaction term with random variation
        future_data['area_yield_interaction'] = future_data['rice_area_(1000_ha)'] * future_data['rice_yield_(kg_per_ha)']
        
        # Add some more random variation to area and yield
        future_data['rice_area_(1000_ha)'] += np.random.normal(0, future_data['rice_area_(1000_ha)'].values[0] * 0.05)
        future_data['rice_yield_(kg_per_ha)'] += np.random.normal(0, future_data['rice_yield_(kg_per_ha)'].values[0] * 0.05)
        
        # Predict future prices
        future_pred = xg_reg.predict(future_data)
        future_prices.append(future_pred[0])
        
        # Print predicted price for each future year
        print(f"Predicted Price for Rice in the year {year}: {future_pred[0]:.2f}")

    # Plot future price predictions using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(future_years, future_prices, color='blue')
    plt.xlabel('Year')
    plt.ylabel('Predicted Price (Rs per Quintal)')
    plt.title(f'Predicted Rice Prices for Future Years in {state_name}')
    plt.xticks(future_years)
    plt.show()

# Get user input for state name and list of future years
state_name_input = input(f"Enter the state name for price prediction: ").strip()
years_input = input("Enter the years for prediction (comma-separated, e.g., 2025, 2026, 2027): ")
future_years_input = list(map(int, years_input.split(',')))

# Call the prediction function with user input
predict_rice_price_for_state(state_name_input, future_years_input)
