import boardlayout
import move_player
from datetime import datetime
import dice, random

def play_game():
    # Introduction to the game and its rules
    print("xxx Welcome to the board game! xxx")
    print("1. The goal of the game is to reach the end of the board before the other player does.")
    print("2. You must roll a 6 to start the game.")
    print("3. You can roll the dice to move your player. If you land on a black hole, you will be sent back to the beginning of the board.")
    print("4. The number of moves is equal to half of the dice value.")
    print("\n")
    print("Symbols: ")
    print("You ------> X")
    print("Computer ------> X")
    print("Black hole ------> O")
    print("\n")
    # Prompt the user to start the game
    print("<<<<<<Press Enter to start the game...>>>>>>")
    input()
    # Initialize the board and player stats
    board = boardlayout.initialize_board()
    current_player = None
    game_started = False
    player_names = ["Human", "Computer"]
    player_stats = [{'total_moves': 0, 'black_hole_hits': 0, 'won_game': False, 'current_position': 0},
                    {'total_moves': 0, 'black_hole_hits': 0, 'won_game': False, 'current_position': 0}]
    # Start the game loop
    while True:
        # Display the current state of the board
        boardlayout.display_board(board)
        # Check if the game has started yet
        if not game_started:
            # Roll the dice to start the game
            dice_roll = dice.roll_dice()
            if dice_roll == 6:
                # Start the game if the dice roll is a 6
                game_started = True
                current_player = random.randint(0, 1)
                print("Game started! Current player:", player_names[current_player])
        else:
            # Roll the dice for the current player's turn
            dice_roll = dice.roll_dice()
            print("Dice roll:", dice_roll)
            # Calculate the number of moves based on the dice roll
            num_moves = dice_roll // 2
            # Move the player based on the number of moves
            if move_player(board, current_player, num_moves, player_stats, player_names):
                # End the game if a player has won
                break
            print(f"Current position of {player_names[current_player]}: {player_stats[current_player]['current_position']}")
            # Switch to the other player's turn
            current_player = (current_player + 1) % board.NUM_PLAYERS
            print("Current player:", player_names[current_player])
        # Wait for the user to continue the game
        input("Press Enter to continue...")
    # Game over
    print("Game over!")
    # Save the player stats to a file with a timestamp as the filename
    now = datetime.now()
    filename = now.strftime("%Y_%m_%d_%H_%M") + ".txt"
    with open(filename, "w") as f:
        for i in range(boardlayout.NUM_PLAYERS):
            f.write(f"{player_names[i]}\n")
            f.write(f"Total moves: {player_stats[i]['total_moves']}\n")
            f.write(f"Black hole hits: {player_stats[i]['black_hole_hits']}\n")
            f.write("Won the game\n" if player_stats[i]['won_game'] else "Lost the game\n")
            f.write("----------------------------\n")

            
# Define a loop that will continue to ask the user if they want to play again until they enter "N"
while True:
    # Ask the user if they want to play again
    print("Do you want to play again? (Y/N)")
    user_input = input()
    
    # If the user enters "Y", call the play_game() function again to start a new game
    if user_input == "Y":
        play_game()
        
    # If the user enters "N", break out of the loop to end the program
    elif user_input == "N":
        break
        
    # If the user enters anything other than "Y" or "N", print an error message and continue the loop
    else:
        print("Invalid input. Please try again.")
        
# Call the play_game() function to start the first game
play_game()
