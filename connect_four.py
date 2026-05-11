from board import create_board, display_board, drop_disc, PLAYER_1, PLAYER_2, EMPTY

BOARD_COLS = 7


def check_win(board, player):
    """Check if the given player has won."""
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True

    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True

    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True

    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True

    return False


def is_board_full(board):
    """Check if the board is full."""
    for row in range(6):
        for col in range(7):
            if board[row][col] == EMPTY:
                return False
    return True


def get_valid_input():
    """Get valid column input from player."""
    while True:
        try:
            col = int(input("Enter column (1-7): ")) - 1
            if 0 <= col < 7:
                return col
            else:
                print("Invalid input. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")


def main():
    board = create_board()
    current_player = PLAYER_1

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")

        col = get_valid_input()

        if drop_disc(board, col, current_player) == -1:
            print("Column is full. Try again.")
            continue

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        current_player = PLAYER_2 if current_player == PLAYER_1 else PLAYER_1


if __name__ == "__main__":
    main()
