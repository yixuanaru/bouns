import random

def initialize_board(length=30, penalty_probability=0.3):
    """Initialize the game board with safe and penalty squares."""
    board = ['_' if random.random() > penalty_probability else 'P' for _ in range(length)]
    return board

def roll_dice():
    """Simulate rolling a dice."""
    return random.randint(1, 6)

def move_player(position, roll, board):
    """Move the player and determine if they land on a penalty square."""
    new_position = position + roll
    if new_position >= len(board):
        new_position = len(board) - 1
    return new_position, board[new_position] == 'P'

def print_board(board, player_a_pos, player_b_pos, penalty_a, penalty_b):
    """Print the current state of the board with player positions."""
    display = list(board)
    
    if player_a_pos == player_b_pos:
        display[player_a_pos] = 'X' if not penalty_a and not penalty_b else 'x'
    else:
        display[player_a_pos] = 'A' if not penalty_a else 'a'
        display[player_b_pos] = 'B' if not penalty_b else 'b'
    
    print("Board: ", ''.join(display))

def game():
    board = initialize_board()
    player_a_pos = 0
    player_b_pos = 0
    penalty_a = False
    penalty_b = False
    game_over = False

    while not game_over:
        if not penalty_a:
            roll_a = roll_dice()
            player_a_pos, penalty_a = move_player(player_a_pos, roll_a, board)
        
        if not penalty_b:
            roll_b = roll_dice()
            player_b_pos, penalty_b = move_player(player_b_pos, roll_b, board)

        print_board(board, player_a_pos, player_b_pos, penalty_a, penalty_b)

        if player_a_pos == len(board) - 1 or player_b_pos == len(board) - 1:
            game_over = True

        if player_a_pos == len(board) - 1:
            penalty_a = False
        
        if player_b_pos == len(board) - 1:
            penalty_b = False

    print("Game Over!")
    print("Final Board with Penalties:")
    final_board = ['P' if cell == 'P' else '_' for cell in board]
    print("Board: ", ''.join(final_board))
    
    if player_a_pos == len(board) - 1 and player_b_pos == len(board) - 1:
        print("Both players win!")
    elif player_a_pos == len(board) - 1:
        print("Player A wins!")
    elif player_b_pos == len(board) - 1:
        print("Player B wins!")

# Start the game
game()
