# 5COM2003: Artificial Intelligence
# Worksheet 2

# Unicode for characters used in the grid world.
white_square = '\u25A1'  # Unicode for a white square.
capital_pi = '\u220F'  # Unicode for a capital pi.
notation_spot = '\u2981'  # Unicode for a notation spot.

# Agent Class
class Agent:
    def __init__(self, row, col, agent_char=capital_pi):
        self.row = row
        self.col = col
        self.agent_char = agent_char

    def get_position(self):
        return self.row, self.col

# Leaf Class
class Leaf:
    def __init__(self, row, col, leaf_char=notation_spot):
        self.row = row
        self.col = col
        self.leaf_char = leaf_char

# Grid World Class
class GridWorld:
    def __init__(self, size=5):
        self.size = size
        self.grid_fill = white_square
        self.grid = [[self.grid_fill for _ in range(self.size)] for _ in range(self.size)]
        self.agent = Agent(size // 2, size // 2)
        self.leaf = Leaf(size // 2, size // 2 + 1)
        self.update_grid()

    def update_grid(self):
        self.grid = [[self.grid_fill for _ in range(self.size)] for _ in range(self.size)]
        self.grid[self.agent.row][self.agent.col] = self.agent.agent_char
        self.grid[self.leaf.row][self.leaf.col] = self.leaf.leaf_char

    def display(self):
        for row in self.grid:
            print('  '.join(row))
        print()

    def moveAgentWest(self):
        if self.agent.col > 0:
            self.agent.col -= 1
            self.update_grid()
        else:
            print("CAUTION: Western boundary reached. Agent cannot move West.")

    def moveAgentEast(self):
        if self.agent.col < self.size - 1:
            self.agent.col += 1
            self.update_grid()
        else:
            print("CAUTION: Eastern boundary reached. Agent cannot move East.")

    def moveAgentNorth(self):
        if self.agent.row > 0:
            self.agent.row -= 1
            self.update_grid()
        else:
            print("CAUTION: Northern boundary reached. Agent cannot move North.")

    def moveAgentSouth(self):
        if self.agent.row < self.size - 1:
            self.agent.row += 1
            self.update_grid()
        else:
            print("CAUTION: Southern boundary reached. Agent cannot move South.")


world = GridWorld()
print("\nInitial grid world with agent and leaf.")
world.display()

for _ in range(3):
    world.moveAgentSouth()
    world.display()

agent_position = world.agent.get_position()
print("Agent's Current Position: Row " + str(agent_position[0]) + ", Column " + str(agent_position[1]))