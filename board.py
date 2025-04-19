import numpy as np

class Board:
    def __init__(self, r=6, c=7):
        self.r = r
        self.c = c
        self.board = np.zeros((r, c))

    def next_move(self, r, c, p):
        self.board[r][c] = p

    def is_move_valid(self, c):
        return 0 <= c < self.c and self.board[self.r-1][c] == 0

    def get_blank_rows(self, c):
        for r in range(self.r):
            if self.board[r][c] == 0:
                return r
        return None

    def get_legal_moves(self):
        v_moves = set()
        for c in range(self.c):
            if self.is_move_valid(c):
                v_moves.add(c)
        return v_moves

    def winner_checker(self, p):
        for r in range(self.r):
            for c in range(self.c-3):
                if all(self.board[r][c+i] == p for i in range(4)):
                    return True

        for r in range(self.r-3):
            for c in range(self.c):
                if all(self.board[r+i][c] == p for i in range(4)):
                    return True

        for r in range(self.r-3):
            for c in range(self.c-3):
                if all(self.board[r+i][c+i] == p for i in range(4)):
                    return True

        for r in range(3, self.r):
            for c in range(self.c-3):
                if all(self.board[r-i][c+i] == p for i in range(4)):
                    return True
        return False

    def is_full(self):
        return len(self.get_legal_moves()) == 0

    def print_board(self):
        print(np.flip(self.board, 0))