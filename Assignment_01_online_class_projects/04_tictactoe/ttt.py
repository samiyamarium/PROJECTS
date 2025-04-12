# Tic Tac Toe - 2 Player Game

# Initialize the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a winner
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for cond in win_conditions:
        if all(board[i] == player for i in cond):
            return True
    return False

# Function to check if the board is full
def is_draw():
    return ' ' not in board

# Main game loop
def play_game():
    current_player = 'X'

    while True:
        print_board()
        move = input(f"Player {current_player}, enter your move (1-9): ")

        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Choose a number between 1 and 9.")
            continue

        move = int(move) - 1

        if board[move] != ' ':
            print("That spot is already taken. Try again.")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins! 🎉")
            break

        if is_draw():
            print_board()
            print("It's a draw! 🤝")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
play_game()

