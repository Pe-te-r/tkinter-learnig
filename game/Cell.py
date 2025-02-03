from tkinter import ttk
from random import sample
class Cell(ttk.Button):
    all = []

    def __init__(self, master, col, row, style, exploded_mines, is_mine=False):
        super().__init__(master=master)
        self.col = col
        self.row = row
        self.style = style
        self.exploded_mines = exploded_mines
        self.is_clicked = False
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
        if self.is_clicked is not True:
            if self.is_mine:
                self.exploded_mines.set(int(self.exploded_mines.get() + 1))
                self.show_mine_error()
            else:
                self.show_cell()
                if self.mine_cell_number == 0:
                    cells = self.get_neighbour_cell
                    for cell in cells:
                        cell.show_cell()
            self.is_clicked = True

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
        self.config(style="Mine.TButton", text="💣")

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
    def randomize(cls, size):
        cells = sample(cls.all, size)
        for cell in cells:
            cell.is_mine = True


