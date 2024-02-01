# 5COM2003 Worksheet 1

# Grid World
# Question 1
# 
class GridWorld:
    def __init__(self, size=5):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
        # Starting the agent in the middle of the grid
        self.agent_row = self.agent_col = size // 2
        self.grid[self.agent_row][self.agent_col] = 'A'

    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()

grid_world = GridWorld()
grid_world.display()


# Movement in this Grid World
# Question 2
def moveAgentWest(grid_world):
    # Simply move the agent one step to the west
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = '.'
    grid_world.agent_col -= 1
    grid_world.grid[grid_world.agent_row][grid_world.agent_col] = 'A'

# Testing the moveAgentWest function
grid_world = GridWorld()
print("Initial World:")
grid_world.display()

# Move the agent west without handling borders
moveAgentWest(grid_world)
print("After moving west:")
grid_world.display()

