from tkinter import ttk,StringVar

class TopFrame(ttk.Frame):
    def __init__(self, master, style, mine_var):
        style.configure("Top.TFrame", background="#2c3e50")  
        super().__init__(master, style="Top.TFrame")
        self.mine_var = mine_var

        self.adjust_mines_display()
        self.reset_button_display()


        # Place the frame
        self.place(x=0, y=0, relwidth=1, relheight=0.2)
        self.start_func = None

    def adjust_mines_display(self):
        self.frame1=ttk.Frame(self,style='Top.TFrame')
        self.frame1.pack(side='left',expand=True,fill='both')
           # Label for the slider
        self.text_var = StringVar(value=f"There are {self.mine_var.get()} mines 💣 available")
        ttk.Label(self.frame1,textvariable=self.text_var,font=("Arial", 14),foreground="white",background="#2c3e50",).pack(expand=True, pady=10)
        self.mine_var.trace_add("write",lambda *args: self.text_var.set(f"There are {self.mine_var.get()} mines 💣 available"),)

        # Slider (ttk.Scale) to adjust the number of mines
        self.slider = ttk.Scale(self.frame1,from_=5, to=10, length=5,orient="horizontal",variable=self.mine_var, command=self.reset_game,)
        self.slider.pack(expand=True,fill='x')

    def reset_button_display(self):
        self.frame2=ttk.Frame(self,style='Top.TFrame')
        self.frame2.pack(side='left',expand=True,fill='both')
        self.reset_button = ttk.Button(self.frame2,text="Reset Game",   command=self.reset_game,)
        self.reset_button.pack(expand=True)

    def set_start_game(self, func):
        self.start_func = func

    def reset_game(self,*args):
        if self.start_func is not None:
            self.start_func()
