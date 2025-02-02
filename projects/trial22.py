import tkinter as tk
from tkinter import re, re, DISABLED, DISABLED, ttk
from random import sample
class Window(tk.Tk):
    def __init__(self,width,height,title):
        super().__init__()
        self.geometry(f'{width}x{height}')
        self.title(title)
        self.resizable(False,False)
        self.style = ttk.Style()
        TopFrame(self,self.style)
        SideFrame(self,self.style)
        CenterFrame(self,self.style)
        self.mainloop()



class TopFrame(ttk.Frame):
    def __init__(self,master,style):
        style.configure("Top.TFrame", background="lightblue")
        super().__init__(master,style='Top.TFrame')
        self.place(x=0,y=0,relwidth=1,relheight=.2)

class SideFrame(ttk.Frame):
    def __init__(self,master,style):
        style.configure("Side.TFrame", background="blue")
        super().__init__(master=master,style='Side.TFrame')
        self.place(x=0,rely=.2,relwidth=.3,relheight=1)

class CenterFrame(ttk.Frame):
    def __init__(self,master,style):
        self.style=style
        self.style.configure("Center.TFrame", background="black")
        super().__init__(master=master,style='Center.TFrame')
        self.place(rely=.2,relx=.2,relheight=.8,relwidth=.8)
        self.columnconfigure((0,1,2,3,4),weight=1,uniform='a')
        self.rowconfigure((0,1,2,3,4),weight=1,uniform='a')
        self.grid_size=5
        self.add_cells()
    
    def add_cells(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                cell = Cell(self,col,row,self.style)
                # cell.create_btn_object()
                cell.grid(row=row,column=col,sticky='news',padx=2,pady=2)
        Cell.randomize()


class Cell(ttk.Button):
    all=[]
    def __init__(self,master,col,row,style,is_mine=False):
        super().__init__(master=master,text=f'({row} {col})')
        self.col=col
        self.row=row
        self.style=style
        self.is_mine=is_mine
        # events
        self.bind("<Button-1>", self.left_click)
        self.bind("<Button-3>", self.right_click)
        # append cell
        Cell.all.append(self)

    def left_click(self,event):
        if self.is_mine:
            self.show_mine_error()
        else:
            self.show_cell()
        
    def show_cell(self):
        cells=self.get_neighbour_cell
        counter=self.mine_cell(cells)
        print(counter)
        self.config(text=counter)

    def mine_cell(self,cells):
        counter=0
        for cell in cells:
            if cell.is_mine:
                counter +=1
        return counter
    @property
    def get_neighbour_cell(self):
        cells=[
            Cell.get_cell(self.col-1,self.row),
            Cell.get_cell(self.col+1,self.row),
            Cell.get_cell(self.col,self.row+1),
            Cell.get_cell(self.col,self.row-1),
            Cell.get_cell(self.col+1,self.row-1),
            Cell.get_cell(self.col-1,self.row+1),
            Cell.get_cell(self.col+1,self.row+1),
            Cell.get_cell(self.col-1,self.row-1),
        ]
        return [cell for cell in cells if cell is not None]
    # called when left click and is mine
    def show_mine_error(self):
        self.style.configure("Button.TFrame", background="red")
        self.config(style='Button.TFrame',text='mine')
        

    def right_click(self,event):
        pass
    
    @classmethod
    def get_cell(cls,col,row):
        cell_return=None
        for cell in cls.all:
            if cell.col==col and cell.row==row:
                cell_return=cell
                break
        return cell_return


    @classmethod
    def randomize(cls,size=9):
        cells = sample(cls.all,size)
        for cell in cells:
            cell.is_mine=True




Window(800,500,'mine game')