#Food in the field is indicated as '*'
#Goal is indicated as 'G'
#Agent is indicated as 'A'

 #the brain of the agent: makeDecision
    #the first function that is called if agent is triggered.
    #triggers the sensor to start getting information.
    #makes agent decides to eat: if sensor returns -1; by calling eat function. ie agent is in a field with food
    #makes agent decides to end movement: if sensor returns 1. i.e at a goal.
    #makes agent move towards the direction of food if any adjacent field indicates a food by calling the move function.
    #makes agent to make random move if non of the adjacent fields indicate food by calling the move function.
    #display the decision of agent at a given point in time.
    #agent makes decision to eat food if it moves to a field with food.

#when agent decides to move:
    #movement is a possibility of 1 and 0
    #successful move: possibility is 1
    #unsuccessful move: possibility is 0
    #move is successful  even if movement can be bouncy

#Agent makes decision, take action, display its decision and display the grid to show the result of the action
#please, press the 'ALT' key to pause the program to study the solution if using python 3 IDLE


import random
import time
class Agent:
    def __init__(self, ID):
        self.id = ID
        self.position = [] # stores the position of the agent 
        self.decisionBox = {'eat':self.eat, 'move':self.move} #stores agents decision making functions headlines
        self.myWorld = None #stores the image of the gridworld in the agent class
        self.foodCount = 0  #indicate the food consumed by agent
        self.image = None   #holds the agent image in the agent class
        self.buffer = None  # holds the label at agent current position
        self.AdjacentLabels = {} #holds the agent adjacent fields labels

    #returns the Identity representation of the agent   
    def getId(self):
        return self.id

    #remove food from the world
    #counts the number of food consumed by agent
    def eat(self):
        self.buffer = None
        self.foodCount += 1
        
    #senses the label of the agent current field
    #senses the labels of the adjacent fields to the agent
    #returns 1 if agent is at the same field as goal
    #returns -1 if agent is at the same field with food
    
    def sensor(self):
        #if(self.position == self.myWorld.goal):
        #    return 1
        if self.buffer == '*':
            return -1
        if self.buffer == 'G':
            return 1
        row = self.position[0]         
        col = self.position[1]
        if row-1 >= 0:
            self.AdjacentLabels['north'] = self.readLabel(row-1, col)
        else:
            self.AdjacentLabels['north'] = None
        if col+1 < self.myWorld.size[1]:
            self.AdjacentLabels['east'] = self.readLabel(row, col+1)
        else:
            self.AdjacentLabels['east'] = None
        if row+1 < self.myWorld.size[0]:
            self.AdjacentLabels['south'] = self.readLabel(row+1, col)
        else:
             self.AdjacentLabels['south'] = None
        if col-1 >= 0:
            self.AdjacentLabels['west'] = self.readLabel(row, col-1)
        else:
             self.AdjacentLabels['west'] = None
        return 0
    #returns the label of a specified field
    def readLabel(self, x_in, y_in):
        return self.myWorld.grid[x_in][y_in]

    #returns the current position of the agent
    def getPosition(self):
        return self.position
    
    #the brain of the agent
    #the first function that is called if agent is triggered.
    #makes the copy of the gridworld to agent class.
    #makes an image of the agent to the agent class.
    #triggers the sensor to start getting information.
    #makes agent decides to eat: if sensor returns -1; by calling eat function.
    #makes agent decides to end movement: if sensor returns 1. i.e at a goal.
    #makes agent move towards the direction of food if any adjacent field indicates a food by calling the move function.
    #makes agent to make random move if non of the adjacent fields indicate food by calling the move function.
    #display the decision of agent at a given point in time.
    #agent makes decision to eat food if it moves to a field with food.
    def makeDecision(self):
        print("***********Episode begins here***********")
        self.myWorld = world
        self.image = agent1
        self.sensor()
        signal = rand_move = flag = 0
        
        while(signal != 1):
            print("Agent is thinking...\n")
            time.sleep(1)
            print("Adjacent fields: ", self.AdjacentLabels)
            if signal == -1:
                print("agent decides to eat food")
                self.decisionBox['eat']()
            else:
                labels = self.AdjacentLabels
                for k in labels.keys():
                    if labels[k] == '*':
                        print("Agent decides to move: ", k)
                        flag = self.decisionBox['move'](k)
                        rand_move = 0
                        break;
                    else:
                        rand_move = 1
                if rand_move == 1:
                    print("Agent decides to make random move")
                    self.decisionBox['move'](None)
            if(not signal):
                print("move: successful!!!") if flag else  print("move: unsuccessful!!!")

            print("Agent position: ", self.position)
            print("food eaten: ", self.foodCount)
            signal = self.sensor()
            world.display()
            print("**************************************")
            
        if signal == 1:
            print("Agent is at goal. Episode is ended!")
            return

    #moves in a specified direction; dirXY is a list datatype
    #if direction isn't specified makes random move
    
    def move(self, dirXY):
        p_move = p_noMove = 0.5
        outCome = random.choices([1, 0], weights=[p_move, p_noMove])[0]
        if(outCome): 
            direction = random.randint(0,3) if dirXY == None else dirXY
            row = self.position[0]         #gets the current row position of the agent
            col = self.position[1]         #gets the current column position of the agent   
            r=c=0  #r(row direction), c(column direction)
            if direction == 'north' or direction == 0:
                r = -1 if self.position[0]-1 >= 0 else 0
            elif direction == 'south' or direction == 1:
                r = 1 if self.position[0]+1 < self.myWorld.size[0] else 0
            elif direction == 'west' or direction == 2:
                c = -1 if self.position[1]-1 >= 0 else 0
            elif direction == 'east' or direction == 3:
                c = 1 if self.position[1]+1 < self.myWorld.size[1] else 0           
            
            self.buffer = self.myWorld.grid[row+r][col+c]
            self.myWorld.grid[row][col] = None
            if self.buffer != None:
                self.myWorld.grid[row+r][col+c] = [self.image, self.buffer]
                self.position = [row+r, col+c]
            self.myWorld.grid[row+r][col+c] = self.image
            self.position = [row+r, col+c]
            return 1
        else:
            return 0


