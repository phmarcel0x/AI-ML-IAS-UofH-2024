"""Motivation controller controller."""
# Template controller for Thymio II robot
# Initialises sensors, motors and Robot Window controller
# Designed to allow various "behaviours" to control the robot.


# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import random
from random import randint

# Hardware constants
DISTANCE_SENSOR_COUNT = 7 #defined by the robot design
GROUND_SENSOR_COUNT = 2 #defined by the robot design

# Control constants
MOTOR_SPEED = 6
# FOOD level (physiological variable)
FOOD_LEVEL_UPPER_BOUND = 150
FOOD_LEVEL_LOWER_BOUND = 0
OXYGEN_LEVEL_UPPER_BOUND = 300
OXYGEN_LEVEL_LOWER_BOUND = 0
# threshold for ground sensors (for resource detection)
THRESHOLD_FISH = 200 # detects darker color, black
THRESHOLD_WATER = 700 # detects lighter color, blue
THRESHOLD_WALL = 1000 # threshold  for detecting a wall for the front sensors

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# initialisation functions
def init_actuators():
    """ Initialise motors and LEDs """
    global motor_left, motor_right, motor_speed_left, motor_speed_right, led_top, led_top_colour

    # Set up motors
    motor_left = robot.getDevice('motor.left')
    motor_right = robot.getDevice('motor.right')

    # Configure motors for velocity control
    motor_left.setPosition(float('inf'))
    motor_right.setPosition(float('inf'))
    
    # set up LEDs
    led_top = robot.getDevice('leds.top')
    # Not used for anything here but can be used to show states etc.

    # initialise variables for actuator values
    reset_actuator_values()

def init_sensors():
    """ Initialise distance sensors, ground sensors etc. """
    global distance_sensors, distance_sensors_values, ground_sensors, ground_sensors_values
    # Set up distance sensors on the front; Much of it is Webots and model specific
    distance_sensors = []
    for i in range(DISTANCE_SENSOR_COUNT):
        distance_sensors_name = 'prox.horizontal.{:d}'.format(i) 
        distance_sensors.append(robot.getDevice(distance_sensors_name))
        distance_sensors[i].enable(timestep)

    # Create array to store distance sensor readings
    distance_sensors_values = [0] * DISTANCE_SENSOR_COUNT

    # Set up ground sensors; Much of it is Webots and model specific
    ground_sensors = []
    for i in range(GROUND_SENSOR_COUNT):
        ground_sensors_name = 'prox.ground.{:d}'.format(i)
        # print(ds_name) # uncomment to debug names
        ground_sensors.append(robot.getDevice(ground_sensors_name))
        ground_sensors[i].enable(timestep)

    # Create array to store ground sensor readings
    ground_sensors_values = [0] * GROUND_SENSOR_COUNT

def read_sensors():
    """ Read sensor values from modelled hardware into variables """
    global distance_sensors, distance_sensors_values, ground_sensors, ground_sensors_values

    for i in range(DISTANCE_SENSOR_COUNT):
        distance_sensors_values[i] = distance_sensors[i].getValue()

    for i in range(GROUND_SENSOR_COUNT):
        ground_sensors_values[i] = ground_sensors[i].getValue()
    

def reset_actuator_values():
    """ Reset motor & LED target variables to zero/off. """
    global motor_speed_left, motor_speed_right, led_top_colour, action_taken
    
    motor_speed_left = 0
    motor_speed_right = 0
    led_top_colour = 0x000000 # Feel free to use this for status communication
    action_taken = False # marker that no action was taken


def send_actuator_values():
    """ Write motor speed and LED colour variables to hardware.
        Called at the end of the Main loop, after actions have been calculated """
    global motor_speed_left, motor_speed_right, led_top_colour
    motor_right.setVelocity(motor_speed_left)
    motor_left.setVelocity(motor_speed_right)
    led_top.set(led_top_colour)

#
# Main entry point for the control code
# 


###### Physiological Variable Homeostasis ######
def manage_PVs(ground_state):
    """ This function decreases the internal physiological variable FOOD"""
    global food_level, oxygen_level
    
    # This reduces the FOOD level and oxygen level slowly
    food_level -= 0.1  # decreases the food level by 0.1 each step
    if ground_state[0] == 'water' and ground_state[1] == 'water' :
        oxygen_level -= 0.7 # decreases the oxygen level by 0.7 each step under water
    elif ground_state[0] == 'land' and ground_state[1] == 'land': 
        oxygen_level +=0.05 # increases the oxygen level by 0.05 each step on land
        if oxygen_level >= OXYGEN_LEVEL_UPPER_BOUND:
                    oxygen_level = OXYGEN_LEVEL_UPPER_BOUND
        

