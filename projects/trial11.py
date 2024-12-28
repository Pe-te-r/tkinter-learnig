import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('200x100')
window.title('Tabs')

notebook = ttk.Notebook(window)
notebook.pack()

# tab 1
tab1 = ttk.Frame(notebook)
label = ttk.Label(tab1,text='found on tab1')
label.pack()

# tab 2
tab2 = ttk.Frame(notebook)
label_tab2 = ttk.Label(tab2,text='found on tab2')
label_tab2.pack()

# tab3 
tab3 = ttk.Frame(notebook)
button1 = ttk.Button(tab3,text='button 1')
button2 = ttk.Button(tab3,text='button 2')
entry_tab3 = ttk.Entry(tab3)

button1.pack()
button2.pack()
entry_tab3.pack()

notebook.add(tab1,text='Tab 1')
notebook.add(tab2, text="Tab 2")
notebook.add(tab3,text='Tab 3')

window.mainloop()