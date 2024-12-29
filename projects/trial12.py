import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('500x400')
window.title('layout for pack')

label1 = ttk.Label(window,text='label one',background='red')
label1.pack(fill='x')

label2 = ttk.Label(window,text='label two',background='blue')
label2.pack(expand=True)

label3 = ttk.Label(window,text='label three',background='green')
label3.pack(expand=True,fill='both')

button = ttk.Button(window,text='button')
button.pack(fill='x')

window.mainloop()