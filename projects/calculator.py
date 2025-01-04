import tkinter as tk
from tkinter import ttk,font

class Calculator(tk.Tk):
    def __init__(self,title,size):
        super().__init__()
        self.title(title)
        print(font.families())
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        self.columnconfigure((0,1,2,3),weight=1,uniform='a')
        self.rowconfigure((0,1,2,3,4),weight=1,uniform='a')
        self.style = ttk.Style()
        print(self.style.theme_names())
        self.style.theme_use('clam')
        self.input_show=Input(self,self.style)
        self.input_show.grid(row=0,column=0,columnspan=4,sticky='esw',ipadx=17,ipady=20,padx=5)
        self.math_work =DoMath(self.input_show)
        self.add_buttons()

    def add_buttons(self):
        ButtonCalc(self,'1',self.style,self.input_show).grid(row=4,column=0,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'0',self.style,self.input_show).grid(row=4,column=1,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'=',self.style,self.input_show,funct=self.math_work).grid(row=4,column=2,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'2',self.style,self.input_show).grid(row=3,column=0,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'3',self.style,self.input_show).grid(row=3,column=1,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'4',self.style,self.input_show).grid(row=3,column=2,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'5',self.style,self.input_show).grid(row=2,column=0,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'6',self.style,self.input_show).grid(row=2,column=1,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'7',self.style,self.input_show).grid(row=2,column=2,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'8',self.style,self.input_show).grid(row=1,column=0,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'9',self.style,self.input_show).grid(row=1,column=1,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'c',self.style,self.input_show).grid(row=1,column=2,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'+',self.style,self.input_show).grid(row=1,column=3,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'/',self.style,self.input_show).grid(row=2,column=3,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'*',self.style,self.input_show).grid(row=3,column=3,sticky='news',padx=5,pady=5)
        ButtonCalc(self,'-',self.style,self.input_show,funct=self.math_work).grid(row=4,column=3,sticky='news',padx=5,pady=5)
        self.mainloop()

class DoMath:
    def __init__(self,input):
        self.input=input
        self.sign = ''
        self.add = Add()
        self.subtract=Subtract()
        self.multiple = Multiple()
        self.division = Division()
        print(self.input.entry_value.get())

    def set_sign(self,sign):
        self.sign=sign

class SetValues:
    def __init__(self):
        self.num1=0
        self.num2=0
    def set_num1(self,num1):
        self.num1=num1
    def set_num2(self,num2):
        self.num2=num2

class Add(SetValues):
    def __init__(self):
        super().__init__()
    def total(self):
        return int(self.num1)+int(self.num2)

class Subtract(SetValues):
    def __init__(self):
        super().__init__()
    def total(self):
        return int(self.num1)-int(self.num2)

class Multiple(SetValues):
    def __init__(self):
        super().__init__()
    def total(self):
        return int(self.num1) * int(self.num2)

class Division(SetValues):
    def __init__(self):
        super().__init__()
    def total(self):
        return float(self.num1)/float(self.num2)

class Input(ttk.Entry):
    def __init__(self,parent,style ):
        super().__init__(parent)
        self.style = style
        self.entry_value = tk.StringVar(value='')
        self.style.configure('TEntry',font=('Cantarell',20))
        # self.style.map('TEntry',foreground=[('disabled','black')],background=[('disabled','black')])
        self['textvariable']=self.entry_value
        # self['state']='disabled'
        # self['style']='TEntry'

class ButtonCalc(ttk.Frame):
    def __init__(self,parent,button_text,style,input,funct=None):
        super().__init__(parent)
        self.style = style
        self.input=input
        self.button_text =button_text
        self.style.configure('TButton',background='#ffed22',hover='green',font=('FreeMono',20))
        self.style.map('TButton',background=[('hover','#ffe192')])
        self.funt = funct
        ttk.Button(self,text=button_text,command=self.handle_click  ).pack(fill='both',expand=True)
    
    def handle_click(self):
        value = self.input.entry_value.get()
        value += self.button_text 
        if self.button_text == '=':
            self.handle_equals()
        print(value)
        if self.button_text == '-':
            index=value.find('-')
            self.funt.set_sign('-')
            if self.funt.subtract.num1 == 0:
                self.funt.subtract.set_num1(int(value[:index-1]))
            if self.funt.subtract.num2 == 0 and self.funt.subtract.num1 != 0:
                self.funt.subtract.set_num2(int(value[index + 1:]))
        self.input.entry_value.set(value)
    def handle_equals(self):
        if self.funt.sign == '-':
            # pass
            print(self.funt.subtract.num1)
            print(self.funt.subtract.num2)
            # print(self.funt.subtract.total())
    

Calculator('calculator trial',(600,800))