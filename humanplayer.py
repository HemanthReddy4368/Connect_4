class HumanPlayer:
    def get_move(self, board):
        while True:
            try:
                col = int(input(f"Your turn! Enter column (0-{board.c-1}): "))
                if col in board.get_legal_moves():
                    return col
                else:
                    print("Invalid move! Column is either full or out of range.")
            except ValueError:
                print("Please enter a valid number!")