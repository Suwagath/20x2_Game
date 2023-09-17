# Import the 'random' module for generating random numbers
import random

# Define a function named 'roll_dice()' that takes no arguments
def roll_dice():
    try:
        # Use the 'random.randint()' function to generate a random integer between 1 and 6
        return random.randint(1, 6)
    except ValueError as e:
        # If an error occurs while generating the random number, print the error message and raise the exception
        print("Error:", e)
        raise
