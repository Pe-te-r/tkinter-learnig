import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('frames layout')
window.geometry('400x600')

# top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame,text='label one',background='red')
label2 = ttk.Label(top_frame,text='label two',background='blue')


# middle Label
label3 = ttk.Label(window,text='Label Three', background='green')


# bottom frame 
bottom_frame = ttk.Frame(window)
button = ttk.Button(bottom_frame,text='button one')
button2 = ttk.Button(bottom_frame,text='button two')
label4= ttk.Label(bottom_frame,text='label 4',background='yellow')
# frame inside bottom frame
another_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(another_frame,text='button three')
button4 = ttk.Button(another_frame,text='button four')
button5 = ttk.Button(another_frame,text='button five')


# top layout
label1.pack(side='left',expand=True,fill='both')
label2.pack(side='left',expand=True,fill='both')
top_frame.pack(expand=True,fill='both')

# middle Layout
label3.pack(expand=True)


# bottomo layout
button.pack(side='left',expand=True,fill='both')
label4.pack(side='left',expand=True,fill='both')
button2.pack(side='left',expand=True,fill='both')

button3.pack(expand=True,fill='both')
button4.pack(expand=True,fill='both')
button5.pack(expand=True,fill='both')

another_frame.pack(side='left',fill='both',expand=True)
bottom_frame.pack(expand=True,fill='both',padx=10,pady=10)

window.mainloop()