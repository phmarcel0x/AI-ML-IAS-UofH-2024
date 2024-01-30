import random

# Let the user enter the desired temperature and moisture level
# desired_temp = 75.0 # Target temperature
desired_temp = float(input("Enter the desired temperature: "))
print("Desired temperature:", desired_temp)
current_temp = 70.0 # Initial temperature
adjustment_factor_temp = 0.1 # Temperature adjustment rate

# desired_moisture = 60.0 # Target moisture level
desired_moisture = float(input("Enter the desired moisture level: "))
print("Desired moisture level:", desired_moisture)
current_moisture = 55.0 # Initial moisture level
adjustment_factor_moisture = 0.2 # Moisture adjustment rate


plant_growth_rate = 0.05 # Plant growth rate based on temperature and moisture
print("Initial state:")
print("Temperature:", current_temp)
print("Moisture:", current_moisture)

while True:
    # Negative feedback loop for temperature
    temp_difference = desired_temp - current_temp
    current_temp += adjustment_factor_temp * temp_difference
    
    # Positive feedback loop for plant growth
    growth_factor = current_temp * current_moisture * plant_growth_rate
    
    # Negative feedback loop for moisture (adjusted by plant growth)
    moisture_difference = desired_moisture - (current_moisture + growth_factor)
    current_moisture += adjustment_factor_moisture * moisture_difference
    
    print("\nCurrent state:")
    print("Temperature:", current_temp)
    print("Moisture:", current_moisture)
    print("Plant growth:", growth_factor)
    
    # Simulate external factors
    current_temp += (random.random() - 0.5) * 2 # Random temperature fluctuations
    current_moisture -= (random.random() - 0.5) * 1 # Random moisture fluctuations
    
    # Check for stability
    if abs(temp_difference) < 0.1 and abs(moisture_difference) < 0.2:
        print("\nStable environment achieved.")
        break