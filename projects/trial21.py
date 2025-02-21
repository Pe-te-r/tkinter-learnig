import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self,title,size):
        super().__init__()
        self.geometry(f'{size[0]}x{size[1]}')
        self.geometry('500x600')
        self.title(title)
        self.minsize(size[0],size[1])

        # 
        self.style = ttk.Style()

        self.style.theme_use('classic')

        MainFrame(self,self.style)

        self.mainloop()



class MainFrame(ttk.Frame):
    def __init__(self,parent,style):
        super().__init__(parent)
        self.style = style
        self.style.configure('one.TFrame',background='#2081DD')
        self.pack(expand=True,fill='both')
        self['style']='one.TFrame'
        SidePanel(self,self.style)
        MainPanel(self,self.style)


class MainPanel(ttk.Frame):
    def __init__(self,parent,style):
        super().__init__(parent)
        self.style = style
        self.frame=ttk.Frame(self)
        self.start()
        self.frame.place(relx=.25,rely=.5,anchor='sw')
    def start(self):
        self.style.configure('TEntry',foreground='black')
        self.style.configure('two.TFrame',background='orange')
        self['style'] = 'two.TFrame'
        self.place(relx=.3,relwidth=.7,relheight=1)
        self.head()
        self.body()
    def head(self):
        ttk.Label(self,text='Phantom Manager',font=('Arial',16,'bold'),justify='center',background='orange').pack(padx=5,pady=8,fill='x')
    def body(self):
        self.style.configure('TButton',background='green',foreground='white')
        self.style.map('TButton',background=[('hover','blue')])
        self.username= tk.StringVar()
        self.password= tk.StringVar()
        ttk.Label(self.frame, text="Login", font=("Source Code Pro", 15,'bold')).pack(ipady=10)
        self.input('username',self.username)
        self.input('password',self.password)
        ttk.Button(self.frame,text='submit',command=self.getInput).pack(pady=10)
    def input(self, label_text,value):
        self.input_frame = ttk.Frame(self.frame)
        self.input_frame.pack()
        ttk.Label(self.input_frame,text=label_text,font=('FreeSerif',16,),justify='center').pack(side='left',pady=10,padx=10)
        self.input_frame.pack()
        self.entry = ttk.Entry(self.input_frame,textvariable=value)
        self.entry.pack(side='left',pady=10,padx=10)

    def getInput(self):
        # print(self.username.get(), self.password.get())
        if self.username.get()=='peter' and self.password.get()=='wahu':
            print('here')
            self.frame.forget()
            self.frame = ttk.Frame(self)
            # ttk.Label(self.frame,background='white',text='welcome here').pack(expand=True,fill='both')
            self.frame.pack(expand=True,fill='both')



class SidePanel(ttk.Frame):
    def __init__(self,parent,style):
        super().__init__(parent)
        self.style=style
        self.style.configure('side.TFrame',background='grey')
        self['style']='side.TFrame'
        self.place(x=0,relheight=1,relwidth=.3)

App('fun trial',(800,800))