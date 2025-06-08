import tkinter as tk

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("Tic Tac Toe")
        self.curr_player = "X"
        self.turns = 0
        self.game_over = False
        self.board = [[None]*3 for _ in range(3)]

        # Colors
        self.color_blue = "#4584b6"
        self.color_yellow = "#f7d74c"
        self.color_gray = "#d9d9d9"
        self.color_light_gray = "#f2f2f2"

        # Frame and label
        self.frame = tk.Frame(self.window)
        self.label = tk.Label(self.frame, text=self.curr_player + "'s turn", font=("Consolas", 20),
                              background=self.color_gray, foreground="white")
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

        # Buttons (game board)
        for row in range(3):
            for col in range(3):
                self.board[row][col] = tk.Button(self.frame, text="", font=("Consolas", 50, "bold"),
                                                 background=self.color_gray, foreground=self.color_blue,
                                                 width=4, height=1,
                                                 command=lambda r=row, c=col: self.set_tile(r, c))
                self.board[row][col].grid(row=row+1, column=col)

        # Reset button
        reset_btn = tk.Button(self.frame, text="Reset", font=("Consolas", 20),
                              background=self.color_gray, foreground="white", command=self.reset_game)
        reset_btn.grid(row=4, column=0, columnspan=3, sticky="we")

        self.frame.pack()

    def set_tile(self, row, col):
        if self.game_over or self.board[row][col]["text"] != "":
            return

        self.board[row][col]["text"] = self.curr_player
        self.check_winner()

        if not self.game_over:
            self.switch_player()

    def switch_player(self):
        self.curr_player = "O" if self.curr_player == "X" else "X"
        self.label["text"] = self.curr_player + "'s turn"

    def check_winner(self):
        self.turns += 1
        b = self.board
        lines = [  # 8 possible win conditions
            [b[0][0], b[0][1], b[0][2]],
            [b[1][0], b[1][1], b[1][2]],
            [b[2][0], b[2][1], b[2][2]],
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]],
        ]

        for line in lines:
            if line[0]["text"] == line[1]["text"] == line[2]["text"] != "":
                for btn in line:
                    btn.config(foreground=self.color_yellow, background=self.color_light_gray)
                self.label.config(text=f"{line[0]['text']} wins!", foreground=self.color_yellow)
                self.game_over = True
                return

        if self.turns == 9:
            self.label.config(text="It's a tie!", foreground=self.color_yellow)
            for row in self.board:
                for btn in row:
                    btn.config(foreground=self.color_yellow, background=self.color_light_gray)
            self.game_over = True

    def reset_game(self):
        self.curr_player = "X"
        self.turns = 0
        self.game_over = False
        self.label.config(text=self.curr_player + "'s turn", foreground="white")
        for row in self.board:
            for btn in row:
                btn.config(text="", foreground=self.color_blue, background=self.color_gray)


# Start the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    
    # Center the window on the screen
    root.update()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_x = int(screen_width / 2 - window_width / 2)
    window_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    root.mainloop()
