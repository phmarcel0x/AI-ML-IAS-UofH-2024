import random

def adjust_environment(current, target, adjustment_factor):
    """Adjust the environment towards the target value."""
    if current < target:
        current += adjustment_factor * (target - current)
    elif current > target:
        current -= adjustment_factor * (target - current)
    return current

def simulate_external_factors(current_temp, current_moisture):
    """Simulate external temperature and moisture fluctuations."""
    current_temp += (random.random() - 0.5) * 2  # Random temperature fluctuations
    current_moisture -= (random.random() - 0.5) * 1  # Random moisture fluctuations
    return current_temp, current_moisture

def check_greenhouse_stability(current_temp, current_moisture, desired_temp, desired_moisture):
    """Check for greenhouse stability and adjust if necessary."""
    temp_stable = abs(current_temp - desired_temp) <= 5  # Temperature within 5 degrees of desired
    moisture_stable = abs(current_moisture - desired_moisture) <= 10  # Moisture within 10% of desired
    return temp_stable and moisture_stable

def check_plant_health(current_temp, current_moisture, plants):
    """Check which plants will strive and which will die."""
    plant_status = []
    for plant in plants:
        name, optimal_temp, optimal_moisture, growth_rate = plant
        temp_diff = abs(current_temp-optimal_temp)
        moisture_diff = abs(current_moisture-optimal_moisture)
        if temp_diff <= 5 and moisture_diff <= 10: # Threshholds
            status = 'Thriving'
        else:
            status = 'Dying'
        plant_status.append((name, status))
    return plant_status

# Input desired conditions
desired_temp = float(input("Enter the desired temperature: "))
desired_moisture = float(input("Enter the desired moisture level: "))

# Initial conditions
current_temp = 70.0
current_moisture = 55.0
adjustment_factor_temp = 0.1
adjustment_factor_moisture = 0.2

# Plant data (name, temperature, moisture, growth rate)
plants = [
    ("banana", 75, 60, 0.1),
    ("coconut", 80, 70, 0.1),
    ("mango", 80, 70, 0.1),
    ("papaya", 80, 70, 0.1),
    ("pineapple", 80, 70, 0.1),
    ("coffee", 70, 60, 0.1),
    ("cacao", 70, 60, 0.1),
    ("sugarcane", 75, 60, 0.1),
    ("rice", 75, 60, 0.1),
    ("corn", 75, 60, 0.1),
    ("birds_of_paradise", 75, 60, 0.1)
]

# Simulation loop for a set period or until a stop condition is met
for day in range(1, 31): # Simulate for 30 days
    current_temp, current_moisture = simulate_external_factors(current_temp, current_moisture)
    
    # Adjust environment towards desired conditions
    current_temp = adjust_environment(current_temp, desired_temp, adjustment_factor_temp)
    current_moisture = adjust_environment(current_moisture, desired_moisture, adjustment_factor_moisture)
    
    # Check for greenhouse stability
    stable = check_greenhouse_stability(current_temp, current_moisture, desired_temp, desired_moisture)
    
    # Check for plant health
    plant_health = check_plant_health(current_temp, current_moisture, plants)
    
    
    print(f"Day {day}: Temp: {current_temp:.2f}, Moisture: {current_moisture:.2f}, Stable: {'Yes' if stable else 'No'}")
    for name, status in plant_health:
        print(f"    {name}: {status}")
    
