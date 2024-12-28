import tkinter as tk
from tkinter import ttk

def button_fun(widget):
          print(widget.get())

window = tk.Tk()
window.geometry('400x300')
window.title('functions arguments')

# data
entry_var = tk.StringVar(value='test')

# widget
entry =ttk.Entry(window,textvariable=entry_var)
entry.pack()

button = ttk.Button(window,text='button press',command=lambda: button_fun(entry_var))
button.pack()

window.mainloop()