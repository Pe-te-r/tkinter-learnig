import tkinter as tk
from tkinter import  ttk
# from DIsplay import TopFrame,CenterFrame,SideFrame
from SideFrame import SideFrame
from CenterFrame import CenterFrame
from TopFrame import TopFrame

class Window(tk.Tk):
    def __init__(self, width, height, title):
        super().__init__()
        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(False, False)
        self.style = ttk.Style()

        # Data
        self.exploded_mines = tk.IntVar()
        self.opened_cell=tk.IntVar()
        self.mine_size = tk.IntVar(value=6)
        self.grid_size_var = tk.IntVar(value=5)  

        # Frames
        top_frame = TopFrame(self, self.style, self.mine_size)
        self.side_frame=SideFrame(self, self.style, self.mine_size, self.exploded_mines,self.grid_size_var)
        self.center_frame = CenterFrame(
            self, self.style, self.mine_size, self.exploded_mines,self.grid_size_var,self.opened_cell
        )

        # Link top frame to center frame
        top_frame.set_start_game(self.center_frame.add_cells)
        self.side_frame.set_start_game(self.center_frame.add_cells)

        self.mainloop()
    
    def check_win(self):
        # if self.opened_cell.get() + self.mine_size.get() > self.grid_size_var.get() **2:
        #     return True
        # return False
        print(self.opened_cell.get())
        if self.grid_size_var.get()**2 - self.mine_size.get() <= self.opened_cell.get():
            return True
        return False
    
    def game_over(self):
        if self.exploded_mines.get()>3:
            return True
        return False

Window(1200,800,'minescapper')