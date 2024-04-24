# %% [markdown]
# ### 6COM2007 - Programming and Testing the Intelligent Adaptive System
# - Marcelo Hernandez
# - UH Student ID: 23033126
# - April 25, 2024
# 
# #### Exploratory Data Analysis

# %%
# Libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# Load the data into pandas dataframes 
training_data_path = '../IAS_DATA/6com2007-3.csv'
windows_open_data_path = '../IAS_DATA/windows_open.csv'
new_day_data_path = '../IAS_DATA/New_day.csv'

training_data = pd.read_csv(training_data_path)
windows_open_data = pd.read_csv(windows_open_data_path)
new_day_data = pd.read_csv(new_day_data_path)

# %%
# Convert 'Date' values in format 'dd/mm/yy' to 'dd/mm/yyyy' for consistency across datasets
def convert_dates(date_series):
    date_parts = date_series.str.split('/', expand=True)
    date_parts[2] = date_parts[2].apply(lambda x: '20' + x if len(x) == 2 else x)
    return date_parts[0] + '/' + date_parts[1] + '/' + date_parts[2]

# Apply the conversion
training_data['Date'] = convert_dates(training_data['Date'])
windows_open_data['Date'] = convert_dates(windows_open_data['Date'])
new_day_data['Date'] = convert_dates(new_day_data['Date'])

# Parse the 'Datetime' columns
training_data['Datetime'] = pd.to_datetime(training_data['Date'] + ' ' + training_data['Time'], format='%d/%m/%Y %H:%M')
windows_open_data['Datetime'] = pd.to_datetime(windows_open_data['Date'] + ' ' + windows_open_data['Time'], format='%d/%m/%Y %H:%M:%S')  
new_day_data['Datetime'] = pd.to_datetime(new_day_data['Date'] + ' ' + new_day_data['Time'], format='%d/%m/%Y %H:%M')

# Sort the data by 'Datetime' column
training_data_sorted = training_data.sort_values('Datetime')
windows_open_data_sorted = windows_open_data.sort_values('Datetime')
new_day_data_sorted = new_day_data.sort_values('Datetime')

# %%
# Perform an initial missing data check
print("\nMissing training_data_cleaned check:")
print(training_data_sorted.isnull().sum())

print("\nMissing windows_open data check:")
print(windows_open_data_sorted.isnull().sum())

print("\nMissing new_day data check:")
print(new_day_data_sorted.isnull().sum())

# %%
# training_data_sorted: interpolate missing values for 'Satisfaction' (5x) and 'Outside temp' (2x)
training_data_sorted['Satisfaction'] = training_data_sorted['Satisfaction'].fillna(training_data_sorted['Satisfaction'].interpolate(method='linear'))
training_data_sorted['Outside temp'] = training_data_sorted['Outside temp'].fillna(training_data_sorted['Outside temp'].interpolate(method='linear'))

# windows_open_data_sorted is good to go

# new_day_data_sorted: interpolate missing value for 'Outside temp' (1x)
new_day_data_sorted['outside temp'] = new_day_data_sorted['outside temp'].fillna(new_day_data_sorted['outside temp'].interpolate(method='linear'))

# %%
# Perform a new missing data check post interpolation
print("\nMissing training_data_cleaned check:")
print(training_data_sorted.isnull().sum())

print("\nMissing windows_open data check:")
print(windows_open_data_sorted.isnull().sum())

print("\nMissing new_day data check:")
print(new_day_data_sorted.isnull().sum())

# %%
# Save the cleaned windows open and new day data to new csv files
cleaned_training_data_path = '../IAS_DATA/6com2007-3_cleaned.csv'
cleaned_windows_open_data_path = '../IAS_DATA/windows_open_cleaned.csv'
cleaned_new_day_data_path = '../IAS_DATA/New_day_cleaned.csv'

# Save as excel, sortable tables with column names
training_data_sorted.to_csv(cleaned_training_data_path, index=False)
windows_open_data_sorted.to_csv(cleaned_windows_open_data_path, index=False)
new_day_data_sorted.to_csv(cleaned_new_day_data_path, index=False)

# %%
# Plot things

# Define factors and satisfaction for pair plot analysis
factors = ['CO2_room', 'Relative_humidity_room', 'Lighting_room', 'Indoor_temperature_room', 'Outside temp', 'Satisfaction']

# Create separate datasets for each occupancy scenario
occupant1_data = training_data_sorted[training_data_sorted['Occupancy 1'] == 1]
occupant2_data = training_data_sorted[training_data_sorted['Occupancy 2'] == 1]
occupant3_data = training_data_sorted[training_data_sorted['Occupancy 3'] == 1]

# Create pair plots per occupant 
print("Pair Plot for Occupant 1")
sns.pairplot(occupant1_data, vars=factors, hue='Occupancy 1', palette='viridis')
plt.show()

print("Pair Plot for Occupant 2")
sns.pairplot(occupant2_data, vars=factors, hue='Occupancy 2', palette='viridis')
plt.show()

print("Pair Plot for Occupant 3")
sns.pairplot(occupant3_data, vars=factors, hue='Occupancy 3', palette='viridis')
plt.show()


