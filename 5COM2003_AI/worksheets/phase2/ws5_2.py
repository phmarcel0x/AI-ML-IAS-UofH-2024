#WS5_2
import random

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
            return False  # Agent stays in place

        x, y = self.position
        if direction == "up":
            x = max(0, x - 1)
        elif direction == "down":
            x = min(self.world.rows - 1, x + 1)
        elif direction == "left":
            y = max(0, y - 1)
        elif direction == "right":
            y = min(self.world.cols - 1, y + 1)

        if (x, y) != self.position and self.world.grid[x][y] in [' ', 'F', 'G']:
            if self.world.grid[x][y] == 'F':  # Added: Checks and consumes food if moving onto a food tile
                self.consume_food()
            self.world.grid[self.position[0]][self.position[1]] = ' '  # Clear old position
            self.position = (x, y)
            self.world.grid[x][y] = 'A'
            return True  # Changed: Now returns True when the agent successfully moves
        return False  # Added: Returns False if the move is not successful

    def consume_food(self):
        self.food_eaten += 1  # No change in the method itself, but it's now called correctly in move()

    def find_food_direction(self):
        directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        for direction, (dx, dy) in directions.items():
            nx, ny = self.position[0] + dx, self.position[1] + dy
            if 0 <= nx < self.world.rows and 0 <= ny < self.world.cols and self.world.grid[nx][ny] == 'F':
                return direction
        return None

    def decide_and_act(self):
        if self.world.grid[self.position[0]][self.position[1]] == 'F':
            self.consume_food()  # No change, but this ensures food is consumed if starting on a food tile

        food_direction = self.find_food_direction()
        if food_direction:
            if self.move(food_direction):  # Changed: move() method's return value is now checked
                print(f"Moved {food_direction} towards food.")
        else:
            if self.move(random.choice(["up", "down", "left", "right"])):  # Changed: move() method's return value is now checked
                print("Moved randomly.")

        print(f"Food eaten so far: {self.food_eaten}")  # Unchanged

# To run the simulation:
world = GridWorld()
agent = Agent(world)

print("Initial Grid:")
world.display_grid()

for _ in range(20):  # Simulate 20 steps
    agent.decide_and_act()
    world.display_grid()