def check_robot_vitality():
    """ This function checks to see if the robot is still alive and stops all movement if not"""
    global food_level, oxygen_level, motor_speed_left, motor_speed_right
    
    #the actual check for the FOOD level
    if food_level <= FOOD_LEVEL_LOWER_BOUND or oxygen_level <= OXYGEN_LEVEL_LOWER_BOUND:
        stop()
        led_top.set(0x000000)
        print('robot dead')


###### Basic Movement Functions ######
def turn_right():
    global motor_speed_left, motor_speed_right
    motor_speed_left = MOTOR_SPEED / 2
    motor_speed_right = MOTOR_SPEED + 3 
    
def turn_left():
    global motor_speed_left, motor_speed_right
    motor_speed_left = MOTOR_SPEED + 3
    motor_speed_right = MOTOR_SPEED / 2

def forward_normal():
    global motor_speed_left, motor_speed_right
    motor_speed_left = MOTOR_SPEED 
    motor_speed_right = MOTOR_SPEED 

def forward_slow(): 
    global motor_speed_left, motor_speed_right
    motor_speed_left = MOTOR_SPEED / 2
    motor_speed_right = MOTOR_SPEED / 2
    
def forward_fast():
    global motor_speed_left, motor_speed_right
    motor_speed_left = 9
    motor_speed_right = 9
    
def backwards_turn():
    global motor_speed_left, motor_speed_right
    motor_speed_left = -4
    motor_speed_right = -9
    
def stop():
    global motor_speed_left, motor_speed_right
    motor_speed_left = 0
    motor_speed_right = 0
 
 
###### Sensing the ground ######   
def detect_ground_states():
    global ground_state
    ground_state  = [None, None]
    for i in range(0,GROUND_SENSOR_COUNT):
        if ground_sensors_values[i] < THRESHOLD_FISH:
            ground_state[i] = 'fish'
        elif ground_sensors_values[i] < THRESHOLD_WATER:
            ground_state[i] = 'water'
        else:
            ground_state[i] = 'land'   
    return ground_state
    


###### Base behaviours ######
def walk_avoid_walls():
    global distance_sensors_values, motor_speed_left, motor_speed_right, current_motor_speed_left, current_motor_speed_right 
    distance_sensors_left = 3*distance_sensors_values[0] + distance_sensors_values[1] + 0.5 * distance_sensors_values[2] 
    distance_sensors_right = 2*distance_sensors_values[4] + distance_sensors_values[3] 

    if distance_sensors_left > distance_sensors_right:
        turn_right()
    elif distance_sensors_right > distance_sensors_left:
        turn_left()
    else: 
        behaviour_random_walk()
        
def behaviour_random_walk():
    """ This function makes the robot wander in stochastic manner with use of the random function."""
    global motor_speed_left, motor_speed_right, walk_stability, current_motor_speed_left, current_motor_speed_right 
    
    print('walk')
    if walk_stability < 0:    
        current_motor_speed_left = MOTOR_SPEED + randint(-2,2)
        current_motor_speed_right = MOTOR_SPEED + randint(-2,2)
        walk_stability = 50
    else:
        walk_stability -= 1 # walk stability ensures that the robot does not act too eratic
     
    motor_speed_left = current_motor_speed_left
    motor_speed_right = current_motor_speed_right
    
###### Coordination ######
def behaviour_coordination():
    """ This function should coordinate the behaviours"""
   
    # Right now it just does the random walk and somewhat avoids walls (does get stuck somethimes)
    walk_avoid_walls()



# Internal physiological states. These are global variables initialised as their respective max values
food_level = FOOD_LEVEL_UPPER_BOUND
oxygen_level = OXYGEN_LEVEL_UPPER_BOUND
walk_stability = 50
current_motor_speed_left = MOTOR_SPEED
current_motor_speed_right = MOTOR_SPEED
# This global variable is used as the timer for how long the simulation has been run for
simulation_run_time = 0
init_sensors()
init_actuators()
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    read_sensors()
    ground_state = detect_ground_states()

    # Process sensor data here.
    reset_actuator_values()
        
    # This calls the decreases the value FOOD
    manage_PVs(ground_state)
    
    # This calls the actual behaviour coordination
    behaviour_coordination()
    
    # This calls the function that checks to see if the robot is still alive.
    check_robot_vitality()

    # Send actuator commands:
    send_actuator_values()

# End of Main loop
# Exit & cleanup code.
# (none required)