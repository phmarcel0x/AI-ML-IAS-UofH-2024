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
        self.agent_char = agent_char  # Character to represent the agent.

    def get_position(self):
        return self.row, self.col

# Leaf Class
class Leaf:
    def __init__(self, row, col, leaf_char=notation_spot):
        self.row = row
        self.col = col
        self.leaf_char = leaf_char
        
    def move(self, direction, size):
        if direction == "west" and self.col > 0:
            self.col -= 1
        elif direction == "east" and self.col < size - 1:
            self.col += 1
        elif direction == "north" and self.row > 0:
            self.row -= 1
        elif direction == "south" and self.row < size - 1:
            self.row += 1
        else:
            return False  # Leaf pushed off the grid.
        return True

# Grid World Class
class GridWorld:
    def __init__(self, size=5):
        self.size = size
        self.grid_fill = white_square  # Fill character for the grid.
        self.grid = [[self.grid_fill for _ in range(self.size)] for _ in range(self.size)]
        self.agent = Agent(size // 2, size // 2)
        self.leaf = Leaf(size // 2, size // 2 + 1)
        self.leafGone = False
        self.update_grid()
        
    def update_grid(self):
        self.grid = [[self.grid_fill for _ in range(self.size)] for _ in range(self.size)]  # Reset the grid to the fill character.
        # Place the leaf on the grid if it is within the grid boundaries.
        if 0 <= self.leaf.row < self.size and 0 <= self.leaf.col < self.size:
            self.grid[self.leaf.row][self.leaf.col] = self.leaf.leaf_char 
        self.grid[self.agent.row][self.agent.col] = self.agent.agent_char  # Place the agent on the grid.   

    def display(self):
        for row in self.grid:
            print('  '.join(row))
        if self.leafGone:
            print("Leaf has left the chat.")
            self.leafGone = False  # Reset the flag after displaying the message.
        print()

    # Check if the leaf is pushed off the grid and move it in the given direction.
    def check_and_move_leaf(self, direction):
        if not self.leaf.move(direction, self.size):
            self.leaf.row, self.leaf.col = -1, -1
            self.leafGone = True  # Set the flag to display the message.

    def moveAgentWest(self):
        if (self.agent.row, self.agent.col - 1) == (self.leaf.row, self.leaf.col):
            self.check_and_move_leaf("west")
        if self.agent.col > 0:
            self.agent.col -= 1
            print("Agent moves West.")
        else:
            print("CAUTION: Western boundary reached. Agent cannot move West.")
        self.update_grid()
        self.display()

    def moveAgentEast(self):
        if (self.agent.row, self.agent.col + 1) == (self.leaf.row, self.leaf.col):
            self.check_and_move_leaf("east")
        if self.agent.col < self.size - 1:
            self.agent.col += 1
            print("Agent moves East.")
        else:
            print("CAUTION: Eastern boundary reached. Agent cannot move East.")
        self.update_grid()
        self.display()

    def moveAgentNorth(self):
        if (self.agent.row - 1, self.agent.col) == (self.leaf.row, self.leaf.col):
            self.check_and_move_leaf("north")
        if self.agent.row > 0:
            self.agent.row -= 1
            print("Agent moves North.")
        else:
            print("CAUTION: Northern boundary reached. Agent cannot move North.")
        self.update_grid()
        self.display()

    def moveAgentSouth(self):
        if (self.agent.row + 1, self.agent.col) == (self.leaf.row, self.leaf.col):
            self.check_and_move_leaf("south")
        if self.agent.row < self.size - 1:
            self.agent.row += 1
            print("Agent moves South.")
        else:
            print("CAUTION: Southern boundary reached. Agent cannot move South.")
        self.update_grid()
        self.display()

# Initialize the GridWorld
world = GridWorld()
print("\nInitial Grid World with Agent and Leaf:")
world.display()

for _ in range(2): 
    world.moveAgentEast()

# agent_position = world.agent.get_position()
# print("Agent's Current Position: Row " + str(agent_position[0]) + ", Column " + str(agent_position[1]))
