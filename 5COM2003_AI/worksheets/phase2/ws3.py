import random

class Agent:
    def __init__(self, x, y):
        # Initialize the agent with its position
        self.x = x
        self.y = y

    def get_position(self):
        # Return the current position of the agent
        return self.x, self.y

    def perceive_label(self, grid_world):
        # Return the label of the current field
        return grid_world.get_label(self.x, self.y)

    def move(self, direction):
        # Move the agent in the specified direction
        if direction == 'north':
            self.x -= 1
        elif direction == 'south':
            self.x += 1
        elif direction == 'west':
            self.y -= 1
        elif direction == 'east':
            self.y += 1


class Leaf:
    def __init__(self, x, y):
        # Initialize the leaf with its position
        self.x = x
        self.y = y


class GridWorld:
    def __init__(self, size=5):
        # Initialize the grid world with the specified size
        self.size = size
        # Create a grid filled with zeros
        self.grid = [[0] * size for _ in range(size)]
        # Create an agent instance at the center of the grid
        self.agent = Agent(size // 2, size // 2)
        # Create a leaf instance to the right of the agent
        self.leaf = Leaf(size // 2, size // 2 + 1)
        # Place the goal label in one of the corners
        corner = random.choice([(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)])
        self.grid[corner[0]][corner[1]] = 'goal'
        # Add direction labels to guide the agent towards the goal
        self.add_direction_labels()

    def add_direction_labels(self):
        # Add direction labels to guide the agent towards the goal
        goal_x, goal_y = self.get_goal_position()
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) != (goal_x, goal_y):
                    if i < goal_x:
                        self.grid[i][j] = 'south'
                    elif i > goal_x:
                        self.grid[i][j] = 'north'
                    if j < goal_y:
                        self.grid[i][j] = 'east'
                    elif j > goal_y:
                        self.grid[i][j] = 'west'

    def get_goal_position(self):
        # Return the position of the goal
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 'goal':
                    return i, j

    def get_label(self, x, y):
        # Return the label of the specified field
        return self.grid[x][y]

    def print_grid(self):
        # Print the current state of the grid with the agent and leaf positions
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) == self.agent.get_position():
                    print(" A ", end="")
                elif (i, j) == (self.leaf.x, self.leaf.y):
                    print(" L ", end="")
                else:
                    print(f" {self.grid[i][j]} ", end="")
            print()

    def move_agent(self, direction):
        # Move the agent in the specified direction and handle collisions
        self.agent.move(direction)
        self.handle_collision(direction)

    def handle_collision(self, direction):
        # Check if the agent collides with boundaries or the leaf, and handle accordingly
        agent_x, agent_y = self.agent.get_position()
        leaf_x, leaf_y = self.leaf.x, self.leaf.y

        # Handle boundary collisions
        if agent_x < 0:
            self.agent.x = 0
        elif agent_x >= self.size:
            self.agent.x = self.size - 1

        if agent_y < 0:
            self.agent.y = 0
        elif agent_y >= self.size:
            self.agent.y = self.size - 1

        # Handle collisions with the leaf
        if (agent_x, agent_y) == (leaf_x, leaf_y):
            # Move the leaf if the agent collides with it
            if direction == 'north' and leaf_x > 0:
                self.leaf.x -= 1
            elif direction == 'south' and leaf_x < self.size - 1:
                self.leaf.x += 1
            elif direction == 'west' and leaf_y > 0:
                self.leaf.y -= 1
            elif direction == 'east' and leaf_y < self.size - 1:
                self.leaf.y += 1
                
    def random_walk_to_goal(self):
        steps = 0  
        while True:
            # Randomly select a direction from the available directions
            random_direction = random.choice(['north', 'south', 'east', 'west'])
            self.move_agent(random_direction)  
            steps += 1
            # Check if the agent has reached the goal
            if self.agent.perceive_label(self) == 'goal':
                print("Agent has reached the goal in " + str(steps) + " steps.\n")
                break


# Example Usage:
# if __name__ == "__main__":
#     # Create a GridWorld instance with a size of 5
#     grid_world = GridWorld()

#     # Print the initial state of the grid
#     print("Initial Grid:")
#     grid_world.print_grid()
#     print()

#     # Move the agent according to the labels towards the goal
#     while True:
#         label = grid_world.agent.perceive_label(grid_world)
#         if label == 'goal':
#             print("Goal reached!")
#             break
#         else:
#             print(f"Moving {label}")
#             grid_world.move_agent(label)
#             grid_world.print_grid()
#             print()
            
# Example Random Walk:
if __name__ == "__main__":
    # Create a GridWorld instance with a size of 5
    grid_world = GridWorld()

    # Print the initial state of the grid
    print("Initial Grid:")
    grid_world.print_grid()
    print()

    # Start the random walk towards the goal
    grid_world.random_walk_to_goal()