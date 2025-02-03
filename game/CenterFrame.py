from tkinter import ttk
from Cell import Cell
class CenterFrame(ttk.Frame):
    def __init__(self, master, style, mine_var, exploded_mines,gride_size):
        self.style = style
        self.exploded_mines = exploded_mines
        self.mine_var = mine_var
        style.configure("Center.TFrame", background="#2c3e50")
        self.grid_size = gride_size
        super().__init__(master=master, style="Center.TFrame")
        self.place(rely=0.2, relx=0.3, relheight=0.8, relwidth=0.7)
        self.add_cells()

    def add_cells(self):
        for widget in self.winfo_children():
            widget.destroy()


        Cell.all = []
        for i in range(self.grid_size.get()):
            self.columnconfigure(i, weight=1, uniform="a")
            self.rowconfigure(i, weight=1, uniform="a")
        self.exploded_mines.set(value=0)
        for row in range(self.grid_size.get()):
            for col in range(self.grid_size.get()):
                cell = Cell(self, col, row, self.style, self.exploded_mines)
                cell.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        Cell.randomize(self.mine_var.get())
