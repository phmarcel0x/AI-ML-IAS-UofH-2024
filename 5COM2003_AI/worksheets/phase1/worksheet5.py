# 5COM2003: Artificial Intelligence
# Worksheet 5

white_square = '\u25A1' # Unicode for a white square.
capital_pi = '\u220F' # Unicode for a capital pi.

class GridWorld:
    # Initialises the grid world with a given size.
    def __init__(self, size=5):
        self.size = size  # Size of the grid (size x size).
        self.agent_name = capital_pi # Displayed name of the agent.
        # String used to fill the grid (and adjusted for agent's name length for pleasing display).
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
        
        
grid_world = GridWorld()  # Create an instance of GridWorld.
grid_world.display()  # Display the initial state of the grid world.