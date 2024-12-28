import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.geometry('500x300')
window.title('Scale and progress bar')

scale_var = tk.IntVar(value=15)
scale = ttk.Scale(window,variable=scale_var,from_=0 ,to=30,command=lambda _: print(scale_var.get()),length=300,orient='horizontal')
scale.pack()

progress=ttk.Progressbar(window,maximum=30,variable=scale_var)
progress.pack()

# exercise
exercise_var= tk.IntVar()
progress_bar= ttk.Progressbar(window,maximum=100,variable=exercise_var,orient='vertical')
progress_bar.pack()
progress_bar.start()

label = ttk.Label(window,text='label',textvariable=exercise_var)
label.pack()

scale_bar = ttk.Scale(window, from_=0, to=100,length=180, command=lambda _: print(scale_var.get()),variable=exercise_var)
scale_bar.pack()

window.mainloop()