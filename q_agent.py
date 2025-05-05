from q_learning import QLearning
from copy import deepcopy

class QAgent:
    def __init__(self, a=0.5, g=0.9, e=0.1):
        self.q_learner = QLearning(alpha=a, gamma=g, epsilon=e)
        self.last_board = None
        self.last_move = None

    def get_move(self, board):
        valid_moves = board.get_legal_moves()
        if not valid_moves:
            return None

        self.last_board = deepcopy(board)
        self.last_move = self.q_learner.choose_action(board, valid_moves)
        return self.last_move

    def learn_from_result(self, new_board, reward, done):
        if self.last_board and self.last_move is not None:
            self.q_learner.learn(self.last_board, self.last_move, reward, new_board, done)
            self.last_board = None
            self.last_move = None

    def save_model(self, filename='q_table.pkl'):
        self.q_learner.save_q_table(filename)

    def load_model(self, filename='q_table.pkl'):
        self.q_learner.load_q_table(filename)