
# 6COM2007 - Coursework 2: System Simulation Design
# Author: Marcelo Hernandez 
# University of Hertfordshire - ID: 23033126
# April 25, 2024

import pandas as pd
import numpy as np

# Load the cleaned datasets
training_data_path = 'C:/Users/marsp/OneDrive/Escritorio/UK/code-AI-ML-IAS/6COM2007_IAS/IAS_DATA/6com2007-3_cleaned.csv'
training_data = pd.read_csv(training_data_path)

# Convert 'Datetime' column to datetime type
training_data['Datetime'] = pd.to_datetime(training_data['Datetime'])

# Constants for the simulation
HEATING_DURATION = pd.Timedelta(hours=4)
HEATING_EFFECT = 0.5  # temperature increase in degrees
MAX_HEATING_ACTIVATIONS_PER_DAY = 2
TIME_INTERVAL = pd.Timedelta(minutes=15)

# Select only the rows with the '11:45' timestamp
initial_conditions_data = training_data[training_data['Time'] == '11:45']

# Select only numeric columns for calculating the initial state
useful_columns = ['Indoor_temperature_room', 'Relative_humidity_room', 'CO2_room']
initial_conditions = initial_conditions_data[useful_columns].mean()

# Initialise the state of the home environment
environment_state = {
    'indoor_temp': initial_conditions['Indoor_temperature_room'],  # Use the actual column name from your dataset
    'indoor_humidity': initial_conditions['Relative_humidity_room'],  # Use the actual column name from your dataset
    'CO2': initial_conditions['CO2_room'],  # Use the actual column name from your dataset
    'heater_active': False,
    'ventilation_active': False,
    'heater_activation_times': [],  # List to store datetime when the heater was activated
}

# Update the environment state for each time step
def update_environment(state, current_time, outdoor_conditions, occupancy):
    
    # Outdoor conditions (for ventilation)
    outdoor_temp = outdoor_conditions['temp']
    outdoor_humidity = outdoor_conditions['humidity']

# Simulation loop
def run_simulation(data, state):
    simulation_results = []

    for index, row in data.iterrows():
        current_time = row['Datetime']
        outdoor_conditions = {'temp': row['Outside temp'], 'humidity': row['Outdoor_relative_humidity_Sensor']} 
        occupancy = {'occupancy_1': row['Occupancy 1'], 'occupancy_2': row['Occupancy 2'], 'occupancy_3': row['Occupancy 3']}  
        
        # Update environment
        updated_state = update_environment(state, current_time, outdoor_conditions, occupancy)
        
        # Save the results
        simulation_results.append({
            'Datetime': current_time,
            'Indoor Temperature': updated_state['indoor_temp'],
            'Indoor Humidity': updated_state['indoor_humidity'],
            'CO2': updated_state['CO2']
        })
        
        # Update the current state for the next iteration
        state = updated_state

    return pd.DataFrame(simulation_results)

# Run the simulation with the training data starting from the specified date and time
start_datetime = pd.to_datetime('13/03/2012 11:45')
simulation_data = training_data[training_data['Datetime'] >= start_datetime]
simulation_results = run_simulation(simulation_data, environment_state)
simulation_results.to_csv('simulation_output.csv', index=False)