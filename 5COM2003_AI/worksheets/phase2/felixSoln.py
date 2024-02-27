"""Expanding the w2 solution (and altering a lot)"""
import random
import time

##################################
## Task 1 - Creating Fields
##################################
class Field:
    content = []
    border = False
    east = None
    west = None
    north = None
    south = None

    def __init__(self, label, goal, name):
        self.label = label
        self.id = name
        self.goal = goal  # For task 3

    def setContent(self, content):
        self.content = content

    def getLabel(self):
        return self.label

    def isGoal(self):  # For task 3
        return self.goal

class Agent:
    def senseLabelAndMakeDecision(self, field):
        return field.getLabel()

    def decisionMaking(self, field):  # Task 3 Function
        if not self.senseGoal(field):  # First check if we want to move
            return self.senseLabelAndMakeDecision(field)  # Then think about moving
        else:
            return "stay"

    def senseGoal(self, field):  # Task 3 Function
        return field.isGoal()

    def randomDecisionMaking(self, field):  # Task 4 Function
        if not self.senseGoal(field):  # First check if we want to move
            return randomLabel()  # Then do not think about moving all that much
        else:
            return "stay"
class Leaf:
    pass

class OneAgentWorld:
    def __init__(self, agentField, agent):
        self.agentField = agentField
        self.agent = agent

    def moveAgent(self, decision):
        if decision == "west" and self.agentField.west is not None:
            self.agentField = self.agentField.west
        if decision == "east" and self.agentField.east is not None:
            self.agentField = self.agentField.east
        if decision == "north" and self.agentField.north is not None:
            self.agentField = self.agentField.north
        if decision == "south" and self.agentField.south is not None:
            self.agentField = self.agentField.south

    def arrivedAtGoal(self):
        return self.agentField.getLabel() == "Goal"

    """
        We know the agents current field
        The agent does not know a thing
        
        We ask the agent and the honor the agents decision.
        This is where we could add differing dynamics
    """
    def runOneStep(self):
        decision = self.agent.senseLabelAndMakeDecision(self.agentField)
        self.moveAgent(decision)

    def runOneStep2(self):
        decision = self.agent.decisionMaking(self.agentField)
        if decision != "stay":
            self.moveAgent(decision)
        return decision

    def randomWalk(self):
        decision = self.agent.randomDecisionMaking(self.agentField)
        if decision != "stay":
            self.moveAgent(decision)
        return decision



def randomLabel():
    return random.choices(["west", "east", "north", "south"])[0]  # Gives us one of the elements

def createGrid():
    listOfFields = []
    for i in range(25):
        listOfFields.append(Field(randomLabel(), False, i))

    for i in range(25):
        # Starting with all west connections
        # All nodes 0,5,10,15,20 do not have a neighbour to the west
        if (i % 5) != 0:  # If not 0,5,10,15,20
            listOfFields[i].west = listOfFields[i - 1]  # Connecting a node to the node left/west of it
        # Continuing with all east connections
        # This excludes all nodes on the eastern border: 4,9,14,19,24
        if ((i + 1) % 5) != 0:
            listOfFields[i].east = listOfFields[i + 1]
        # Continuing with the north, the first 5 (0-4) do not have a north
        if i > 4:
            listOfFields[i].north = listOfFields[i - 5]
        # Continuing with the nodes south
        if i < 20:
            listOfFields[i].south = listOfFields[i + 5]
    return listOfFields



################################
## Creating the Path
################################
# Ensuring there is a path to the eastern edge from the middle
def ensureThereIsAPath(someWorld):
    for i in [12, 13]:
        someWorld[i].label = "east"
    # Ensuring there is a path to the southern corner
    for i in [14, 19]:
        someWorld[i].label = "south"
    return someWorld

################################
## Adding the Objects and Goal
################################
def setupWorld():
    world1 = createGrid()
    world1 = ensureThereIsAPath(world1)
    world1[13].setContent(Leaf())  # Put the leaf into the world (We will never care again)
    return world1

################################
## Running Task 2
################################
"""
grid = setupWorld()
grid[24].label = "Goal"  # Putting the goal in the bottom left corner
world = OneAgentWorld(grid[12], Agent())  # Starting our world with the field the agent is in

while not world.arrivedAtGoal():
    world.runOneStep()
    print(world.agentField.id)
    time.sleep(1)
print("Goal Reached Task 2")
"""
################################
## Running Task 3
################################
"""
grid = setupWorld()
grid[24].goal = True  # Setting the Goal Label to True
world = OneAgentWorld(grid[12], Agent())  # Starting our world with the field the agent is in

intent = ""
while intent != "stay":
    intent = world.runOneStep2()
    print(world.agentField.id)
    time.sleep(1)
print("Goal Reached Task 3")
"""
################################
## Running Task 4 - This might take a while
################################

grid = setupWorld()
grid[24].goal = True  # Setting the Goal Label to True
world = OneAgentWorld(grid[12], Agent())  # Starting our world with the field the agent is in

intent = ""
while intent != "stay":
    intent = world.randomWalk()
    print(world.agentField.id)
    time.sleep(0.3)
print("Goal Reached Task 4")



##################################
## Thank you for reading :)
##################################