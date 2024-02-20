class GridWorld:
    def __init__(self):
        self.grid = [[0] * 5 for _ in range(5)]  # Create a 5x5 grid with all states initialized to 0
        self.agent_position = (2, 2)  # Start the agent in the middle of the grid

    def move_agent(self, direction):
        x, y = self.agent_position
        if direction == 'up' and x > 0:
            self.agent_position = (x - 1, y)
        elif direction == 'down' and x < 4:
            self.agent_position = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.agent_position = (x, y - 1)
        elif direction == 'right' and y < 4:
            self.agent_position = (x, y + 1)

    def move_agent_west(self):
        x, y = self.agent_position
        if y > 0:
            self.agent_position = (x, y - 1)

    def move_agent_west_bouncy(self):
        x, y = self.agent_position
        if y > 0:
            self.agent_position = (x, y - 1)
        else:
            # Reflect the agent back to its current position if it tries to go out of bounds
            self.agent_position = (x, y)

    def print_grid_with_agent(self):
        for i in range(5):
            for j in range(5):
                if (i, j) == self.agent_position:
                    print('A', end=' ')
                else:
                    print(self.grid[i][j], end=' ')
            print()


def moveAgentWest(world):
    world.move_agent_west()


def moveAgentWestBouncy(world):
    world.move_agent_west_bouncy()


world = GridWorld()
world.print_grid_with_agent()  # Initial state with agent in the middle

for i in range (4):
    moveAgentWest(world)
    world.print_grid_with_agent() # State after moving agent one step to the left
    print () 

# moveAgentWestBouncy(world)
# world.print_grid_with_agent()  # State after moving agent another step to the left with bouncing borders
