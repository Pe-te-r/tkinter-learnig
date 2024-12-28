import tkinter as tk
from tkinter import ttk
from database import Database

window = tk.Tk()
window.geometry('500x400')
window.title('password manager')

# tree view
table = ttk.Treeview(window,columns=['url','password'],show='headings')
table.pack(expand=True,fill='both')

table.heading('url',text='Url column',command=lambda: print('clicked'))
table.heading('password',text='password column')

database = Database("passwords")
for item in database.fetchAll():
          table.insert(parent='',index=tk.END,values=item)

# print(database.fetchAll())

window.mainloop()