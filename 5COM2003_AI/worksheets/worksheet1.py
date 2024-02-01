class Agent:
    # Constructor
    def __init__(self, row, col):
        self.row = row # Agent's row position
        self.col = col # Agent's column position
        self.name = 'AGNT' # Agent's name

class GridWorld:
    # Constructor
    def __init__(self):
        self.size = 5 # Grid size (5x5)
        # Create grid (list of lists)
        self.grid = []
        for _ in range(self.size):
            self.grid.append([None] * self.size)
        
        self.agent = Agent(2, 2) # Agent's initial position
        
    # Move Agent West Function
    def moveAgentWest(self):
        current_col = self.agent.col # Get current column
        next_col = current_col - 1 # Calculate next column (minus one == one state to the left)
        self.agent.col = next_col # Update agent's new column
            
    # Move Agent West Bouncy Function (agent cannot move off the western boundary of the grid)
    def moveAgentWestBouncy(self):
        current_col = self.agent.col # Get current column
        next_col = current_col - 1 # Calculate next column (one to the left)
        # Check if next column is within the grid boundaries (indexes 0 to 4)
        if next_col >= 0: 
            self.agent.col = next_col # Update agent's new column
        
    # Display Grid World with Agent 'X' in the grid
    def displayGrid(self):
        # Loop through each row and column
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                
                # Check if agent's position is at current row and column
                if self.agent.row == i and self.agent.col == j:
                    print(self.agent.name, end=" ")
                    
                # Otherwise, print empty space
                else:
                    print(None, end=" ")
                
            print() # Print new line after each row

world = GridWorld() # Create GridWorld object

#world = GridWorld() # Create GridWorld object
#world.displayGrid() # Display grid with agent's current position