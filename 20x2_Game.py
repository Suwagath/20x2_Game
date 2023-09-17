# import necessary libraries
import random
from datetime import datetime
from prettytable import PrettyTable

# define constants
BOARD_SIZE = 20
NUM_PLAYERS = 2
PLAYER_SYMBOL = "X"
BLACK_HOLE_SYMBOL = "O"

# define the function to initialize the game board
def initialize_board():
    
    # create a 2-dimensional list with the given dimensions
    try:
        board = [[None] * BOARD_SIZE for _ in range(NUM_PLAYERS)]
        
        # initialize the first column of each player with the player symbol
        board[0][0] = PLAYER_SYMBOL
        board[1][0] = PLAYER_SYMBOL
        
        # initialize the rest of the board with black hole symbols at the designated positions
        for i in range(1, BOARD_SIZE):
            board[0][i] = "O" if i == 6 or i == 13 else " "
            board[1][i] = "O" if i == 6 or i == 13 else " "
            
        # return the initialized board
        return board
    
    # handle index errors
    except IndexError as e:
        print("Error:", e)
        raise


# define function to display the game board
def display_board(board):
    '''Function to display the game board'''
    # create a new pretty table
    table = PrettyTable()
    # define the field names for the table, including column headers and row labels
    field_names = [str(i+1) for i in range(BOARD_SIZE)]
    table.field_names = ['Player'] + field_names
    # add each player's row to the table
    table.add_row(['Human'] + board[0])
    table.add_row(['Computer'] + board[1])
    # print the table to the console
    print(table)

# define function to roll the dice
def roll_dice():
    '''Function to rill the dice'''
    try:
        # return a random integer between 1 and 6
        return random.randint(1, 6)
    except ValueError as e:
        # handle errors if the random integer cannot be generated
        print("Error:", e)
        raise

# define function to move the player on the board
def move_player(board, player, num_moves, player_stats, player_names):
    '''Function to move the player on the board'''
    try:
        # get the current position of the player
        current_pos = board[player].index(PLAYER_SYMBOL)
        # calculate the new position based on the number of moves
        new_pos = current_pos + num_moves
        # if the new position is outside the board, the player wins
        if new_pos >= BOARD_SIZE:
            print("Human player wins!" if player == 0 else "Computer player wins!")
            # update the player's game stats
            player_stats[player]['won_game'] = True
            # return True to indicate that the game is over
            return True
        # if the new position is a black hole, move the player back to position 1
        if new_pos == 6 or new_pos == 13:
            new_pos = 0
        # if the player steps into a black hole, move them back to position 1 and update their game stats
        if board[player][new_pos] == BLACK_HOLE_SYMBOL:
            if not player_stats[player]['has_hit_black_hole']:
                print(f"Player {player + 1} stepped into a black hole and goes back to position 1!")
                player_stats[player]['black_hole_hits'] += 1
                new_pos = 0
                player_stats[player]['has_hit_black_hole'] = True
            else:
                print(f"Player {player + 1} hit a black hole again but doesn't have to move back to position 1.")
        # update the player's position on the board
        board[player][current_pos] = " "
        board[player][new_pos] = PLAYER_SYMBOL if player == 0 else PLAYER_SYMBOL
        # update the player's game stats
        player_stats[player]['total_moves'] += num_moves
        player_stats[player]['current_position'] = new_pos
        # return False to indicate that the game is not over
        return False
    except IndexError:
        # handle errors if the player tries to make an invalid move
        print(f"Error: Invalid move for player {player_names[player]}. Please try again.")
        return False


# Define a function named play_game that starts the game
def play_game():
    '''Function to start the game'''
    # Print the game's welcome message and rules
    print("xxx Welcome to the board game! xxx")
    print("1. The goal of the game is to reach the end of the board before the other player does.")
    print("2. You must roll a 6 to start the game.")
    print("3. You can roll the dice to move your player. If you land on a black hole, you will be sent back to the beginning of the board.")
    print("4. The number of moves is equal to half of the dice value.")
    print("\n")
    # Explain the symbols used in the game
    print("Symbols: ")
    print("You ------> X")
    print("Computer ------> X")
    print("Black hole ------> O")
    print("\n")
    # Wait for the user to press Enter to start the game
    print("<<<<<<Press Enter to start the game...>>>>>>")
    input()

    # Initialize the board and player statistics
    board = initialize_board()
    current_player = None
    game_started = False
    player_names = ["Human", "Computer"]
    player_stats = [{'total_moves': 0, 'black_hole_hits': 0, 'won_game': False, 'current_position': 0},
                    {'total_moves': 0, 'black_hole_hits': 0, 'won_game': False, 'current_position': 0}]

    # Loop through the game until a player wins or the user quits
    while True:
        # Display the board
        display_board(board)
        
        # If the game has not started, roll the dice to determine who goes first
        if not game_started:
            dice_roll = roll_dice()
            if dice_roll == 6:
                game_started = True
                current_player = random.randint(0, 1)
                print("Game started! Current player:", player_names[current_player])
        # If the game has started, roll the dice and move the current player
        else:
            dice_roll = roll_dice()
            print("Dice roll:", dice_roll)
            num_moves = dice_roll // 2
            if move_player(board, current_player, num_moves, player_stats, player_names):
                break
            print(f"Current position of {player_names[current_player]}: {player_stats[current_player]['current_position']}")
            current_player = (current_player + 1) % NUM_PLAYERS
            print("Current player:", player_names[current_player])
        # Wait for the user to press Enter before continuing to the next turn
        input("Press Enter to continue...")

    # The game is over, so print the results to a file with the current date and time
    print("Game over!")
    now = datetime.now()
    filename = now.strftime("%Y_%m_%d_%H_%M") + ".txt"
    with open(filename, "w") as f:
        for i in range(NUM_PLAYERS):
            f.write(f"{player_names[i]}\n")
            f.write(f"Total moves: {player_stats[i]['total_moves']}\n")
            f.write(f"Black hole hits: {player_stats[i]['black_hole_hits']}\n")
            f.write("Won the game\n" if player_stats[i]['won_game'] else "Lost the game\n")
            f.write("----------------------------\n")


        # Define a loop that will continue to ask the user if they want to play again until they enter "N"

        while True:
            try:
                # Ask the user if they want to play again
                print("Do you want to play again? (Y/N)")
                user_input = input()
                # If the user enters "Y", call the play_game() function again to start a new game
                if user_input == "Y":
                    play_game()
                # If the user enters "N", break out of the loop
                elif user_input == "N":
                    break
                # If the user enters anything else, print an error message and ask them to try again
                else:
                    print("Invalid input. Please try again.")
            except KeyboardInterrupt:
                # If the user presses Ctrl+C, print a message and break out of the loop
                print("\n\nGame terminated by the user.")
            break


# Calling the function to start the 1st game
play_game()