# 5COM2003: Artificial Intelligence
# Worksheet 5

from enum import Enum
import random
import time

# Constants for the grid world
white_square = '\u25A1'  # Unicode for a white square.
double_square_interx = '\u2A4E'  # Unicode for a double square intersection.
black_square = '\u25AA'  # Unicode for a small black square.
GOAL = 'G'

# Directions Enumeration
class Direction(Enum):
    NORTH = "North"
    SOUTH = "South"
    EAST = "East"
    WEST = "West"

# Agent Class
class Agent:
    def __init__(self, row, col, agent_char=double_square_interx):
        self.row = row
        self.col = col
        self.agent_char = agent_char
        self.consumed_food = 0
    
    def get_position(self):
        return self.row, self.col
    
    # (TASK 2)
    def sense_goal(self, grid_world):
        return grid_world.grid[self.row][self.col]['char'] == GOAL

    # Move the agent in the grid world. (TASK 2)
    def move(self, direction, grid_world):
        
        # 50% chance to move or stay in place (TASK 3)
        if random.choice([True, False]):
            new_row, new_col = self.row, self.col
            if direction == Direction.NORTH:
                new_row -= 1
            elif direction == Direction.SOUTH:
                new_row += 1
            elif direction == Direction.EAST:
                new_col += 1
            elif direction == Direction.WEST:
                new_col -= 1

            # Check if the new position is within the grid boundaries.
            if 0 <= new_row < grid_world.m_rows and 0 <= new_col < grid_world.n_cols:
                grid_world.update_agent_position(self.row, self.col, new_row, new_col)
                self.row, self.col = new_row, new_col
                print("Agent moves", direction.value + ".")
            else:
                print("Agent cannot move further", direction.value + ".")
        else:
            print("World has decided that the agent shall not move.")
        
        # Check if the agent has reached the goal after moving.
        if self.sense_goal(grid_world):
            print("Agent has reached the goal!")
            return
            
    # If the agent finds food, it consumes it. (TASK 3)
    def consume_food(self, grid_world):
        if grid_world.grid[self.row][self.col]['food']:
            grid_world.grid[self.row][self.col]['food'] = False
            self.consumed_food += 1
            print("Agent consumes food. Total food consumed:", self.consumed_food)
            return True
        else:
            print("Agent does not find food to consume at this field.")
            return False
    
    # (TASK 2)
    def sense_food(self, grid_world):
        food_nearby = False  # Assume no food is nearby.
        food_directions = []  # List to store the directions to the food.
        # Define the directions with direction labels.
        directions = { 
            Direction.NORTH: (-1, 0),
            Direction.EAST: (0, 1),
            Direction.SOUTH: (1, 0),
            Direction.WEST: (0, -1)
        }
        
        # Check each adjacent field for food.
        for direction, (dir_row, dir_col) in directions.items():
            row, col = self.row + dir_row, self.col + dir_col  # Calculate the adjacent field.
            if 0 <= row < grid_world.m_rows and 0 <= col < grid_world.n_cols:
                if grid_world.grid[row][col]['food']:
                    food_nearby = True  # Flag that food is nearby.
                    food_directions.append(direction)  # Store the direction to the food.
        
        if food_nearby:
            print("Agent senses food in direction(s):", ", ".join(direction.value for direction in food_directions))
        else:
            print("Agent does not sense food nearby.")
        
        return food_directions
    
    # Perception-Action Decision Making (TASK 4)
    def perception_action(self, grid_world):
        if self.sense_goal(grid_world):
            print("Agent has reached the goal. The End.")
            return
        
        if grid_world.grid[self.row][self.col]['food']:
            self.consume_food(grid_world)
            return True
        
        food_directions = self.sense_food(grid_world)
        if food_directions:
            chose_direction = random.choice(food_directions)
            self.move(chose_direction, grid_world)
            return True
        else:
            direction = random.choice(list(Direction))
            self.move(direction, grid_world)
            return True


