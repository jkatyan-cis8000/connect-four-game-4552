import unittest
from board import create_board, display_board, drop_disc, EMPTY, PLAYER_1, PLAYER_2


class TestBoard(unittest.TestCase):
    
    def test_create_board(self):
        """Test that create_board creates a 6x7 board filled with zeros."""
        board = create_board()
        self.assertEqual(len(board), 6)
        for row in board:
            self.assertEqual(len(row), 7)
            for cell in row:
                self.assertEqual(cell, EMPTY)
    
    def test_drop_disc_first_row(self):
        """Test dropping a disc in an empty column."""
        board = create_board()
        row = drop_disc(board, 0, PLAYER_1)
        self.assertEqual(row, 5)
        self.assertEqual(board[5][0], PLAYER_1)
        for i in range(4, -1, -1):
            self.assertEqual(board[i][0], EMPTY)
    
    def test_drop_disc_multiple_rows(self):
        """Test dropping discs in the same column."""
        board = create_board()
        row1 = drop_disc(board, 0, PLAYER_1)
        row2 = drop_disc(board, 0, PLAYER_2)
        row3 = drop_disc(board, 0, PLAYER_1)
        self.assertEqual(row1, 5)
        self.assertEqual(row2, 4)
        self.assertEqual(row3, 3)
        self.assertEqual(board[5][0], PLAYER_1)
        self.assertEqual(board[4][0], PLAYER_2)
        self.assertEqual(board[3][0], PLAYER_1)
    
    def test_drop_disc_different_columns(self):
        """Test dropping discs in different columns."""
        board = create_board()
        row1 = drop_disc(board, 2, PLAYER_1)
        row2 = drop_disc(board, 4, PLAYER_2)
        row3 = drop_disc(board, 6, PLAYER_1)
        self.assertEqual(row1, 5)
        self.assertEqual(row2, 5)
        self.assertEqual(row3, 5)
        self.assertEqual(board[5][2], PLAYER_1)
        self.assertEqual(board[5][4], PLAYER_2)
        self.assertEqual(board[5][6], PLAYER_1)
    
    def test_drop_disc_column_full(self):
        """Test dropping a disc in a full column."""
        board = create_board()
        for _ in range(6):
            drop_disc(board, 0, PLAYER_1)
        row = drop_disc(board, 0, PLAYER_2)
        self.assertEqual(row, -1)
        for row_idx in range(6):
            self.assertEqual(board[row_idx][0], PLAYER_1)
    
    def test_board_state_after_multiple_drops(self):
        """Test board state after multiple discs dropped in various columns."""
        board = create_board()
        drop_disc(board, 3, PLAYER_1)
        drop_disc(board, 3, PLAYER_2)
        drop_disc(board, 4, PLAYER_1)
        drop_disc(board, 4, PLAYER_1)
        drop_disc(board, 4, PLAYER_2)
        
        self.assertEqual(board[5][3], PLAYER_1)
        self.assertEqual(board[4][3], PLAYER_2)
        self.assertEqual(board[5][4], PLAYER_1)
        self.assertEqual(board[4][4], PLAYER_1)
        self.assertEqual(board[3][4], PLAYER_2)


if __name__ == '__main__':
    unittest.main()
