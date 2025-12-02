"""
chatbot.py
Skeleton code for the Python Chatbot Project
Follows required project structure and class design
"""

import random

class Chatbot:
    """A simple command-line chatbot framework."""

def __init__(self, name):
    """Initialize bot name, memory storage, and active flag."""
    self.name = name
    self.memory = {} # Dictionary to store user data
    self.active = True # Controls conversation loop

def greet_user(self):
    """Greet the user and collect/store their name."""
    # TODO: Print greeting
    # TODO: Ask for user's name
    # TODO: Store name in memory dictionary
    # TODO: Acknowledge user by name
    pass

def get_response(self, user_input):
    """
        Process user input and return an appropriate response.
        Should handle:
        hi → random greeting
        how are you → random status message
        bye → farewell
        name → recall stored user name
        color → ask and store favorite color
        favorite → recall favorite color
        exit → set active=False
    """
    # TODO: Clean user_input (lowercase, strip punctuation)
    # TODO: Write conditional logic for supported commands
    # TODO: Return a chatbot response string
    pass

def chat(self):
    """Main conversation loop."""
    # TODO: Start loop while self.active is True
    # TODO: Prompt user for input
    # TODO: Call get_response()
    # TODO: Print bot response with prefix (e.g., PyBot: ...)
    pass

def main():
    """Create a chatbot instance and begin conversation."""
    # TODO: Instantiate Chatbot with a bot name
    # TODO: Call greet_user()
    # TODO: Start chat loop
    pass

if __name__ == "__main__":
    main()
