import tkinter as tk
from tkinter import messagebox
from State import State
from agent_player import *
from minimax import *

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.state = State()
        self.current_player = self.state.current_player
        self.buttons = []
        self.ai_player = q_learning_player()
        

        font = ("Helvetica", 24, "bold")

        # Create the 3x3 button grid
        for i in range(9):
            btn = tk.Button(root, text=" ", font=font, bg="lightgray", activebackground="lightblue", width=10, height=4,  relief="raised", borderwidth=3,
                            command=lambda idx=i: self.on_click(idx))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

        # Reset button
        self.reset_button = tk.Button(root, font=font, text="Reset",bg="gray", command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=1, sticky="nsew")

        # AI selection
        self.ai_choice = ai_choice = tk.StringVar(value="Off")
        options = ["Off", "Minimax", "Q Learning"]
        self.dropdown = tk.OptionMenu(root,  self.ai_choice,*options)
        self.dropdown.grid(row=3, column=1, columnspan=1, sticky="nsew")

        # training button
        self.training_button = tk.Button(root, font=font, text="train", command=self.train)
        self.training_button.grid(row=3, column=2, sticky="nsew", columnspan=1)

    def train(self):
        self.ai_player.train()
        print("Done training!")
        # print(self.ai_player.q_table)


    def on_click(self, index):
        self.make_move(index)

        selected_ai = self.ai_choice.get()
        if not self.state.is_terminal and self.current_player == "O":
            if selected_ai == "Q Learning":
                move = self.ai_player.choose_action(self.state)
                self.make_move(move)
            elif selected_ai == "Minimax":
                eval, move  = alpha_beta_search(self.state, maxPlayer=False)
                self.make_move(move)
        # No move if "Off"


    def make_move(self, move):
        try:
            self.state.make_move(move)
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
