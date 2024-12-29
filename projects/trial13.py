import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x600")
window.title("layout for pack")

label1 = ttk.Label(window, text="label one", background="red")
label1.pack(pady=10,padx=10,expand=True,fill='both',side='top')

label2 = ttk.Label(window, text="label two", background="blue")
label2.pack(side='left',expand=True,fill='both')

label3 = ttk.Label(window, text="label three", background="green")
label3.pack(expand=True,fill='both')

button = ttk.Button(window, text="button")
button.pack(expand=True,fill='both')

window.mainloop()
