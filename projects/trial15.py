import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('grid layout')

label1 = ttk.Label(window,text='label one',background='red')
label2 = ttk.Label(window,text='label two',background='blue')
label3 = ttk.Label(window,text='label Three',background='green')
label4 = ttk.Label(window,text='label Four',background='yellow')
button = ttk.Button(window,text='button one')
button2 = ttk.Button(window,text='button two')
entry = ttk.Entry(window)

window.columnconfigure([0,1,2],weight=1,uniform='a')
window.columnconfigure(3, weight=3, uniform="a")

window.rowconfigure((0, 1, 2), weight=1, uniform="a")
window.rowconfigure(3, weight=3, uniform="a")

label1.grid(row=0,sticky='news',column=0)
label2.grid(column=1,row=1,sticky='news',rowspan=3)
label3.grid(column=0,row=1,sticky='news',columnspan=3,padx=10,pady=10)
label4.grid(column=3,row=3,sticky='se')
button.grid(column=3,row=0,sticky='news')
button2.grid(column=2,row=2,sticky='news')
entry.grid(column=3,row=3)
window.mainloop()