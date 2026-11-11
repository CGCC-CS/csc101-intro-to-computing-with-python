"""
chatbot.py
Starter code for the CSC 101 Final Project: Chatbot.

Fill in every TODO. Keep the class name, method names, and parameters
shown here. You may add helper methods of your own.
"""

import random


class Chatbot:
    """A simple command-line chatbot."""

    def __init__(self, name):
        """Set the bot's name, an empty memory, and the active flag."""
        self.name = name
        self.memory = {}    # User data, e.g. {"name": "Ana", "color": "teal"}
        self.active = True  # The chat loop runs while this is True

    def greet_user(self):
        """Introduce the bot, ask for the user's name, and store it."""
        # TODO: Print an introduction that includes self.name
        # TODO: Ask for the user's name; ask again if the answer is blank
        # TODO: Store the name in self.memory["name"]
        # TODO: Greet the user by name
        pass

    def get_response(self, user_input):
        """
        Return the bot's reply to user_input as a string.

        Commands (matched after the input is cleaned):
            hi / hello    -> random greeting
            how are you   -> random status message
            name          -> recall the user's name
            color         -> ask for and store the favorite color
            favorite      -> recall the favorite color
                             (or say it has not been set yet)
            bye / exit    -> say goodbye and set self.active to False
            your 2 own    -> commands you design
            anything else -> fallback message
        """
        # TODO: Clean user_input: make it lowercase, then strip spaces
        #       and punctuation from both ends
        # TODO: Use if/elif/else to choose a reply for each command
        # TODO: Return the reply (print it in chat(), not here)
        pass

    def chat(self):
        """Run the conversation loop until the user says bye or exit."""
        # TODO: Loop while self.active is True
        # TODO: Read the user's input with the prompt "You: "
        # TODO: Call self.get_response() with that input
        # TODO: Print the reply with the bot's name as a prefix,
        #       e.g. "PyBot: Hello!"
        pass


def main():
    """Create a chatbot and start the conversation."""
    # TODO: Create a Chatbot object with a bot name, e.g. "PyBot"
    # TODO: Call greet_user()
    # TODO: Call chat()
    pass


if __name__ == "__main__":
    main()
