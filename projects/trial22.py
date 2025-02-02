import tkinter as tk
from tkinter import ttk
from random import sample


class Window(tk.Tk):
    def __init__(self, width, height, title):
        super().__init__()
        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(False, False)
        self.style = ttk.Style()
        TopFrame(self, self.style)
        SideFrame(self, self.style)
        CenterFrame(self, self.style)
        self.mainloop()


class TopFrame(ttk.Frame):
    def __init__(self, master, style):
        style.configure("Top.TFrame", background="lightblue")
        super().__init__(master, style="Top.TFrame")
        self.place(x=0, y=0, relwidth=1, relheight=0.2)


class SideFrame(ttk.Frame):
    def __init__(self, master, style):
        style.configure("Side.TFrame", background="blue")
        super().__init__(master=master, style="Side.TFrame")
        self.place(x=0, rely=0.2, relwidth=0.3, relheight=1)


class CenterFrame(ttk.Frame):
    def __init__(self, master, style):
        self.style = style
        self.style.configure("Center.TFrame", background="black")
        super().__init__(master=master, style="Center.TFrame")
        self.place(rely=0.2, relx=0.3, relheight=0.8, relwidth=0.7)
        self.grid_size = 5
        for i in range(self.grid_size):
            self.columnconfigure(i, weight=1, uniform="a")
            self.rowconfigure(i, weight=1, uniform="a")
        self.add_cells()

    def add_cells(self):
        Cell.all=[]
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                cell = Cell(self, col, row, self.style)
                cell.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        Cell.randomize()


class Cell(ttk.Button):
    all = []

    def __init__(self, master, col, row, style, is_mine=False):
        super().__init__(master=master)
        self.col = col
        self.row = row
        self.style = style
        self.is_mine = is_mine
        # Configure the button to expand
        self.configure(style="TButton")
        # Events
        self.bind("<Button-1>", self.left_click)
        self.bind("<Button-3>", self.right_click)
        # Append cell
        Cell.all.append(self)

    def __repr__(self):
        return f"Cell({self.col} {self.row})"

    # When left clicked
    def left_click(self, event):
        if self.is_mine:
            self.show_mine_error()
        else:
            self.show_cell()
            if self.mine_cell_number == 0:
                cells = self.get_neighbour_cell
                for cell in cells:
                    cell.show_cell()

    def show_cell(self):
        _ = self.get_neighbour_cell
        counter = self.mine_cell_number
        self.config(text=counter)

    @property
    def mine_cell_number(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    @property
    def get_neighbour_cell(self):
        cells = [
            Cell.get_cell(self.col - 1, self.row),
            Cell.get_cell(self.col + 1, self.row),
            Cell.get_cell(self.col, self.row + 1),
            Cell.get_cell(self.col, self.row - 1),
            Cell.get_cell(self.col + 1, self.row - 1),
            Cell.get_cell(self.col - 1, self.row + 1),
            Cell.get_cell(self.col + 1, self.row + 1),
            Cell.get_cell(self.col - 1, self.row - 1),
        ]
        self.surrounded_cells = [cell for cell in cells if cell is not None]
        return self.surrounded_cells

    def show_mine_error(self):
        self.style.configure("Mine.TButton", background="red")
        self.config(style="Mine.TButton", text="mine")

    def right_click(self, event):
        print("right click")
        if self.is_mine:
            self.style.configure("Mine.TButton", background="blue")
            self.config(style="Mine.TButton", text="mine")

    @classmethod
    def get_cell(cls, col, row):
        cell_return = None
        for cell in cls.all:
            if cell.col == col and cell.row == row:
                cell_return = cell
                break
        return cell_return

    @classmethod
    def randomize(cls, size=9):
        cells = sample(cls.all, size)
        for cell in cells:
            cell.is_mine = True


Window(900, 600, "mine game")
