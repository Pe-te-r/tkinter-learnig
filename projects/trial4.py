import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.geometry('200x100')
window.title('variable in tkinter')

# widgets
string_var = tk.StringVar(value='test')
# string_var.set('test')

label = ttk.Label(window,text='Label',textvariable=string_var)
label.pack()

entry1 = ttk.Entry(window,textvariable=string_var)
entry1.pack()

entry2 = ttk.Entry(window,textvariable=string_var)
entry2.pack()

window.mainloop()