BOARD_ROWS = 6
BOARD_COLS = 7
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2


def create_board():
    """Create a 6x7 game board initialized with empty cells."""
    board = [[EMPTY for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    return board


def display_board(board):
    """Display the current state of the board."""
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == EMPTY:
                print(" ", end="")
            elif cell == PLAYER_1:
                print("X", end="")
            elif cell == PLAYER_2:
                print("O", end="")
            print("|", end="")
        print()
    print("-" * 15)


def drop_disc(board, col, player):
    """Drop a disc in the specified column for the given player.
    
    Returns the row where the disc was placed, or -1 if column is full.
    """
    for row in range(BOARD_ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return row
    return -1
