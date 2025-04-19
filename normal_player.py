from copy import deepcopy
from random import choice

class NormalPlayer:
    def get_move(self, board):
        valid_moves = list(board.get_legal_moves())
        i = 0
        while i < len(valid_moves):
            c = valid_moves[i]
            r = board.get_blank_rows(c)
            t_board = deepcopy(board)
            t_board.next_move(r, c, 2)
            if t_board.winner_checker(2):
                return c
            i += 1

        i = 0
        while i < len(valid_moves):
            c = valid_moves[i]
            r = board.get_blank_rows(c)
            t_board = deepcopy(board)
            t_board.next_move(r, c, 1)
            if t_board.winner_checker(1):
                return c
            i += 1

        return choice(valid_moves)