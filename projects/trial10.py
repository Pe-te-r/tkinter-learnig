import tkinter as tk
from tkinter import Frame, Frame, ttk

window = tk.Tk()
window.title('frames and parenting')
window.geometry('500x300')

# frame
frame = ttk.Frame(window,width=300,height=100,relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='right')

string_var =tk.StringVar( value='Start')

label = ttk.Label(frame,text='label',textvariable=string_var)
label.pack()

entry = ttk.Entry(frame,textvariable=string_var)
entry.pack()

button = ttk.Button(frame,text='button')
button.pack()

window.mainloop()