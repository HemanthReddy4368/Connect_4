# q_learning.py
import numpy as np
import random
import pickle

class QLearning:
    def __init__(self, alpha=0.5, gamma=0.9, epsilon=0.1):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q_value(self, state, action):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(7)
        return self.q_table[state][action]

    def choose_action(self, board, valid_moves):
        state = self._get_state(board)

        if random.random() < self.epsilon:
            return random.choice(list(valid_moves))
        else:
            q_values = [self.get_q_value(state, a) for a in range(7)]
            max_q = max([q_values[a] for a in valid_moves])
            best_actions = [a for a in valid_moves if q_values[a] == max_q]
            return random.choice(best_actions)

    def learn(self, board, action, reward, new_board, done):
        state = self._get_state(board)
        new_state = self._get_state(new_board)

        if state not in self.q_table:
            self.q_table[state] = np.zeros(7)
        if new_state not in self.q_table:
            self.q_table[new_state] = np.zeros(7)

        current_q = self.q_table[state][action]
        max_next_q = 0 if done else max(self.q_table[new_state])
        new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
        self.q_table[state][action] = new_q

    def _get_state(self, board):
        return ''.join(str(int(cell)) for row in board.board for cell in row)

    def save_q_table(self, filename='q_table.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self.q_table, f)

    def load_q_table(self, filename='q_table.pkl'):
        try:
            with open(filename, 'rb') as f:
                self.q_table = pickle.load(f)
        except FileNotFoundError:
            self.q_table = {}