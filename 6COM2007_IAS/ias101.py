# Intelligent Adaptive Systems - Introduction

# Einstein's Definition of Intelligence
intelligence_definition = "Intelligence is the ability to adapt to change."

# Simple Examples of Intelligent Adaptive Systems

# Example 1: Temperature Control System
class TemperatureControlSystem:
    def __init__(self, target_temperature):
        self.target_temperature = target_temperature
    
    def adjust_temperature(self, current_temperature):
        if current_temperature < self.target_temperature:
            print("Increasing temperature...")
        elif current_temperature > self.target_temperature:
            print("Decreasing temperature...")
        else:
            print("Temperature is optimal.")

# Example 2: Spam Email Filter
class SpamEmailFilter:
    def __init__(self, spam_keywords):
        self.spam_keywords = spam_keywords
    
    def is_spam(self, email_content):
        for keyword in self.spam_keywords:
            if keyword in email_content:
                return True
        return False

# Example 3: Autonomous Robot
class AutonomousRobot:
    def __init__(self, initial_position):
        self.position = initial_position
    
    def move(self, direction):
        if direction == "forward":
            self.position += 1
        elif direction == "backward":
            self.position -= 1
        else:
            print("Invalid direction.")

# Main program
if __name__ == "__main__":
    # Create instances of the intelligent adaptive systems
    temperature_system = TemperatureControlSystem(25)
    spam_filter = SpamEmailFilter(["buy now", "discount"])
    robot = AutonomousRobot(0)

    # Test the systems
    print()
    print("Einstein's definition of intelligence:")
    print(intelligence_definition)
    print()
    
    print("Example 1: Temperature Control System")
    temperature_system.adjust_temperature(28)
    print()
    
    print("Example 2: Spam Email Filter")
    print(spam_filter.is_spam("Get a discount on our products!"))
    print()
    
    print("Example 3: Autonomous Robot")
    robot.move("forward")
    print(robot.position)
    print()
