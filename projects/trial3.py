import tkinter as tk
from tkinter import   ttk

def button_press():
          entry_val = entry.get()
          # label.configure(text='Some other text set')
          label['text']=entry_val
          entry['state']='disable'

def reset_btn():
          entry['state']='enable'
          label['text']='This is a label'

window=tk.Tk()
window.geometry('300x200')
window.title('getting and setting widgets')

label=ttk.Label(window,text='This is a label')
label.pack()

entry= ttk.Entry(window)
entry.pack()

button= ttk.Button(window,text='button',command=button_press)
button.pack()

button2=ttk.Button(window,text='reset',command=reset_btn)
button2.pack()

window.mainloop()