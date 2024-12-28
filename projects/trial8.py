import tkinter as tk
from tkinter import ttk
from random import  choice

def item_select(_):
          for i in table.selection():
                    print(table.item(i)['values'])

def item_delete(_):
          for i in table.selection():
                    table.delete(i)
window = tk.Tk()
window.geometry('600x500')
window.title('tables')

# data 
first_name=['peter','shakira','benja','john','alex','joy','mary']
last_name=['muthoni','mwaura','nyambura','mbugua','maina']

table = ttk.Treeview(window, columns=["first", "last", "email"], show="headings")
table.heading('first',text='First Name')
table.heading('last',text='Last Name')
table.heading('email',text='Email')
table.pack(expand=True,fill='both')

for i in range(100):
          firstName= choice(first_name)
          lastName=choice(last_name)
          email = f'{firstName}{lastName}@gmail.com'
          data = [firstName,lastName,email]
          table.insert(parent='',index=tk.END,values=data)

table.bind(
    "<<TreeviewSelect>>",item_select
)

table.bind(
          "<Delete>",
          item_delete
)
window.mainloop()