import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('class and fucntion approach')
window.geometry('400x600')

class Segmen(ttk.Frame):
          def __init__(self,parent,label_text,button_text):
                    super().__init__(master=parent)
                    self.rowconfigure(0,weight=1)
                    self.columnconfigure((0,1,2),weight=1,uniform='a')
                    ttk.Label(self,text=label_text).grid(column=0,row=0,sticky='news')
                    ttk.Button(self,text=button_text).grid(column=1,row=0,sticky='news')
                    self.pack(expand=True,fill='both',padx=10,pady=10)
          
          def form_input(self,label_text):
                    frame = ttk.Frame(self)
                    ttk.Entry(frame).pack(expand=True,fill='both')
                    ttk.Label(frame,text=label_text,background='green').pack(expand=True,fill='both')
                    return frame
Segmen(window,'username','verify').form_input('here').grid(column=3,row=0,sticky='news')
Segmen(window,'username','verify').form_input('here').grid(column=3,row=0,sticky='news')
Segmen(window,'username','verify').form_input('here').grid(column=3,row=0,sticky='news')
Segmen(window,'username','verify').form_input('here').grid(column=3,row=0,sticky='news')

window.mainloop()