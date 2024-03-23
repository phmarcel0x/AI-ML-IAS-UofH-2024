import random
import time

class GridWorld:
    def __init__(self):
        self.rows = 6
        self.cols = 4
        self.grid = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.populate_grid()

    def populate_grid(self):
        positions = [(i, j) for i in range(self.rows) for j in range(self.cols)]
        agent_pos = random.choice(positions)
        positions.remove(agent_pos)
        goal_pos = random.choice(positions)
        positions.remove(goal_pos)
        food_positions = random.sample(positions, 10)

        self.agent_pos = agent_pos
        self.grid[agent_pos[0]][agent_pos[1]] = 'A'
        self.grid[goal_pos[0]][goal_pos[1]] = 'G'
        for pos in food_positions:
            self.grid[pos[0]][pos[1]] = 'F'

    def display_grid(self):
        for row in self.grid:
            print('   '.join(row))


class Agent:
    def __init__(self, world):
        self.world = world
        self.position = world.agent_pos
        self.food_eaten = 0

    def move(self, direction):
        if random.random() < 0.5:  # 50% chance to not move
            return  # Agent stays in place

        x, y = self.position
        if direction == "up":
            x = max(0, x - 1)
        elif direction == "down":
            x = min(self.world.rows - 1, x + 1)
        elif direction == "left":
            y = max(0, y - 1)
        elif direction == "right":
            y = min(self.world.cols - 1, y + 1)

        # Prevent moving into a wall by staying in place if the move is invalid
        if (x, y) != self.position and self.world.grid[x][y] in [' ', 'F', 'G']:
            self.world.grid[self.position[0]][self.position[1]] = ' '  # Clear old position
            self.position = (x, y)
            self.world.grid[x][y] = 'A'
        else:
            # Bounce back logic can be implemented here if required
            pass

    def consume_food(self):
        if self.world.grid[self.position[0]][self.position[1]] == 'F':

            self.world.grid[self.position[0]][self.position[1]] = ' '  # Remove the food
            self.food_eaten += 1
            print(f"Food consumed. Total food eaten: {self.food_eaten}")

    def find_food_direction(self):
        # Detect the direction of the nearest food in adjacent cells
        directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)} 
        for direction, (dx, dy) in directions.items():
            nx, ny = self.position[0] + dx, self.position[1] + dy
            if 0 <= nx < self.world.rows and 0 <= ny < self.world.cols and self.world.grid[nx][ny] == 'F':
                return direction
        return None

    def decide_and_act(self):
        if self.world.grid[self.position[0]][self.position[1]] == 'G':
            print("Agent has reached the goal.")
            return

        if self.world.grid[self.position[0]][self.position[1]] == 'F':
            self.consume_food()
            print("Food is consumed.")
        else:
            food_direction = self.find_food_direction()
            if food_direction:
                self.move(food_direction)
                print(f"Moved {food_direction} towards food.")
            else:
                # Move randomly if no food is adjacent
                self.move(random.choice(["up", "down", "left", "right"]))
                print("Moved randomly.")
        print(f"Food eaten so far: {self.food_eaten}")
        
        
    
        

# To run the simulation:
world = GridWorld()
agent = Agent(world)

print("Initial Grid:")
world.display_grid()

# Test tje decide_and_act method until the goal is reached
while world.grid[agent.position[0]][agent.position[1]] != 'G':
    agent.decide_and_act()
    world.display_grid()
    time.sleep(0.5)


##Incrementer does not work but everything else in the tasks should work as required.
