import time
from board import Board
from normal_player import NormalPlayer
from q_agent import QAgent
import random

def calculate_reward(boa, ply):
    r = 0

    c_p = sum(1 for r in range(boa.r) if boa.board[r][boa.c//2] == ply)
    r += c_p * 0.2

    r += count_potential_wins(boa, ply) * 0.4

    opp = 1 if boa == 2 else 2
    r -= count_potential_wins(boa, opp) * 0.5

    r += count_connected_pieces(boa, ply) * 0.1

    return r

def count_potential_wins(boa, ply):
    count = 0

    for r in range(boa.r):
        for c in range(boa.c - 3):
            win = [boa.board[r][c+i] for i in range(4)]
            if win.count(ply) == 3 and win.count(0) == 1:
                count += 1


    for r in range(boa.r - 3):
        for c in range(boa.c):
            win = [boa.board[r+i][c] for i in range(4)]
            if win.count(ply) == 3 and win.count(0) == 1:
                count += 1


    for r in range(boa.r - 3):
        for c in range(boa.c - 3):
            win = [boa.board[r+i][c+i] for i in range(4)]
            if win.count(ply) == 3 and win.count(0) == 1:
                count += 1

    return count

def count_connected_pieces(boa, ply):
    con = 0

    for r in range(boa.r):
        for c in range(boa.c - 1):
            if boa.board[r][c] == ply and boa.board[r][c+1] == ply:
                con += 1

    for r in range(boa.r - 1):
        for c in range(boa.c):
            if boa.board[r][c] == ply and boa.board[r+1][c] == ply:
                con += 1

    return con

def train_q_learning(eps=200000):
    q_agent = QAgent(a=0.1, g=0.99, e=0.3)
    no_player = NormalPlayer()

    wins = 0
    draws = 0
    recent_wins = []
    window_size = 1000
    start_time = time.time()

    for episode in range(eps):
        brd = Board()
        done = False
        turn = random.choice([0, 1])

        while not done:
            if turn == 0:
                col = no_player.get_move(brd)
                if col is not None:
                    row = brd.get_blank_rows(col)
                    brd.next_move(row, col, 1)

                    if brd.winner_checker(1):
                        q_agent.learn_from_result(brd, -2.0, True)
                        done = True
                    elif brd.is_full():
                        q_agent.learn_from_result(brd, 0.5, True)
                        draws += 1
                        done = True
                    else:
                        r = calculate_reward(brd, 2)
                        q_agent.learn_from_result(brd, r, False)

            else:
                col = q_agent.get_move(brd)
                if col is not None:
                    row = brd.get_blank_rows(col)
                    brd.next_move(row, col, 2)

                    if brd.winner_checker(2):
                        q_agent.learn_from_result(brd, 2.0, True)
                        wins += 1
                        recent_wins.append(1)
                        done = True
                    elif brd.is_full():
                        q_agent.learn_from_result(brd, 0.5, True)
                        draws += 1
                        recent_wins.append(0)
                        done = True
                    else:
                        r = calculate_reward(brd, 2)
                        q_agent.learn_from_result(brd, r, False)

            turn = 1 - turn

        if len(recent_wins) > window_size:
            recent_wins.pop(0)

        if episode % 1000 == 0:
            recent_win_rate = sum(recent_wins) / len(recent_wins) if recent_wins else 0
            q_agent.save_model()

            elapsed_time = time.time() - start_time
            print(f"\nEpisode {episode + 1}/{eps}")
            print(f"Overall Win Rate: {(wins/(episode+1))*100:.2f}%")
            print(f"Recent Win Rate: {recent_win_rate*100:.2f}%")
            print(f"Draw Rate: {(draws/(episode+1))*100:.2f}%")
            print(f"Current epsilon: {q_agent.q_learner.epsilon:.3f}")
            print(f"Time elapsed: {elapsed_time:.1f} seconds")
            print("------------------------")

    q_agent.save_model()
    total_time = time.time() - start_time
    print("\nTraining completed!")
    print(f"Final Win Rate: {(wins/eps)*100:.2f}%")
    print(f"Final Draw Rate: {(draws/eps)*100:.2f}%")
    print(f"Total training time: {total_time:.1f} seconds")

if __name__ == "__main__":
    train_q_learning()