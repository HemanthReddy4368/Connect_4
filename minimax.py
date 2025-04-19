from copy import deepcopy
from random import choice

class Minimax:
    def eva_win(self, window, p):
        s = 0
        o_p = 1 if p == 2 else 2

        if window.count(p) == 4:
            s += 100
        elif window.count(p) == 3 and window.count(0) == 1:
            s += 5
        elif window.count(p) == 2 and window.count(0) == 2:
            s += 2

        if window.count(o_p) == 3 and window.count(0) == 1:
            s -= 4

        return s

    def eval_position(self, board):
        score = 0
        piece = 1
        c_a = [int(i) for i in list(board.board[:, board.c//2])]
        c_c = c_a.count(piece)
        score += c_c * 3
        r = 0
        while r < board.r:
            r_a = [int(i) for i in list(board.board[r,:])]
            c = 0
            while c < board.c-3:
                w = r_a[c:c+4]
                score += self.eva_win(w, piece)
                c += 1
            r += 1

        c = 0
        while c < board.c:
            c_array = [int(i) for i in list(board.board[:,c])]
            r = 0
            while r < board.r-3:
                w = c_array[r:r+4]
                score += self.eva_win(w, piece)
                r += 1
            c += 1

        r = 0
        while r < board.r-3:
            c = 0
            while c < board.c-3:
                win = [board.board[r+i][c+i] for i in range(4)]
                score += self.eva_win(win, piece)
                win = [board.board[r+3-i][c+i] for i in range(4)]
                score += self.eva_win(win, piece)
                c += 1
            r += 1

        return score

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        v_moves = board.get_legal_moves()
        i_tem = board.winner_checker(1) or board.winner_checker(2) or len(v_moves) == 0

        if depth == 0 or i_tem:
            if i_tem:
                if board.winner_checker(1):
                    return (None, 100000000000000)
                elif board.winner_checker(2):
                    return (None, -100000000000000)
                else:
                    return (None, 0)
            else:
                return (None, self.eval_position(board))

        if maximizing_player:
            value = float('-inf')
            v_moves_list = list(v_moves)
            column = choice(v_moves_list)

            i = 0
            while i < len(v_moves_list):
                c = v_moves_list[i]
                row = board.get_blank_rows(c)
                t_board = deepcopy(board)
                t_board.next_move(row, c, 1)
                n_score = self.minimax(t_board, depth-1, alpha, beta, False)[1]
                if n_score > value:
                    value = n_score
                    column = c
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
                i += 1
            return column, value
        else:
            value = float('inf')
            column = choice(list(v_moves))
            v_moves_list = list(v_moves)
            i = 0
            while i < len(v_moves_list):
                c = v_moves_list[i]
                row = board.get_blank_rows(c)
                t_board = deepcopy(board)
                t_board.next_move(row, c, 2)
                n_score = self.minimax(t_board, depth-1, alpha, beta, True)[1]
                if n_score < value:
                    value = n_score
                    column = c
                beta = min(beta, value)
                if alpha >= beta:
                    break
                i += 1
            return column, value