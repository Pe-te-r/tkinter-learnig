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
        self.mine_size = tk.IntVar(value=6)
        self.grid_size_var = tk.IntVar(value=5)  # Variable for grid size

        # Frames
        top_frame = TopFrame(self, self.style, self.mine_size)
        SideFrame(self, self.style, self.mine_size, self.exploded_mines)
        center_frame = CenterFrame(
            self, self.style, self.mine_size, self.exploded_mines
        )

        # Link top frame to center frame
        top_frame.set_start_game(center_frame.add_cells)

        self.mainloop()

Window(1200,700,'minescapper')