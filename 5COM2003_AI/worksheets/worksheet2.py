# 5COM2003: Artificial Intelligence
# Worksheet 1
white_square = '\u25A1' # Unicode for a white square.
capital_pi = '\u220F' # Unicode for a capital pi.
leaf = '\u2022' # Unicode for a bullet point.

# Grid World II
# Question 1
class Agent:
    def __init__(self, name=capital_pi, row=0, col=0):
        self.name = name
        self.row = row
        self.col = col
        self.position = (row, col)
    
    def display(self):
        print("Agent " + self.name + " is at (" + str(self.row) + str(self.col) + ')')
        print()

class GridWorld:
    # Initialises the grid world with a given size.
    def __init__(self, size=5):
        self.size = size  # Size of the grid (size x size).
        self.agent_name = capital_pi # Displayed name of the agent.
        # String used to fill the grid (and adjust for agent's name length for pleasing display).
        self.grid_fill = white_square * len(self.agent_name)  
        
        # Creates the grid as a list of lists of strings and fills it.
        self.grid = [] 
        for _ in range(size):
            self.grid.append([self.grid_fill] * size)
            
        # Sets the agent's initial position to the center of the grid.
        self.agent_row = size // 2
        self.agent_col = size // 2
        
        # Mark the agent's position on the grid.
        self.grid[self.agent_row][self.agent_col] = self.agent_name  

    # Displays the current state of the grid world.
    def display(self):
        # Prints the grid row by row, and each column is separated by a double space.
        for row in self.grid:
            print('  '.join(row))
        print()


# Movement in this Grid World
# Question 2
# Function to move the agent one step West WITHOUT handling the Western border.
def moveAgentWest(grid_world):
    # Clears agent's current grid position by replacing it with the grid_fill.
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = grid_world.grid_fill 
    # Decreases the column index to move the agent one step West.
    grid_world.agent_col = grid_world.agent_col - 1
    # Place agent in its new position.
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = grid_world.agent_name


# Question 3
# Function to move the agent one step West WITH handling the Western border.
def moveAgentWestBouncy(grid_world):
    # Clears agent's current grid position by replacing it with the grid_fill.
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = grid_world.grid_fill
    
    # Checks if agent is at the Western boundary.
    if grid_world.agent_col == 0:
        # If at Western boundary, do not move (bounce).
        print("CAUTION: Western boundary reached. Agent " + grid_world.agent_name + " can no longer move West.")
        pass
    else:
        # If not at Western boundary, move agent one step West.
        grid_world.agent_col = grid_world.agent_col - 1

    # Place agent in its new position.
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = grid_world.agent_name

    
# Question 4
# Function to move the agent one step North, while wrapping around the now 'round' world
def moveNorthAroundTheWorld(grid_world):
    # Clears agent's current grid position by replacing it with the grid_fill.
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = grid_world.grid_fill
    # Decreases the row index to move the agent one step North.
    grid_world.agent_row = grid_world.agent_row - 1
    
    # Checks if the agent has moved beyond the Northern boundary of the grid.
    if grid_world.agent_row < 0:
        # Wraps the agent to the southernmost row, if it has moved beyond the Northern boundary.
        grid_world.agent_row = grid_world.size - 1 
        
    # Place agent in its new position.
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = grid_world.agent_name


# Test from Worksheet's Example Movement:
def testExampleMovement(grid_world):
    print()
    print("Testing Example Movement from Worksheet:")
    
    print()
    print("Agent "+ grid_world.agent_name + "'s initial World:")
    grid_world.display()

    # Move the agent twice West (this will put the agent at the western/leftmost border).
    print("Moving agent " + grid_world.agent_name + " two steps West, WITHOUT border patrol:")
    for _ in range(2):
        moveAgentWest(grid_world)
        grid_world.display()
        
    # Move the agent two steps West WITH handling the Western border.
    print("Moving agent " + grid_world.agent_name + " two steps West, WITH border patrol:")
    for _ in range(2):
        moveAgentWestBouncy(grid_world)
        grid_world.display()

    # Move the agent North three times to demonstrate round world logic.
    print("Moving agent " + grid_world.agent_name + " North 3 times - around the world:")
    for _ in range(3):
        moveNorthAroundTheWorld(grid_world)
        grid_world.display()
        
    print("The End.")
    print()


# Test Functions Below 

# Q1 Create the Grid World, display it, and place agent in the middle.
grid_world = GridWorld()  # Create an instance of GridWorld.
print()  # New line for asethetic purposes.
print("Question 1 testing:")
print("Welcome to the Grid World of agent " + grid_world.agent_name + "!")
grid_world.display()  # Call the GridWorld's display function.


# Please comment/uncomment and run one question at a time for question 2, 3, 4, and the worksheet's example movement test.

# Q2 Testing the moveAgentWest function by X steps West (WITHOUT handling the Western border).
# Comment/Uncomment test function below using 'Ctrl + /' OR 'Cmd + /'
# print("Question 2 testing:")
# for _ in range(4): # Change the number of steps by changing the range value.
#     print("Moving agent " + grid_world.agent_name + " one step West, WITHOUT border patrol:")
#     moveAgentWest(grid_world)
#     grid_world.display()


# Q3 Testing the moveAgentWestBouncy function by X steps West (WITH handling the Western border).
# Comment/Uncomment test function below using 'Ctrl + /' OR 'Cmd + /'
# print("Question 3 testing:")
# for _ in range(5): # Change the number of steps by changing the range value.
#     print("Moving agent " + grid_world.agent_name + " one step West, WITH border patrol:")
#     moveAgentWestBouncy(grid_world)
#     grid_world.display()


# Q4 Testing the moveNorthAroundTheWorld function by X steps North.
# Comment/Uncomment test function below using 'Ctrl + /' OR 'Cmd + /'
# print("Question 4 testing:")
# for _ in range(5): # Change the number of steps by changing the range value.
#     moveNorthAroundTheWorld(grid_world)
#     print("Moving agent " + grid_world.agent_name + " North - around the world:")
#     grid_world.display()


# Call test from Worksheet's Example Movement
testExampleMovement(grid_world)