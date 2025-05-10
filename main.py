from connect import Connect4MainGame
from connect_q_vs_normal import Connect4QvsNormal
import pygame

def display_menu():
    pygame.init()
    scr = pygame.display.set_mode((700, 400))
    pygame.display.set_caption("Connect 4 - Game Mode Selection")
    fon = pygame.font.SysFont("arial", 32)
    title_font = pygame.font.SysFont("arial", 48, bold=True)

    BG_COLOR = (30, 30, 60)
    TEXT_COLOR = (255, 255, 255)
    HLT_CLR = (0, 255, 127)

    options = [
        "1. Minimax vs Normal Player",
        "2. Minimax vs Q-Learning",
        "3. Q-Learning vs Normal Player",
        "4. Quit"
    ]

    selected = 0

    while True:
        scr.fill(BG_COLOR)

        t = title_font.render("Select one of the Connect 4 Game Modes", True, HLT_CLR)
        scr.blit(t, (700//2 - t.get_width()//2, 50))

        for i, option in enumerate(options):
            color = HLT_CLR if i == selected else TEXT_COLOR
            text = fon.render(option, True, color)
            scr.blit(text, (700//2 - text.get_width()//2, 150 + i * 60))

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
        n =10
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
        elif choice == 4 or choice is None:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
