import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
import xgboost as xgb
import matplotlib.pyplot as plt

# Load the dataset
data_path = "C:\\Users\\patle\\Downloads\\merged_dataset.csv"
df = pd.read_csv(data_path)
# "C:\\Users\\patle\\Downloads\\merged_dataset.csv"
print(df.columns)