agent1 = Agent('A')
class GridWorld:
    def __init__(self):
        #creating 6X4 grid
        self.size = (6, 4)
        self.grid = [[None]*4 for i in range(6)]
        self.agent = agent1
        self.placeAgent()
        self.placeGoal()
        self.placeFood()

    #places agent randomly in the gridworld
    def placeAgent(self):
        self.agent.position = [random.randint(0, 5), random.randint(0, 3)]
        self.grid[self.agent.position[0]][self.agent.position[1]] = self.agent

    #place the goal randomly in the grid.  
    def placeGoal(self):
        rand = [random.randint(0, 5), random.randint(0, 3)]
        while self.grid[rand[0]][rand[1]] != None:
            rand = [random.randint(0, 5), random.randint(0, 3)]
        self.grid[rand[0]][rand[1]] = 'G'
        self.goal = [rand[0], rand[1]]

    #places the foods randomly in the grid
    def placeFood(self):
        for i in range(10):
            rand = [random.randint(0, 5), random.randint(0, 3)]
            while self.grid[rand[0]][rand[1]] != None:
                rand = [random.randint(0, 5), random.randint(0, 3)]
            self.grid[rand[0]][rand[1]] = '*'

    #display the gridworld
    def display(self):
            print()
            for obj in self.grid:
                for state in obj:
                    print('[', end='')
                    if type(state) == type(self.agent) or type(state) == list:
                        print(self.agent.getId(), end='')
                    elif state == None:
                        print(' ', end='')
                    else:
                        print(state, end='')
                    print(']', end=' ')
                print()
                
    #triggers the agent to start working
    def triggerAgent(self):
        self.agent.makeDecision()

              
world = GridWorld()
world.display()
print("initial grid")
print()
world.triggerAgent()