# GridWorld Class
class GridWorld:
    def __init__(self, m_rows=6, n_cols=4, grid_fill=white_square, food_char=black_square):
        self.m_rows = m_rows
        self.n_cols = n_cols
        self.grid_fill = grid_fill
        self.food_char = food_char
        # Create the grid as a list of lists of dictionaries and fill it.
        self.grid = []
        for _ in range(self.m_rows):
            self.grid.append([{'char': self.grid_fill, 'food': False} for _ in range(n_cols)])
        
        self.agent = Agent(0, 0)  # Create the agent.
        self.place_agent()  
        self.place_food(10)
        self.place_goal()
    
    # Helper function to get a unique field in the grid.
    def get_unique_field(self):
        while True:
            row = random.randint(0, self.m_rows - 1)
            col = random.randint(0, self.n_cols - 1)
            if self.grid[row][col]['char'] == self.grid_fill and not self.grid[row][col]['food']:
                return row, col
    
    def place_agent(self):
        self.agent.row, self.agent.col = self.get_unique_field()  
        self.grid[self.agent.row][self.agent.col]['char'] = self.agent.agent_char
        
    def place_food(self, num_food):
        for _ in range(num_food):
            row, col = self.get_unique_field()  
            self.grid[row][col]['food'] = True

    def place_goal(self):
        row, col = self.get_unique_field()   
        self.grid[row][col]['char'] = GOAL
    
    def update_agent_position(self, old_row, old_col, new_row, new_col):
        if self.grid[old_row][old_col]['char'] != GOAL:
            self.grid[old_row][old_col]['char'] = self.grid_fill
        self.agent.row, self.agent.col = new_row, new_col


    def display(self):
        for row in range(self.m_rows):
            row_display = []
            for col in range(self.n_cols):
                if self.agent.row == row and self.agent.col == col:
                    display_char = self.agent.agent_char
                elif self.grid[row][col]['food']:
                    display_char = self.food_char  # Display food character if food is present and no agent.
                else:
                    display_char = self.grid[row][col]['char']  # Otherwise, display the field's default character.
                row_display.append(display_char)
            print('    '.join(row_display))
            
#####################################################################
# TASK 1 Test Code 
# (Do not comment this block)
#####################################################################
world = GridWorld()
print("\nInitial grid world of agent " + world.agent.agent_char + " :")
world.display()
print()
#####################################################################

#####################################################################
# TASK 2 Test Code (random movemement of the agent) 
# (Comment/Uncomment as you please)
#####################################################################
# iteration_count = 0
# max_iterations = 1000  # Safety limit to avoid infinite loops.

# while iteration_count < max_iterations:
#     if world.agent.sense_goal(world):
#         print("The goal has been reached. THE END.\n")
#         break
    
#     direction = random.choice(list(Direction))
#     world.agent.move(direction, world)
#     world.display()
    
#     world.agent.consume_food(world)
#     world.agent.sense_food(world)
    
#     iteration_count += 1
#     print("Task 2 iteration:", iteration_count)
#     print()

# if iteration_count >= max_iterations:
#     print("Max iterations reached without finding the goal :( ")
#####################################################################

#####################################################################
# TASK 4 Test Code (Perception-Action Decision Making)
#####################################################################
# Main simulation loop for TASK 4
iteration_count = 0
max_iterations = 1000  # Safety limit to avoid infinite loops.

print("\nTASK 4 (PERCEPTION-ACTION) SIMULATION\n")

while iteration_count < max_iterations:
    print("Task 4 action:", iteration_count)
    
    action_result = world.agent.perception_action(world)
    world.display()
    
    if not action_result:
        print("\nAhhhh\n")
        break
    
    iteration_count += 1
    print()
    
    # time.sleep(1)  # Sleep for 1 second to slow down the simulation.

if iteration_count >= max_iterations:
    print("\nMaximum iterations reached. Retry the simulation.\n")