import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x500')
window.title('combo and spin')
# data
items= ['sweater','jacket','shoes']

# variable
combo_var = tk.StringVar(value=items[0])

# widget
combo = ttk.Combobox(window,values=items,textvariable=combo_var)
combo.pack()

spin = ttk.Spinbox(window,values=items,command=lambda: print('new item choosen'))
spin.pack()

# event
combo.bind('<<ComboboxSelected>>',lambda event:print('item selected'))

# exercise
items_exe=['A','B','C','D','E']
items_var = tk.StringVar(value=items_exe[0])
spin_exercise = ttk.Spinbox(window,values=items_exe,textvariable=items_var)
spin_exercise.pack()

spin_exercise.bind("<<Decrement>>", lambda event: print("value decresed"))

window.mainloop()