import tkinter as tk
from tkinter import ttk

def button2_press():
          print('hello')
          print(label2)
def button_press():
          print("button pressed")

window =tk.Tk()
window.title('Label and widgets')
window.geometry('600x500')

label = ttk.Label(window,text='This is a test')
label.pack()

text=tk.Text(master=window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

label2=ttk.Label(window,text='my label')
label2.pack()

button = ttk.Button(window,text='button',command=button_press)
button.pack()

button2=ttk.Button(window,text='exercise button',command=button2_press)
button2.pack()

window.mainloop()