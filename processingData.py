from sklearn.preprocessing import MinMaxScaler
import pandas as pd
# Reinitialize the MinMaxScaler
scaler = MinMaxScaler()
data = pd.read_csv("TheDataWeCaveAbout.csv")
# Normalize all numeric columns
numeric_columns = data.select_dtypes(include=['number']).columns[1:]
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

# Save the normalized data to a new CSV file
output_path = 'normalizedData.csv'
data.to_csv(output_path, index=False)