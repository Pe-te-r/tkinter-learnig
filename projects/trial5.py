import tkinter as tk
from tkinter import ttk

def button_press():
          print('button clicked')

def radio_fun():
    print(check_var_exercise.get())
    check_var_exercise.set(False)

def check_fun():
    print(radio_var_exercise.get())

window = tk.Tk()
window.geometry('500x400')
window.title('buttons functions')

# variables
button_var = tk.StringVar(value='button var')
check_var = tk.IntVar(value=10)
radio_var = tk.StringVar()
check_var_exercise=tk.BooleanVar(value=True)
radio_var_exercise = tk.StringVar(value='A')

# button
button = ttk.Button(window,text='button 1',command=button_press,textvariable=button_var)
button.pack()

# checkbox
checkbox = ttk.Checkbutton(window,text='agree to terms and services',variable=check_var,command=lambda: print(check_var.get()),onvalue=10,offvalue=5)
checkbox.pack()

# radio
radio1 = ttk.Radiobutton(window,text='male',variable=radio_var,value='male',command=lambda: print(radio_var.get()))
radio1.pack()
radio2= ttk.Radiobutton(window,text='female',variable=radio_var,value='female',command=lambda: print(radio_var.get()))
radio2.pack()

# exercise
check_button2 = ttk.Checkbutton(window, text="exercise", variable=check_var_exercise,command=check_fun)
check_button2.pack()

radio3=ttk.Radiobutton(window,text='A',value='A',command=radio_fun, variable=radio_var_exercise)
radio3.pack()
radio4=ttk.Radiobutton(window,text='B',value='B',command=radio_fun, variable=radio_var_exercise)
radio4.pack()

window.mainloop()