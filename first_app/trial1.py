import tkinter as tk
# from tkinter import  ttk
import ttkbootstrap as ttk

def button_press():
          # print(entry.get())
          miles_input=entry_int.get()
          km_output = miles_input * 1.61
          text_string.set(f'{km_output} kms')

# window
window=tk.Tk()
window.title('first app')
window.geometry('300x200')

# widgets
text_label = ttk.Label(master=window,text='Miles to kilometers')
text_label.pack()

# frame
frame=ttk.Frame(master=window)

entry_int=tk.IntVar()
entry=ttk.Entry(master=window,textvariable=entry_int)

button=ttk.Button(window,text='convert',command=button_press)
entry.pack(pady=10)
button.pack()
frame.pack( pady=10)

# output
text_string=tk.StringVar()
text_string.set("Output show:")
output_show = ttk.Label(master=window,text='To show output',textvariable=text_string)
output_show.pack(pady=10)



window.mainloop()