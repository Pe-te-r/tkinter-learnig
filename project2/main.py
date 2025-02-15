import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self,size,title):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(expand=True,fill='both')
        SideView(self.main_frame)
        # run
        self.mainloop()


class SideView(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        ttk.Label(text="Label 1").pack()
if __name__=='__main__':
    MainWindow((1200,900),'Phantom App')