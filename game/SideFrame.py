from tkinter import ttk,StringVar
class SideFrame(ttk.Frame):
    def __init__(self, master, style, mine_var, exploded_mines,grid_size):
        style.configure("Side.TFrame", background="#34495e")
        super().__init__(master=master, style="Side.TFrame")
        self.mine_var=mine_var
        self.grid_size=grid_size
        self.start_func=None
        self.string_var = StringVar(self, value=f"There are {mine_var.get()}  mines")
        ttk.Label(
            self,
            textvariable=self.string_var,
            font=("Arial", 14),
            foreground="white",
            background="#34495e",
        ).pack( pady=20)
        exploded_mines.trace_add(
            "write",
            lambda *args: self.string_var.set(
                f"Exploded mines: {exploded_mines.get()}"
            ),
        )
        self.adjust_cell_display()
        self.place(x=0, rely=0.2, relwidth=0.3, relheight=1)

    def adjust_cell_display(self):
        self.frame3=ttk.Frame(self,style='Side.TFrame')
        self.frame3.pack(side='top',expand=True,fill='both')
        self.cell_var = StringVar(value=f"Adjust cells {self.mine_var.get()} available")
        ttk.Label(self.frame3,textvariable=self.cell_var,font=("Arial", 14),foreground="white",background="#34495e").pack(pady=10)

        # Slider (ttk.Scale) to adjust the number of mines
        slider = ttk.Scale(self.frame3,from_=5, to=10, orient="horizontal",variable=self.grid_size,command=self.reset_game)
        slider.pack(fill='x',padx=10)
    
    def set_start_game(self, func):
        self.start_func = func

    def reset_game(self,*args):
        if self.start_func is not None:
            self.start_func()

