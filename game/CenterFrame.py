from tkinter import ttk
from Cell import Cell
class CenterFrame(ttk.Frame):
    def __init__(self, master, style, mine_var, exploded_mines):
        self.style = style
        self.exploded_mines = exploded_mines
        self.mine_var = mine_var
        style.configure("Center.TFrame", background="#2c3e50")
        super().__init__(master=master, style="Center.TFrame")
        self.place(rely=0.2, relx=0.3, relheight=0.8, relwidth=0.7)
        self.grid_size = 5
        for i in range(self.grid_size):
            self.columnconfigure(i, weight=1, uniform="a")
            self.rowconfigure(i, weight=1, uniform="a")
        self.add_cells()

    def add_cells(self):
        Cell.all = []
        self.exploded_mines.set(value=0)
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                cell = Cell(self, col, row, self.style, self.exploded_mines)
                cell.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        Cell.randomize(self.mine_var.get())
