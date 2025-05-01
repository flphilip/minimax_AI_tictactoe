import tkinter as tk
from tkinter import messagebox
from State import State
from minimax import *

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.state = State()
        self.current_player = "X"
        self.buttons = []
        

        font = ("Helvetica", 24, "bold")

        # Create the 3x3 button grid
        for i in range(9):
            btn = tk.Button(root, text=" ", font=font, bg="lightgray", activebackground="lightblue", width=10, height=4,  relief="raised", borderwidth=3,
                            command=lambda idx=i: self.on_click(idx))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

        # Reset button
        self.reset_button = tk.Button(root, font=font, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=2, sticky="nsew")

        # turn on AI checkbox
        self.AI_enabled = False
        self.checkbox = tk.Checkbutton(root, font=font, text="Turn on AI", command=self.enable_AI)
        self.checkbox.grid(row=3, column=2, columnspan=1, sticky="nsew")

    def enable_AI(self):
        self.AI_enabled = not self.AI_enabled
        print(self.AI_enabled)
        if self.current_player == "O":
            self.make_ai_move()


    def on_click(self, index):
        try:
            self.state.make_move(index, self.current_player)
        except Exception:
            print("illegal move")
            return
        self.buttons[index]['text'] = self.current_player
        self.buttons[index]['state'] = 'disabled'

        if self.state.is_terminal:
            if self.state.draw:
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
            self.disable_all_buttons()
            return
        else:
            self.current_player = "O" if self.current_player == "X" else "X"

        if self.AI_enabled:
            return self.make_ai_move()

    def make_ai_move(self):
        eval, move = minimax(self.state, maxPlayer=False)
        print(eval, move)
        try:
            self.state.make_move(move, self.current_player)
        except Exception:
            print("illegal move")
            return
        self.buttons[move]['text'] = self.current_player
        self.buttons[move]['state'] = 'disabled'

        if self.state.is_terminal:
            if self.state.draw:
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
            self.disable_all_buttons()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"

    def disable_all_buttons(self):
        # does not effect reset button
        for btn in self.buttons:
            btn['state'] = 'disabled'

    def reset_game(self):
        self.state = State()
        self.current_player = "X"
        for btn in self.buttons:
            btn['text'] = " "
            btn['state'] = 'normal'


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
