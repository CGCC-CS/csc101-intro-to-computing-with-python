import random

# Function for a number guessing game
def guess_number(min_guess, max_guess, max_attempts):
    """
    Runs a number guessing game where the player tries to guess a random number.
    
    The player has a limited number of attempts to guess a randomly generated
    number between min_guess and max_guess. Provides feedback on whether each
    guess is too high, too low, or correct.

    Args:
        min_guess (int): The minimum possible guess.
        max_guess (int): The maximum possible guess.
        max_attempts (int): The maximum number of attempts allowed.

    Returns:
        None: Prints game results directly to console
    """
    secret = random.randint(min_guess, max_guess)  # Pick random number in range
    remaining_attempts = max_attempts  # Number of allowed guesses
    
    print(f"Guess the number between {min_guess} and {max_guess}! You have {max_attempts} tries.")
    
    # Loop until the player runs out of attempts
    while remaining_attempts > 0:
        guess = int(input("Enter your guess: "))
        remaining_attempts -= 1
        
        if guess == secret:
            print("You win!")
            return
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")
        print(f"{remaining_attempts} tries left.")
    
    print(f"Game over! The number was {secret}.")

def main():
    print("\nLet's play a guessing game!")
    guess_number(1,10,3)

if __name__ == "__main__":
    main()