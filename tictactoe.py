import tkinter as tk
from tkinter import messagebox
from State import State

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.state = State()
        self.current_player = "X"
        self.buttons = []

        # Create the 3x3 button grid
        for i in range(9):
            btn = tk.Button(root, text=" ", width=10, height=4,
                            command=lambda idx=i: self.on_click(idx))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def on_click(self, index):
        try:
            self.state.make_move(index, self.current_player)
        except Exception:
            print("illegal move")
            return  # illegal move

        self.buttons[index]['text'] = self.current_player
        self.buttons[index]['state'] = 'disabled'

        if self.state.is_terminal:
            if self.state.draw:
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
            self.disable_all_buttons()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"

    def disable_all_buttons(self):
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
