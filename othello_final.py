import tkinter as tk
from tkinter import *
from tkinter import messagebox
class Othello:
    

    def __init__(self,master):
        self.master = master
        self.master.title("Othello")
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()
        self.black_score = 2
        self.white_score = 2
        self.count=4
        self.current_player = 'black'
        self.turn_label=tk.Label(master,text=f"Turn: {self.current_player}")
        self.turn_label.pack()
        self.score_label = tk.Label(master, text=f"Black: {self.black_score}  White: {self.white_score}")
        self.score_label.pack()
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board[3][3], self.board[4][4] = 'white', 'white'
        self.board[3][4], self.board[4][3] = 'black', 'black'
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)
   
    def draw_board(self):
        self.canvas.delete("tiles")
        for row in range(8):
            for col in range(8):
                x0, y0 = col * 50, row * 50
                x1, y1 = x0 + 50, y0 + 50
                color = "green"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, tags="tiles")
                if self.board[row][col] != ' ':
                    self.canvas.create_oval(x0+5, y0+5, x1-5, y1-5, fill=self.board[row][col], tags="tiles")
    def scores(self):
        self.score_label.config(text=f"Black: {self.black_score}  White: {self.white_score}")

    def on_click(self,event):
        col = event.x // 50
        row = event.y // 50
        if self.is_valid_move(row, col):
            if self.current_player=='black': 
                         self.black_score=self.black_score+1
                         
            else :
                         self.white_score=self.white_score+1
        
            self.make_move(row, col)
            self.scores()
            self.turn_label.config(text=f"Turn: {self.current_player}")
            self.draw_board()  
            if self.count==64:
                if(self.black_score>self.white_score):
                    messagebox.showinfo(' ','Game Over,Black Wins')
                else:
                    messagebox.showinfo(' ','Game Over,White Wins')   
            
        else:
            if self.count==63:
                if(self.black_score>self.white_score):
                    messagebox.showinfo(' ','Game Over,Black Wins')
                else:
                    messagebox.showinfo(' ','Game Over,White Wins')
            else:            
             messagebox.showerror(' ','Invalid,Try again!')
             
    def is_valid_move(self, row, col):
        if self.board[row][col] != ' ':
            return False

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for dir_x, dir_y in directions:
            x, y = row + dir_x, col + dir_y
            temp = []
            while 0 <= x < 8 and 0 <= y < 8:
                if self.board[x][y] == ' ':
                    break
                elif self.board[x][y] == self.current_player:
                    if temp:
                        return True
                    break
                else:
                    temp.append((x, y))
                x += dir_x
                y += dir_y
        return False

    def make_move(self, row, col):
        self.count+=1
        self.board[row][col] = self.current_player
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dir_x, dir_y in directions:
            x, y = row + dir_x, col + dir_y
            temp = []
            while 0 <= x < 8 and 0 <= y < 8:
                if self.board[x][y] == ' ':
                    break
                elif self.board[x][y] == self.current_player:
                    
                    for i, j in temp:
                        self.board[i][j] = self.current_player
                        if self.current_player=='black': 
                         self.black_score=self.black_score+1
                         self.white_score=self.white_score-1
                        else :
                         self.white_score=self.white_score+1
                         self.black_score=self.black_score-1
                    break
                else:
                    temp.append((x, y))
                x += dir_x
                y += dir_y
        self.current_player = 'white' if self.current_player == 'black' else 'black'
    
def main():
    root = tk.Tk()
    othello = Othello(root)
    root.mainloop()

if __name__ == "__main__":
    main()
