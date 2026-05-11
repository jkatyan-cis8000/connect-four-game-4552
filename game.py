import board


def check_horizontal_win(board, row, col):
    """Check for a horizontal win starting from the last placed disc."""
    player = board[row][col]
    if player == board.EMPTY:
        return False
    
    count = 0
    for c in range(board.BOARD_COLS):
        if board[row][c] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False


def check_vertical_win(board, row, col):
    """Check for a vertical win starting from the last placed disc."""
    player = board[row][col]
    if player == board.EMPTY:
        return False
    
    count = 0
    for r in range(row, -1, -1):
        if board[r][col] == player:
            count += 1
            if count == 4:
                return True
        else:
            break
    return False


def check_diagonal_win(board, row, col):
    """Check for a diagonal win in either direction."""
    player = board[row][col]
    if player == board.EMPTY:
        return False
    
    if check_diagonal_positive(board, row, col, player):
        return True
    if check_diagonal_negative(board, row, col, player):
        return True
    return False


def check_diagonal_positive(board, row, col, player):
    """Check diagonal from top-left to bottom-right."""
    count = 0
    r, c = row, col
    while r >= 0 and c >= 0 and board[r][c] == player:
        count += 1
        r -= 1
        c -= 1
    
    r, c = row + 1, col + 1
    while r < board.BOARD_ROWS and c < board.BOARD_COLS and board[r][c] == player:
        count += 1
        r += 1
        c += 1
    
    return count >= 4


def check_diagonal_negative(board, row, col, player):
    """Check diagonal from bottom-left to top-right."""
    count = 0
    r, c = row, col
    while r < board.BOARD_ROWS and c >= 0 and board[r][c] == player:
        count += 1
        r += 1
        c -= 1
    
    r, c = row - 1, col + 1
    while r >= 0 and c < board.BOARD_COLS and board[r][c] == player:
        count += 1
        r -= 1
        c += 1
    
    return count >= 4


def is_board_full(board):
    """Check if the board is full (draw condition)."""
    for col in range(board.BOARD_COLS):
        if board[0][col] == board.EMPTY:
            return False
    return True


def check_win(board, row, col):
    """Check if there's a win starting from the last placed disc."""
    if check_horizontal_win(board, row, col):
        return True
    if check_vertical_win(board, row, col):
        return True
    if check_diagonal_win(board, row, col):
        return True
    return False
