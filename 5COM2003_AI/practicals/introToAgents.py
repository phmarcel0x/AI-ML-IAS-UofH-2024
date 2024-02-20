# Introduction to AI agents
print()
print("Welcome to the world of AI agents!")
print("An AI agent is an entity that perceives its environment and takes actions to achieve a goal.")
print("AI agents can be designed to solve complex problems, make decisions, and learn from experience.")
print("They can be found in various domains, such as robotics, gaming, finance, healthcare, and more.")
print("Let's explore the fascinating world of AI agents together!")
print()

# Example 1: Simple AI agent
class SimpleAgent:
    def __init__(self):
        self.environment = None

    def perceive(self, environment):
        self.environment = environment

    def act(self):
        if self.environment == "clean":
            print("The environment is already clean.")
        else:
            print("Cleaning the environment.")

# Example 2: Reinforcement Learning agent
class RLAgent:
    def __init__(self):
        self.state = None

    def perceive(self, state):
        self.state = state

    def act(self):
        if self.state == "win":
            print("Celebrating the victory!")
        elif self.state == "lose":
            print("Analyzing the defeat and learning from it.")
        else:
            print("Taking a random action.")

# Example 3: Natural Language Processing agent
class NLPAgent:
    def __init__(self):
        self.input_text = None

    def perceive(self, input_text):
        self.input_text = input_text

    def act(self):
        if "hello" in self.input_text:
            print("Responding with a greeting.")
        elif "goodbye" in self.input_text:
            print("Responding with a farewell.")
        else:
            print("Performing language processing tasks.")

# Create instances of the agents and demonstrate their behavior
print("Example 1: Simple AI agent")
simple_agent = SimpleAgent()
simple_agent.perceive("dirty")
simple_agent.act()
print()

print("Example 2: Reinforcement Learning agent")
rl_agent = RLAgent()
rl_agent.perceive("win")
rl_agent.act()
print()

print("Example 3: Natural Language Processing agent")
nlp_agent = NLPAgent()
nlp_agent.perceive("Hello, how are you?")
nlp_agent.act()
print()
