import numpy as np
import random
import pickle

class QLearning:
    def __init__(self, alpha=0.1, gamma=0.99, epsilon=0.3):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.visit_counts = {}
        self.min_epsilon = 0.01
        self.epsilon_decay = 0.9999

    def get_sta(self, brd):
        state_parts = []

        for r in range(brd.r):
            rw_state = ''.join(str(int(brd.board[r][c])) for c in range(brd.c))
            state_parts.append(rw_state)

        thrts = self.get_thrts(brd)
        state_parts.append(thrts)

        c_control = ''.join(str(int(brd.board[r][brd.c//2])) for r in range(brd.r))
        state_parts.append(c_control)

        return '|'.join(state_parts)

    def get_thrts(self, board):
        thrts = []
        for ply in [1, 2]:

            for r in range(board.r):
                for c in range(board.c - 3):
                    win = [int(board.board[r][c+i]) for i in range(4)]
                    if win.count(ply) == 3 and win.count(0) == 1:
                        thrts.append(f"h{r}{c}{ply}")

            for r in range(board.r - 3):
                for c in range(board.c):
                    win = [int(board.board[r+i][c]) for i in range(4)]
                    if win.count(ply) == 3 and win.count(0) == 1:
                        thrts.append(f"v{r}{c}{ply}")

        return '_'.join(sorted(thrts)) if thrts else 'no_threats'

    def get_q_value(self, state, action):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(7) + 0.2
            self.visit_counts[state] = np.zeros(7)
        return self.q_table[state][action]

    def choose_action(self, board, valid_moves):
        state = self.get_sta(board)

        if random.random() < self.epsilon:
            strategic_moves = self.get_str_moves(board, valid_moves)
            if strategic_moves:
                return random.choice(strategic_moves)
            return random.choice(list(valid_moves))

        if state not in self.q_table:
            return random.choice(list(valid_moves))

        ucb_values = []
        total_visits = sum(self.visit_counts[state]) + len(valid_moves)

        for action in valid_moves:
            q_value = self.q_table[state][action]
            visit_count = self.visit_counts[state][action]
            exploration_term = np.sqrt(2 * np.log(total_visits) / (visit_count + 1))
            ucb_values.append((action, q_value + exploration_term))

        return max(ucb_values, key=lambda x: x[1])[0]

    def get_str_moves(self, board, valid_moves):
        strategic_moves = []

        for c in valid_moves:
            r = board.get_blank_rows(c)
            if r is not None:
                board.board[r][c] = 2
                if board.winner_checker(2):
                    strategic_moves.append(c)
                board.board[r][c] = 0

                board.board[r][c] = 1
                if board.winner_checker(1):
                    strategic_moves.append(c)
                board.board[r][c] = 0

        return strategic_moves if strategic_moves else list(valid_moves)

    def learn(self, state, action, reward, new_state, done):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(7) + 0.2
            self.visit_counts[state] = np.zeros(7)
        if new_state not in self.q_table:
            self.q_table[new_state] = np.zeros(7) + 0.2
            self.visit_counts[new_state] = np.zeros(7)

        self.visit_counts[state][action] += 1

        eff_alpha = self.alpha / (1 + self.visit_counts[state][action] * 0.1)

        current_q = self.q_table[state][action]

        if done:
            new_q = current_q + eff_alpha * (reward - current_q)
        else:
            max_future_q = max(self.q_table[new_state])
            new_q = current_q + eff_alpha * (reward + self.gamma * max_future_q - current_q)

        self.q_table[state][action] = new_q

        self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay)

    def save_q_table(self, filename='q_table.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(dict(self.q_table), f)

    def load_q_table(self, filename='q_table.pkl'):
        try:
            with open(filename, 'rb') as f:
                self.q_table = pickle.load(f)
            print(f"Loaded Q-table from {filename}")
        except FileNotFoundError:
            self.q_table = {}
            print("No existing Q-table found. So, Starting fresh.")