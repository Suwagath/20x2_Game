# Import necessary variables from the 'boardlayout' module
from boardlayout import PLAYER_SYMBOL, BOARD_SIZE, BLACK_HOLE_SYMBOL

# Declare all the variables used in this module
player_stats = []
player_names = []
board = []
player = 0
num_moves = 0
current_pos = 0
new_pos = 0
num_moves = 0

# Define a function named 'move_player()' that takes in five arguments - 'board', 'player', 'num_moves', 'player_stats', and 'player_names'
def move_player(board, player, num_moves, player_stats, player_names):
    try:
        # Get the current position of the player on the board
        current_pos = board[player].index(PLAYER_SYMBOL)
        # Calculate the new position of the player based on the number of moves
        new_pos = current_pos + num_moves
        # Check if the player has reached the end of the board
        if new_pos >= BOARD_SIZE:
            # If yes, print the winner and update the player's stats
            print("Human player wins!" if player == 0 else "Computer player wins!")
            player_stats[player]['won_game'] = True
            return True
        # Check if the player has landed on a special tile (6 or 13)
        if new_pos == 6 or new_pos == 13:
            # If yes, move the player back to position 1
            new_pos = 0
        # Check if the player has landed on a black hole
        if board[player][new_pos] == BLACK_HOLE_SYMBOL:
            # If yes, check if the player has hit a black hole before
            if not player_stats[player]['has_hit_black_hole']:
                # If not, move the player back to position 1 and update the player's stats
                print(f"Player {player + 1} stepped into a black hole and goes back to position 1!")
                player_stats[player]['black_hole_hits'] += 1
                new_pos = 0
                player_stats[player]['has_hit_black_hole'] = True
            else:
                # If yes, print a message indicating that the player has hit a black hole again but doesn't have to move back to position 1
                print(f"Player {player + 1} hit a black hole again but doesn't have to move back to position 1.")
        # Update the board by moving the player's symbol from the current position to the new position
        board[player][current_pos] = " "
        board[player][new_pos] = PLAYER_SYMBOL if player == 0 else PLAYER_SYMBOL
        # Update the player's stats
        player_stats[player]['total_moves'] += num_moves
        player_stats[player]['current_position'] = new_pos
        # Return False indicating that the move was successful
        return False
    except IndexError:
        # If an error occurs, print an error message and return False indicating that the move was not successful
        print(f"Error: Invalid move for player {player_names[player]}. Please try again.")
        return False
