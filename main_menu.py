import tkinter as tk
from tkinter import messagebox
from othelo_final import Othello as Game

class MainMenu:
    
    def __init__(self,master):
        self.master=master
        self.master.title("Othello Menu")

        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack()

        self.title_label = tk.Label(self.menu_frame, text="Othello Menu", font=('Comic Sans MS', 32))
        self.title_label.grid(row=0, column=0, padx=5, pady=5)
        self.selected_items_text =  tk.Button(self.menu_frame, text="Rules", font=('Comic Sans MS', 20),height=2, width=20, command=self.display_rules)
        self.selected_items_text.grid(row=1, column=0, columnspan=2, padx=5)

        self.start_button = tk.Button(self.menu_frame, text="Start", font=('Comic Sans MS', 20),height=2, width=20, command=self.start_game)
        self.start_button.grid(row=2, column=0, padx=5, pady=5)

    def display_rules(self):
        messagebox.showinfo("Rules of Othello", "Goal: Gain control of the board by flipping your opponent's discs to your color\nMoves: Place discs to capture your opponent's discs by sandwiching them between your discs.\nWinning: The player with the most discs of their color at the end wins.\nStrategy: Plan ahead to control key positions and limit your opponent's options.")

    def start_game(self):
        self.master.destroy()
        game=tk.Tk()
        startgame= Game(game)
    
        
def main():
        root = tk.Tk() 
        othello_menu = MainMenu(root)
        root.mainloop()
        root.destroy() 
if __name__ == "__main__":
  main()
    



