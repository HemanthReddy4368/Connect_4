from Connect4MinimaxVsHuman import Connect4_MinimaxVsHuman
from connect import Connect4MainGame
from connect_q_vs_normal import Connect4QvsNormal
import pygame

def display_menu():
    pygame.init()
    scr = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Connect 4 - Game Mode Selection")
    fon = pygame.font.SysFont("arial", 72)
    title_font = pygame.font.SysFont("arial", 120, bold=True)

    BG_COLOR = (30, 30, 60)
    TEXT_COLOR = (255, 255, 255)
    HLT_CLR = (0, 255, 127)

    options = [
        "1. Minimax vs Normal Player",
        "2. Minimax vs Q-Learning",
        "3. Q-Learning vs Normal Player",
        "4. Minimax vs Human",
        "5. Quit"
    ]

    selected = 0

    while True:
        scr.fill(BG_COLOR)

        t = title_font.render("Select a Connect 4 Game Mode", True, HLT_CLR)
        scr.blit(t, (1600//2 - t.get_width()//2, 100))

        for i, option in enumerate(options):
            color = HLT_CLR if i == selected else TEXT_COLOR
            text = fon.render(option, True, color)
            scr.blit(text, (1600//2 - text.get_width()//2, 350 + i * 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    pygame.quit()
                    return selected + 1

        pygame.time.wait(100)

def main():
    while True:
        choice = display_menu()
        n = 10
        if choice == 1:
            for i in range(n):
                game = Connect4MainGame(use_q_learning=False)
                game.game_play()
        elif choice == 2:
            for i in range(n):
                game = Connect4MainGame(use_q_learning=True)
                game.game_play()
        elif choice == 3:
            for i in range(n):
                game = Connect4QvsNormal()
                game.game_play()
        elif choice == 4:
            game = Connect4_MinimaxVsHuman()
            game.game_play()
        elif choice == 5 or choice is None:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()