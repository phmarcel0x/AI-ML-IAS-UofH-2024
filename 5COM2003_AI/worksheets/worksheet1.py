# 5COM2003: Artificial Intelligence
# Worksheet 1

# Grid World Setup
# Question 1
class GridWorld:
    # Initializes a new GridWorld of a specified size with the agent in the center
    def __init__(self, size=5):
        self.size = size  # Grid dimension (size x size)
        self.grid = [['~~' for _ in range(size)] for _ in range(size)]  # Initialize grid with water tiles ('~~')
        self.agent_row = self.agent_col = size // 2  # Start agent at the grid's center
        self.grid[self.agent_row][self.agent_col] = 'ME'  # Mark agent's initial position with its name: 'ME'

    # Prints the current state of the GridWorld to the console
    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()

# Demonstrates the initial state of GridWorld
# Uncomment the lines below to test the initial setup of GridWorld
# grid_world = GridWorld()
# print("\nWelcome to agent ME's Grid World!")
# grid_world.display()


# Movement Functions
# Question 2: Move Agent West Without Border Handling
def moveAgentWest(grid_world):
    """Moves the agent one step to the west without considering grid boundaries."""
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = '~~'  # Clear current position
    grid_world.agent_col -= 1  # Move west by one step
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = 'ME'  # Update agent's position

# Uncomment the block below to test moving the agent west without border handling
# for _ in range(5): 
#     print("Moving agent ME one step West, WITHOUT border patrol:")
#     moveAgentWest(grid_world)
#     grid_world.display()


# Question 3: Move Agent West With Bouncy Border
def moveAgentWestBouncy(grid_world):
    """Moves the agent one step west with boundary checking, preventing out-of-bounds movement."""
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = '~~'
    if grid_world.agent_col == 0:  # At western border
        print("CAUTION: Western boundary reached. Agent ME can no longer move West.")
    else:
        grid_world.agent_col -= 1  # Safe to move west
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = 'ME'

# Uncomment the block below to test moving the agent west with bouncy border handling
# for _ in range(5): 
#     print("Moving agent ME one step West, WITH border patrol:")
#     moveAgentWestBouncy(grid_world)
#     grid_world.display()


# Question 4: Move Agent North Around the World
def moveNorthAroundTheWorld(grid_world):
    """Moves the agent north, wrapping around to the southern edge if it goes beyond the northern border."""
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = '~~'
    grid_world.agent_row -= 1  # Move north
    if grid_world.agent_row < 0:  # Wrap around to the bottom
        grid_world.agent_row = grid_world.size - 1
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = 'ME'

# Uncomment the block below to test moving the agent north around the world
# for _ in range(5):
#     print("Moving North - around the world:")
#     moveNorthAroundTheWorld(grid_world)
#     grid_world.display()


# Combined Test Function for Example Movement
def test_example_movement(grid_world):
    """Performs a series of movements to demonstrate different movement handling."""
    print("\nTesting Example Movement from Worksheet:")
    print("\nInitial World:")
    grid_world.display()

    # Move agent west without border handling
    print("Moving agent ME 2 steps West, WITHOUT border patrol:")
    for _ in range(2):
        moveAgentWest(grid_world)
        grid_world.display()
        
    # Move agent west with bouncy border handling
    print("Moving agent ME 2 steps West, WITH border patrol:")
    for _ in range(2):
        moveAgentWestBouncy(grid_world)
        grid_world.display()

    # Move agent north, demonstrating round-world logic
    print("Moving agent ME North 5 times - around the world:")
    for _ in range(5):
        moveNorthAroundTheWorld(grid_world)
        grid_world.display()

# Uncomment below to create an instance of GridWorld and execute the test movements
grid_world = GridWorld()
test_example_movement(grid_world)
