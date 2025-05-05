from board import Board
from normal_player import NormalPlayer
from q_agent import QAgent
import time
import random

def train_q_learning(episodes=100000):
    q_agent = QAgent(a=0.5, g=0.9, e=0.3)
    normal_player = NormalPlayer()

    wi = 0
    drw = 0

    for episode in range(episodes):
        boa = Board()
        do = False
        tur = 0

        while not do:
            if tur == 0:
                co = normal_player.get_move(boa)
                if co is not None:
                    ro = boa.get_blank_rows(co)
                    boa.next_move(ro, co, 1)

                    if boa.winner_checker(1):
                        q_agent.learn_from_result(boa, -1, True)
                        do = True
                    elif boa.is_full():
                        q_agent.learn_from_result(boa, 0.5, True)
                        drw += 1
                        do = True
                    else:
                        reward = 0
                        if has_three_in_row(boa, 1):
                            reward -= 0.3
                        q_agent.learn_from_result(boa, reward, False)
            else:
                co = q_agent.get_move(boa)
                if co is not None:
                    ro = boa.get_blank_rows(co)
                    boa.next_move(ro, co, 2)

                    if boa.winner_checker(2):
                        q_agent.learn_from_result(boa, 1, True)
                        wi += 1
                        do = True
                    elif boa.is_full():
                        q_agent.learn_from_result(boa, 0.5, True)
                        drw += 1
                        do = True
                    else:
                        reward = 0
                        if has_three_in_row(boa, 2):
                            reward += 0.3
                        q_agent.learn_from_result(boa, reward, False)

            tur = 1 - tur

        if (episode + 1) % 100 == 0:
            win_rate = (wi / (episode + 1)) * 100
            draw_rate = (drw / (episode + 1)) * 100
            print(f"Episode {episode + 1}/{episodes}")
            print(f"Win Rate: {win_rate:.2f}%")
            print(f"Draw Rate: {draw_rate:.2f}%")
            print(f"Loss Rate: {100 - win_rate - draw_rate:.2f}%")
            print("------------------------")

    q_agent.save_model()
    print("\nFinal Statistics:")
    print(f"Total Wins: {wi}")
    print(f"Total Draws: {drw}")
    print(f"Total Losses: {episodes - wi - drw}")
    print(f"Win Rate: {(wi/episodes)*100:.2f}%")
    print("Training completed. Q-table saved.")

def has_three_in_row(boa, player):
    for r in range(boa.r):
        for c in range(boa.c-2):
            if all(boa.board[r][c+i] == player for i in range(3)):
                return True
    for r in range(boa.r-2):
        for c in range(boa.c):
            if all(boa.board[r+i][c] == player for i in range(3)):
                return True
    return False

if __name__ == "__main__":
    start_time = time.time()
    train_q_learning(episodes=100000)
    print(f"Training took {time.time() - start_time:.2f} seconds")