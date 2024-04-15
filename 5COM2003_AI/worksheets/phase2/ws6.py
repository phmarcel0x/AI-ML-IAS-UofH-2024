import random

grid = [[0]*4 for x in range(6)]

#Food Generation
def add_food(grid):                         
    coordinates = set()
    while len(coordinates) < 10:
        x = random.randint(0, 5)
        y = random.randint(0, 3)
        coordinate = (x, y)
        coordinates.add(coordinate)
    coordinates = list(coordinates)
    for i in coordinates:
        x = i[0]
        y = i[1]
        grid[x][y] = 'f'
    return grid


#Goal Generation
def randgoal(grid):                                 
    coordinate = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                coordinate.append((i, j))

    a = random.randint(0, len(coordinate) - 1)
    r = coordinate[a]
    grid[r[0]][r[1]] = 'G'
    return grid


# Agent Generation
def randagent(grid):                            
    coordinate = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                coordinate.append((i, j))

    a = random.randint(0, len(coordinate) - 1)
    r = coordinate[a]
    grid[r[0]][r[1]] = 'A'
    return grid

def sense(grid, agent_position):
    tile_value = grid[agent_position[0]][agent_position[1]]
    neighbors = []

    if agent_position[0] > 0:
        neighbors.append(grid[agent_position[0]-1][agent_position[1]])
        if agent_position[1] > 0:
            neighbors.append(grid[agent_position[0]-1][agent_position[1]-1])
    if agent_position[0] < len(grid)-1:
        neighbors.append(grid[agent_position[0]+1][agent_position[1]])
        if agent_position[1] < len(grid[0])-1:
            neighbors.append(grid[agent_position[0]+1][agent_position[1]+1])
    if agent_position[1] > 0:
        neighbors.append(grid[agent_position[0]][agent_position[1]-1])
    if agent_position[1] < len(grid[0])-1:
        neighbors.append(grid[agent_position[0]][agent_position[1]+1])

    if 'f' in neighbors:
        return True
    else:
        return False

def print_grid(grid):
    for x in grid:
        print(x)


rangrid = add_food(grid)
print("Food Generation")
print_grid(rangrid)
print()
rangrid = randgoal(rangrid)
print("Goal Generation")
print_grid(rangrid)
print()
rangrid = randagent(rangrid)
print("Agent Generation")
print_grid(rangrid)
