import tkinter as tk
from tkinter import   ttk
# import ttkbootstrap as ttk

class App(tk.Tk):
          def __init__(self,title,size):
                    super().__init__(themename='journal')
                    self.geometry(f'{size[0]}x{size[1]}')
                    self.title(title)
                    self.minsize(size[0],size[1])

                    MenuFrame(self)
                    MainMenu(self)

                    # run
                    self.mainloop()


class MenuFrame(ttk.Frame):
          def __init__(self, parent):
                    super().__init__(parent)
                    self.place(x=0, y=0, relwidth=0.3, relheight=1)
                    self.handle_widgets()

          def handle_widgets(self):
                    button1 = ttk.Button(self, text="button one")
                    button2 = ttk.Button(self, text="button two")
                    button3 = ttk.Button(self, text="button three")
                    scaler1 = ttk.Scale(self, from_=0, to=30, length=200, orient="vertical")
                    scaler2 = ttk.Scale(self, from_=0, to=30, length=200, orient="vertical")
                    # toggle frame
                    toggle_frame = ttk.Frame(self)
                    check1 = ttk.Checkbutton(toggle_frame, text="male")
                    check2 = ttk.Checkbutton(toggle_frame, text="female")

          # menu layout
                    self.columnconfigure([0,1,2,],weight=1,uniform="a" )
                    self.rowconfigure([0, 1, 2, 3, 4], weight=1, uniform="a")

                    button1.grid(row=0, column=0, sticky="news", columnspan=2)
                    button2.grid(row=0, column=2, sticky="news")
                    button3.grid(row=1, column=0, columnspan=3, sticky="news")
                    scaler1.grid(row=2, column=0, rowspan=2, sticky="ns")
                    scaler2.grid(row=2, column=2, rowspan=2, sticky="ns")
                    toggle_frame.grid(row=4, column=0, columnspan=3, sticky="news")
                    check1.pack(side="left", expand=True)
                    check2.pack(side="left", expand=True)

class MainMenu(ttk.Frame):
          def __init__(self,parent):
                    super().__init__(parent)
                    self.place(relx=0.3,relheight=1,y=0,relwidth=0.7)
                    Entry(self,'label one','button one','green')
                    Entry(self,'label two','button two','blue')

class Entry(ttk.Frame):
          def __init__(self,parent,label_text,button_text,color):
                    super().__init__(parent)
                    ttk.Label(self,text=label_text,background=color).pack(expand=True,fill='both')
                    ttk.Button(self,text=button_text).pack(expand=True,fill='both',pady=10)
                    self.pack(side='left',expand=True,fill='both',padx=10,pady=10)
# layout
App('class based',(600,600))