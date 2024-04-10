# 5COM2003: Artificial Intelligence
# Worksheet 6

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
        self.energy = 4  # Energy level of the agent
        self.action_counts = {'move': 0, 'consume_food': 0}  # Count of actions taken.
    
    
    def get_position(self):
        return self.row, self.col
    
    def get_energy(self):
        return self.energy
    
    def sense_goal(self, grid_world):
        return grid_world.grid[self.row][self.col]['char'] == GOAL

    # Move the agent in the grid world.
    def move(self, direction, grid_world):
    
        self.action_counts['move'] += 1
        
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
            self.energy -= 1  # Reduce the energy level by 1 for each move.
            print("Agent moves", direction.value + ". (-1 energy)")
        else:
            print("Agent cannot move further", direction.value + ". (-1 energy)")
            self.energy -= 1  # Reduce the energy level by 1 even if the move is invalid.
       
        # Check if the agent has reached the goal after moving.
        if self.sense_goal(grid_world):
            print("Agent has reached the goal!")
            return
            
            
    # If the agent finds food, it consumes it.
    def consume_food(self, grid_world):
        
        self.action_counts['consume_food'] += 1
        
        if grid_world.grid[self.row][self.col]['food']:
            grid_world.grid[self.row][self.col]['food'] = False
            self.consumed_food += 1
            self.energy += 5  # Increase the energy level by 5 for each food consumed.
            print("Agent consumes food (+5 energy)")
            print("Total food consumed =", self.consumed_food)
            return True
        else:
            print("Agent does not find food to consume at this field.")
            return False
    

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
        
        # if food_nearby:
        #     print("Agent senses food in direction(s):", ", ".join(direction.value for direction in food_directions))
        # else:
        #     print("Agent does not sense food nearby.")
        
        return food_directions
    
    # Perception-Action Decision Making
    def perception_action(self, grid_world):
        
        if self.energy <= 0:
            print("Agent has run out of energy. Game Over.")
            return False
        
        if self.sense_goal(grid_world):
            print("Agent has reached the goal. The End.")
            return False
        
        if grid_world.grid[self.row][self.col]['food']:
            self.consume_food(grid_world)
            
        else:
            food_directions = self.sense_food(grid_world)  # Check for food before deciding to move.
            if food_directions:
                chose_direction = random.choice(food_directions)
                self.move(chose_direction, grid_world)
            else:
                direction = random.choice(list(Direction))
                self.move(direction, grid_world)
        
        # After action, sense for food again and report it at the end of the action.
        # food_directions_after_action = self.sense_food(grid_world)
        # if food_directions_after_action:
        #     print("Agent senses food in direction(s):", ", ".join(direction.value for direction in food_directions_after_action))
        # else:
        #     print("Agent does not sense food nearby.")
        
        return True
        
    def update_agent_energy(self):
        if self.energy <= 0:
            print("Agent has run out of energy. Game Over.\n")
            return False
        else:
            print("Agent energy level:", self.energy)
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
world = GridWorld()
print("\nInitial grid world of agent " + world.agent.agent_char + " :")
world.display()
print("Agent energy level:", world.agent.energy)
# print()
initial_food_directions = world.agent.sense_food(world)  # Call to sense_food
if initial_food_directions:
    print("Agent senses food in direction(s):", ", ".join(direction.value for direction in initial_food_directions))
else:
    print("Agent does not sense food nearby.")
#####################################################################

#####################################################################
# Move Around Until the Goal is Reached OR Energy is Depleted.
#####################################################################
# Main simulation loop.
iteration_count = 1
max_iterations = 1000  # Safety limit to avoid infinite loops.

print("\nBEGIN AGENT-WITH-ENERGY SIMULATION:")

while iteration_count < max_iterations:
    print("Action #", iteration_count)

    if world.agent.energy > 0:
        action_result = world.agent.perception_action(world)  # Agent takes an action based on perception.
        world.display()  # Display the grid after the action.

        # Now, sense and display food directions based on the updated agent position and grid state.
        food_directions_after_action = world.agent.sense_food(world)
        if food_directions_after_action:
            print("Agent senses food in direction(s):", ", ".join(direction.value for direction in food_directions_after_action))
        else:
            print("Agent does not sense food nearby.")

        energy_status = world.agent.update_agent_energy()  # Update and print the agent's energy status.
        
        if not action_result or not energy_status:
            print("Simulation ends due to energy depletion or goal reached.\n")
            break
        
        iteration_count += 1
        print()
    else:
        print("Agent has run out of energy. Game Over.\n")
        break
    
    # time.sleep(0.5)
    
    total_actions = sum(world.agent.action_counts.values())
    if total_actions > 0:
        energy_per_action = world.agent.get_energy() / total_actions
    else:
        energy_per_action = 0
        
# Calculating and printing the efficiency for each action type
print("\nEfficiency of actions based on remaining energy and actions taken:")
for action_type, count in world.agent.action_counts.items():
    efficiency = count * energy_per_action
    print(f"{action_type}: {efficiency:.2f}")

if iteration_count >= max_iterations:
    print("\nMaximum iterations reached. Retry the simulation.\n")
