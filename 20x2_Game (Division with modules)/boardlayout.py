# Import the PrettyTable library to display the game board in a table format
from prettytable import PrettyTable

# Define the board size, number of players, and the symbols for the player and black holes
BOARD_SIZE = 20
NUM_PLAYERS = 2
PLAYER_SYMBOL = "X"
BLACK_HOLE_SYMBOL = "O"

# Define a function to initialize the game board
def initialize_board():

    # Try to create a 2D list with dimensions NUM_PLAYERS x BOARD_SIZE
    try:
        board = [[None] * BOARD_SIZE for _ in range(NUM_PLAYERS)]
        
        # Set the starting positions for each player
        board[0][0] = PLAYER_SYMBOL
        board[1][0] = PLAYER_SYMBOL
        
        # Set the black holes on the board at positions 6 and 13 for each player
        for i in range(1, BOARD_SIZE):
            board[0][i] = "O" if i == 6 or i == 13 else " "
            board[1][i] = "O" if i == 6 or i == 13 else " "
        
        # Return the initialized game board
        return board
    
    # Catch any index errors and print an error message
    except IndexError as e:
        print("Error:", e)
        raise

# Define a function to display the game board
def display_board(board):
    
    # Create a new PrettyTable instance to display the board
    table = PrettyTable()
    
    # Set the field names for the table (the column headers)
    field_names = [str(i+1) for i in range(BOARD_SIZE)]
    table.field_names = ['Player'] + field_names
    
    # Add a row to the table for each player, with their name and their corresponding row on the board
    table.add_row(['Human'] + board[0])
    table.add_row(['Computer'] + board[1])
    
    # Print the table to the console
    print(table)
