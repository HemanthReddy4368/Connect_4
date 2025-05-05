import pygame
import time
from board import Board
from q_agent import QAgent
from normal_player import NormalPlayer
from constants import *

class Connect4QvsNormal:
    def __init__(self):
        pygame.init()
        self.b = Board()
        self.q_agent = QAgent()
        self.q_agent.load_model() 
        self.normal_player = NormalPlayer()
        self.game_over = False
        self.turn = 0 
        self.clock = pygame.time.Clock()

        self.width = self.b.c * SSize
        self.height = (self.b.r + 1) * SSize
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Connect 4 - Q-Learning vs Normal Player")

    def game_board(self, last_move=None):
        self.screen.fill(BG_COLOR)
        for c in range(self.b.c):
            for r in range(self.b.r):
                pygame.draw.rect(
                    self.screen, BRD_CLR,
                    (c*SSize, (r+1)*SSize, SSize, SSize),
                    border_radius=12
                )
                pygame.draw.rect(
                    self.screen, GRD_CLR,
                    (c*SSize, (r+1)*SSize, SSize, SSize),
                    width=4, border_radius=12
                )
                pygame.draw.circle(
                    self.screen, EMPT_CLR,
                    (c*SSize+SSize//2, (r+1)*SSize+SSize//2),
                    RADIUS
                )

        for c in range(self.b.c):
            for r in range(self.b.r):
                if self.b.board[r][c] == 1:
                    color = PLY_CLR1
                elif self.b.board[r][c] == 2:
                    color = PLY_CLR2
                else:
                    continue
                pygame.draw.circle(
                    self.screen, color,
                    (c*SSize+SSize//2, self.height-r*SSize-SSize//2),
                    RADIUS
                )

        if last_move is not None:
            r, c = last_move
            pygame.draw.circle(
                self.screen, HLT_CLR,
                (c*SSize+SSize//2, self.height-r*SSize-SSize//2),
                RADIUS, width=6
            )

        pygame.display.update()

    def show_message(self, message, color=HLT_CLR):
        font = pygame.font.SysFont("arial", 60, bold=True)
        text = font.render(message, True, color)
        self.screen.blit(text, (self.width//2 - text.get_width()//2, 10))
        pygame.display.update()

    def game_play(self):
        last_move = None

        while not self.game_over:
            self.clock.tick(FPS)
            self.game_board(last_move)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            if self.turn == 0:
                col = self.q_agent.get_move(self.b)
            else:
                col = self.normal_player.get_move(self.b)

            if col is not None:
                row = self.b.get_blank_rows(col)
                self.b.next_move(row, col, self.turn + 1)
                last_move = (row, col)

                if self.b.winner_checker(self.turn + 1):
                    self.game_board(last_move)
                    winner = "Q-Learning Agent" if self.turn == 0 else "Normal Player"
                    self.show_message(f"{winner} wins!")
                    self.game_over = True
                    pygame.time.wait(3500)
                    break

                self.turn = 1 - self.turn

            if self.b.is_full():
                self.show_message("It's a draw!")
                self.game_over = True
                pygame.time.wait(3500)
                break

            pygame.time.wait(400)

        pygame.quit()

if __name__ == "__main__":
    game = Connect4QvsNormal()
    game.game_play()
