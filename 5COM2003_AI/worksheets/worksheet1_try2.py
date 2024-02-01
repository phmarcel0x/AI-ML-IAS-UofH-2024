# 5COM2003: Artificial Intelligence
# Worksheet 1

# Grid World
# Question 1
class GridWorld:
    # GridWorld Constructor
    def __init__(self, size=5):
        self.size = size # Define the size of the square grid world
        self.grid = [['~~' for _ in range(size)] for _ in range(size)] # Create the grid given the size
        self.agent_row = self.agent_col = size // 2 # Starting the agent in the middle of the grid
        self.grid[self.agent_row][self.agent_col] = 'ME' # Place Agent '1' in the grid

    # Function to display the GridWorld
    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()

# Q1 Testing the Grid World's creation, its display, and Agent's initial position
# Comment/Uncomment test function using 'Ctrl + /' OR 'Cmd + /'
# grid_world = GridWorld() # Create an instance of GridWorld
# print() # Nnew line for asethetic purposes
# print("Welcome to agent ME's Grid World!")
# grid_world.display() # Call the GridWorld's display function


# Movement in this Grid World
# Question 2
# Function to move the agent one step to the west WITHOUT handling the western border
def moveAgentWest(grid_world):
    # Clears the agent's current grid position by setting it to '~~'
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = '~~'
    grid_world.agent_col -= 1 # Subtract 1 from the agent's column means moving one step West
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = 'ME' # Place agent 'A' in its new position

# Q2 Testing the moveAgentWest function by 5 steps (WITHOUT handling western border!)
# Comment/Uncomment test function using 'Ctrl + /' OR 'Cmd + /'
# for _ in range(5): 
#     print("Moving agent ME one step West, WITHOUT border patrol:")
#     moveAgentWest(grid_world)
#     grid_world.display()


# Question 3
# Function to move the agent one step to the west WITH handling the western border
def moveAgentWestBouncy(grid_world):
    # Clears the agent's current grid position by setting it to '~~'
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = '~~'
    # Check if agent is at the western boundary
    if grid_world.agent_col == 0:
        # If at western boundary, do not move (bounce)
        print("CAUTION: Western boundary reached. Agent ME can no longer move West.")
        pass
    else:
        # If not, move agent one step West
        grid_world.agent_col -= 1

    # Place agent 'ME' in its new position
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = 'ME'


# Q3 Testing the moveAgentWestBouncy function by 5 steps (WITH handling western border!)
# Comment/Uncomment test function using 'Ctrl + /' OR 'Cmd + /'
# for _ in range(5): 
#     print("Moving agent ME one step West, WITH border patrol:")
#     moveAgentWestBouncy(grid_world)
#     grid_world.display()
    
# Question 4
# Function to move the agent North, while wrapping around the now 'round' world
def moveNorthAroundTheWorld(grid_world):
    # Clears the agent's current grid position by setting it to '~~'
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = '~~'
    # Decreases the row index to move the agent one step north
    grid_world.agent_row -= 1
    # Checks if the agent has moved beyond the northern boundary of the grid
    if grid_world.agent_row < 0:
        # Wraps the agent to the southernmost row if it has moved beyond the northern boundary
        grid_world.agent_row = grid_world.size - 1
    # Places the agent in the new position on the grid, effectively moving it north or wrapping it around
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = 'ME'

# Q4 Testing the moveNorthAroundTheWorld function by 5 steps
# Comment/Uncomment test function using 'Ctrl + /' OR 'Cmd + /'
# for _ in range(5):
#     moveNorthAroundTheWorld(grid_world)
#     print("Moving North - around the world:")
#     grid_world.display()


# Test function for Worksheet's Example Movement:
def test_example_movement(grid_world):
    print()
    print("Testing Example Movement from Worksheet:")
    
    print()
    print("Initial World:")
    grid_world.display()

    # Move the agent twice west (this will put the agent at the western/leftmost border)
    print("Moving agent ME 2 steps West, WITHOUT border patrol:")
    for _ in range(2):
        moveAgentWest(grid_world)
        grid_world.display()
        
    # Move the agent twice west with bounce handling
    print("Moving agent ME 2 steps West, WITH border patrol:")
    for _ in range(2):
        moveAgentWestBouncy(grid_world)
        grid_world.display()

    # Move the agent north three times to demonstrate round world logic
    print("Moving agent ME North 5 times - around the world:")
    for _ in range(5):
        moveNorthAroundTheWorld(grid_world)
        grid_world.display()

# Create an instance of GridWorld
grid_world = GridWorld()
# Execute the test function
test_example_movement(grid_world)