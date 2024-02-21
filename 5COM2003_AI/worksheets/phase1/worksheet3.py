# 5COM2003: Artificial Intelligence
# Worksheet 3

# Import the required libraries.
from enum import Enum
import random

# Unicode for characters used in the grid world.
white_square = '\u25A1'  # Unicode for a white square.
double_square_interx = '\u2A4E'  # Unicode for a double square intersection.
black_square = '\u25A0'  # Unicode for a black square.

# Direction Enumeration
class Direction(Enum):
    NORTH = "N" 
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    GOAL = "G"


# Agent Class
class Agent:
    def __init__(self, row, col, agent_char=double_square_interx):
        self.row = row
        self.col = col
        self.agent_char = agent_char  # Character to represent the agent.

    def get_position(self):
        return self.row, self.col
    
    # Perception function for the agent's current label at position is found in the GridWorld class.
    

# Leaf Class
class Leaf:
    def __init__(self, row, col, leaf_char=black_square):
        self.row = row
        self.col = col
        self.leaf_char = leaf_char  # Character to represent the leaf.
        

# Grid World Class
class GridWorld:
    def __init__(self, size=5):
        self.size = size
        self.grid_fill = white_square  # Character to fill the grid.
        self.grid = []
        # Each state contains a dictionary with a character and a label.
        for _ in range(self.size):
            self.grid.append([{'char': self.grid_fill, 'label': None} for _ in range(self.size)])
        self.agent = Agent(size // 2, size // 2)  # Place the agent in the middle of the grid.
        self.leaf = Leaf(size // 2, size // 2 + 1)  # Place the leaf to the right of the agent.
        self.leafGone = False  # Flag to indicate if the leaf has been pushed off the grid.
        self.assign_labels()  # Assign labels to the grid fields.
        self.update_grid()  # Update the grid with the agent and leaf positions.
        self.display_mode = 'normal'  # Default display mode. Automatically changed for the random walk task.
        
    ###########################################################################################
    # TASK 1: ADD LABELS TO EACH FIELD IN THE GRID AND PERCEIVE THE LABEL OF THE CURRENT STATE.
    ###########################################################################################
    # Assign directional labels to states to get to the goal strategically.
    def assign_labels(self):
        for row in range(self.size):
            for col in range(self.size):
                # Assign True to 'goal' for the top-left corner cell, and False for all other cells.
                self.grid[row][col]['goal'] = (row == 0 and col == 0)
                if row > 0:
                    self.grid[row][col]['label'] = Direction.NORTH.value  # North label for all cells in the first column.
                elif col > 0:
                    self.grid[row][col]['label'] = Direction.WEST.value  # West label for all cells in the first row.
                if self.grid[row][col]['goal']:
                    self.grid[row][col]['label'] = Direction.GOAL.value  # Goal label for the top-left corner cell.

    # Perception function for direction.
    def perceive_current_label(self):
        row, col = self.agent.get_position()  
        return self.grid[row][col]['label']  
    ##########################################################################################

    def update_grid(self):
        for row in range(self.size):
            for col in range(self.size):
                self.grid[row][col]['char'] = self.grid_fill  # Reset the grid to the fill character.

        # Place the leaf on the grid if it is within the boundaries.
        if 0 <= self.leaf.row < self.size and 0 <= self.leaf.col < self.size:
            self.grid[self.leaf.row][self.leaf.col]['char'] = self.leaf.leaf_char

        # Place the agent on the grid.
        self.grid[self.agent.row][self.agent.col]['char'] = self.agent.agent_char

    def display(self):
        # Display the grid with labels for the normal tasks with direction labels.
        if self.display_mode == 'normal':
            for row in self.grid:
                print('  '.join([cell['char'] + ' ' + (cell['label'] if cell['label'] else ' ') for cell in row]))  # Display the grid with labels.
            if self.leafGone:
                print("***Leaf " + self.leaf.leaf_char + " has left the chat.***")  # Display a message if the leaf is pushed off the grid.
                self.leafGone = False  # Reset the flag after displaying the message.
                
            # Display the agent's current label using the perceive_current_label method.
            current_label = self.perceive_current_label()
            print("Current label: " + current_label)
            
            # Display if the current goal label is true or false using the is_current_position_goal method.
            is_goal = self.is_current_position_goal()
            if is_goal:
                print("Current position is the goal!")
            else:
                print("Current position is not the goal, keep trying!")
            print()
        # Display the grid without direction labels for the random walk task.
        elif self.display_mode == 'random_walk':
            self.display_for_random_walk()

    def move_agent(self, direction):
        old_row, old_col = self.agent.row, self.agent.col  # Store the current position for comparison.
        new_row, new_col = old_row, old_col  # Initialise new agent position variables.
        
        # Update position based on direction and check if new position is within bounds.
        if direction == Direction.WEST.value and old_col > 0:
            new_col -= 1
            print("Agent moves west.")
        elif direction == Direction.EAST.value and old_col < self.size - 1:
            new_col += 1
            print("Agent moves east.")
        elif direction == Direction.NORTH.value and old_row > 0:
            new_row -= 1
            print("Agent moves north.")
        elif direction == Direction.SOUTH.value and old_row < self.size - 1:
            new_row += 1
            print("Agent moves south.")
        else:
            print("CAUTION: Boundary reached. Agent cannot move further " + direction + ".")

        # Check if agent is moving into the leaf's position.
        if (new_row, new_col) == (self.leaf.row, self.leaf.col):
            self.push_leaf(direction)  # If so, push the leaf in the same direction.

        # Update the agent's position.
        self.agent.row, self.agent.col = new_row, new_col

        # Refresh the grid.
        self.update_grid()
        self.display()

    def push_leaf(self, direction):
        new_row, new_col = self.leaf.row, self.leaf.col  # Initialise new leaf position variables.
        if direction == Direction.WEST.value:
            new_col -= 1
            print("Agent pushes leaf west.")
        elif direction == Direction.EAST.value:
            new_col += 1
            print("Agent pushes leaf east.")
        elif direction == Direction.NORTH.value:
            new_row -= 1
            print("Agent pushes leaf north.")
        elif direction == Direction.SOUTH.value:
            new_row += 1
            print("Agent pushes leaf south.")

        # Check if the new position is off the grid, then update or remove the leaf accordingly.
        if 0 <= new_row < self.size and 0 <= new_col < self.size:
            self.leaf.row, self.leaf.col = new_row, new_col  # Update the leaf's position.
        else:
            self.leaf.row, self.leaf.col = -1, -1  # Leaf is assigned an invalid position to boot it off the grid.
            self.leafGone = True  # Flag that the leaf has been pushed off the grid.
            
    ##########################################################################################################
    # TASK 2: Implement the mini controller to move the agent towards the goal.
    ##########################################################################################################
    def mini_controller(self):
        while True:
            current_label = self.perceive_current_label()  # Step 1: Perceive the current label.
            
            if current_label == Direction.GOAL.value:  # Step 2: Check if the label is the goal.
                print("WOW. Agent " + self.agent.agent_char + " has reached the goal. GG!\n")
                break  # Stop if the goal is reached.

            # Step 3: Move the agent based on the current label.
            if current_label in [direction.value for direction in Direction if direction != Direction.GOAL]:
                self.move_agent(current_label)
            else:
                print("CAUTION: Invalid movement direction: " + current_label + ".")
                break  # Theoretically, this should never happen, but single event upset (SEU) is a thing, lol.
    ##########################################################################################################
    
    #################################################################################################
    # TASK 3: Implement the hierarchical controller to move the agent towards the goal.
    # Where each state has two labels and their respective perception methods: direction and goal.
    #################################################################################################
    # Perception function for checking if current position is the goal.
    def is_current_position_goal(self):
        row, col = self.agent.get_position()
        return self.grid[row][col]['goal']
    
    def hierarchical_controller(self):
        # Continue checking and moving until the goal is reached.
        while not self.is_current_position_goal():
            # If not the goal, proceed with direction labels.
            current_label = self.perceive_current_label()
            self.move_agent(current_label)
        print("WOW. Agent " + self.agent.agent_char + " has reached the goal. GG!\n")
    ###############################################################################################
    
    
    #######################################################################################################################
    # TASK 4: Random walk to the goal, without using direction labels.
    #######################################################################################################################
    def display_for_random_walk(self):
        for row in self.grid: 
            row_display = []  
            for cell in row:  
                char = cell['char']
                label = Direction.GOAL.value if cell.get('goal', False) else ' ' # Display the goal label only.
                row_display.append(char + ' ' + label)  
            print('  '.join(row_display))  
        print()

    def random_walk_to_goal(self):
        self.display_mode = 'random_walk'  # Set the display mode for random walk, without direction labels.
        steps = 0  
        while not self.is_current_position_goal():
            # Randomly select a direction from the available enum values, excluding the goal label for obvious reasons.
            random_direction = random.choice([direction.value for direction in Direction if direction != Direction.GOAL])
            self.move_agent(random_direction)  
            steps += 1
        print("WOW. Agent " + self.agent.agent_char + " has reached the goal in " + str(steps) + " steps.\n")  # For fun.
        self.display_mode = 'normal'  # Reset the display mode after completing the random walk     
    #######################################################################################################################


###########################################################################################################################
# Test functions
# Comment and uncomment the tasks to test each one individually.
world = GridWorld()
###########################################################################################################################

# # Task 1: Display the initial grid world with the agent, leaf and labels.
print("\nInitial Grid World with direction labels for Agent " + world.agent.agent_char + " and Leaf " + world.leaf.leaf_char)
world.display()

# # Task 2: Initiate mini controller to move the agent towards the goal.
# print("Initiate mini controller to move the agent towards the goal:")
# world.mini_controller()

# # Task 3: Initiate hierarchical controller to move the agent towards the goal.
# print("Initiate hierarchical controller to move the agent towards the goal:")
# world.hierarchical_controller()

# # Task 4: Random walk to the goal, without using direction labels, break when the goal is reached.
# print("Random walk to the goal, without using direction labels:")
# world.random_walk_to_goal()