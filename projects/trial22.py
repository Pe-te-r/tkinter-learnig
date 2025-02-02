import tkinter as tk
from tkinter import  ttk
from random import sample


# class Window(tk.Tk):
#     def __init__(self, width, height, title):
#         super().__init__()
#         self.geometry(f"{width}x{height}")
#         self.title(title)
#         self.resizable(False, False)
#         self.style = ttk.Style()
#         # data
#         self.exploded_mines=tk.IntVar()
#         self.mine_size=tk.IntVar(value=6)
#         top_frame=TopFrame(self, self.style,self.mine_size)
#         SideFrame(self, self.style,self.mine_size,self.exploded_mines)
#         center_frame = CenterFrame(self, self.style, self.mine_size,self.exploded_mines)
#         top_frame.set_start_game(center_frame.add_cells)
#         self.mainloop()

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

class TopFrame(ttk.Frame):
    def __init__(self, master, style, mine_var):
        style.configure("Top.TFrame", background="#2c3e50")  # Dark blue background
        super().__init__(master, style="Top.TFrame")
        self.mine_var = mine_var

        # Label for the slider
        self.text_var = tk.StringVar(
            value=f"Adjust the number of mines {mine_var.get()} available"
        )
        ttk.Label(
            self,
            textvariable=self.text_var,
            font=("Arial", 14),
            foreground="white",
            background="#2c3e50",
        ).pack(expand=True, pady=10)

        # Slider (ttk.Scale) to adjust the number of mines
        self.slider = ttk.Scale(
            self,
            from_=5,  # Minimum value
            to=10,  # Maximum value
            length=5,
            orient="horizontal",  # Horizontal orientation
            variable=mine_var,  # Linked to the mine_var IntVar
            command=self.reset_mine,  # Callback when the slider is moved
        )
        self.slider.place(
            relx=0.4, rely=0.8, relwidth=0.3
        )  # Add padding and fill horizontally
        mine_var.trace_add(
            "write",
            lambda *args: self.text_var.set(f"There are {mine_var.get()} mines"),
        )

        # Reset button
        self.reset_button = ttk.Button(
            self,
            text="Reset Game",
            command=self.reset_game,
        )
        self.reset_button.place(relx=0.8, rely=.5, relwidth=0.2)

        # Place the frame
        self.place(x=0, y=0, relwidth=1, relheight=0.2)
        self.start_func = None

    def set_start_game(self, func):
        self.start_func = func

    def reset_mine(self, *args):
        if self.start_func is not None:
            self.start_func()

    def reset_game(self):
        if self.start_func is not None:
            self.start_func()

class SideFrame(ttk.Frame):
    def __init__(self, master, style, mine_var, exploded_mines):
        style.configure("Side.TFrame", background="#34495e") 
        super().__init__(master=master, style="Side.TFrame")
        self.string_var = tk.StringVar(self, value=f"There are {mine_var.get()}  mines")
        ttk.Label(self,textvariable=self.string_var,font=("Arial", 14),foreground="white",background="#34495e",).pack(expand=True, pady=20)
        exploded_mines.trace_add(
            "write",
            lambda *args: self.string_var.set(
                f"Exploded mines: {exploded_mines.get()}"
            ),
        )
        self.place(x=0, rely=0.2, relwidth=0.3, relheight=1)

class CenterFrame(ttk.Frame):
    def __init__(self, master, style, mine_var, exploded_mines):
        self.style = style
        self.exploded_mines=exploded_mines
        self.mine_var=mine_var
        style.configure("Center.TFrame", background="#2c3e50")
        super().__init__(master=master, style="Center.TFrame")
        self.place(rely=0.2, relx=0.3, relheight=0.8, relwidth=0.7)
        self.grid_size = 5
        for i in range(self.grid_size):
            self.columnconfigure(i, weight=1, uniform="a")
            self.rowconfigure(i, weight=1, uniform="a")
        self.add_cells()

    def add_cells(self):
        Cell.all=[]
        self.exploded_mines.set(value=0)
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                cell = Cell(self, col, row, self.style,self. exploded_mines)
                cell.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
        Cell.randomize(self.mine_var.get())



class Cell(ttk.Button):
    all = []

    def __init__(self, master, col, row, style, exploded_mines, is_mine=False):
        super().__init__(master=master)
        self.col = col
        self.row = row
        self.style = style
        self.exploded_mines = exploded_mines
        self.is_clicked=False
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
                self.exploded_mines.set(int(self.exploded_mines.get()+1))
                self.show_mine_error()
            else:
                self.show_cell()
                if self.mine_cell_number == 0:
                    cells = self.get_neighbour_cell
                    for cell in cells:
                        cell.show_cell()
            self.is_clicked=True

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


Window(900, 600, "mine game")

