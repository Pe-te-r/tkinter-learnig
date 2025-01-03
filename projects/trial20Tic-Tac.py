import tkinter as tk
from tkinter import ttk,font

current_player = 'X'

def change_player():
          global current_player
          if current_player=='X':
                    current_player='O'
          elif current_player=='O':
                    current_player='X'

class App(tk.Tk):
          def __init__(self, title, size):
                    super().__init__()
                    self.geometry(f"{size[0]}x{size[1]}")
                    print(font.families())
                    self.minsize(size[0], size[1])
                    self.title(title)
                    # style
                    self.style = ttk.Style()
                    # self.style.theme_use("alt")
                    self.style.configure("X.TButton", background="grey", font=("", 20))
                    self.style.configure("win.TButton", background="blue", font=("", 20))
                    self.style.configure("over.TButton", background="red",font=('',20))
                    # layout
                    self.main_layout = ttk.Frame(self)
                    # SidePanel(self.main_layout,self.style)
                    self.frame=ttk.Frame(self.main_layout)
                    self.frame.columnconfigure((0, 1, 2), weight=1, uniform="a")
                    self.frame.rowconfigure((0, 1, 2), weight=1, uniform="a")
                    self.frame.place(relx=0,relwidth=1,relheight=1)
                    self.main_layout.pack(expand=True,fill='both')

                    self.squares = []
                    self.add_squares()
                    # attributes
                    self.game= Game(self,self.squares)

                    self.mainloop()

          def add_squares(self):
                    # first column
                    square1 = Square(self.frame,self)
                    square2 = Square(self.frame,self)
                    square3 = Square(self.frame,self)
                    self.squares.append([square1, square2, square3])
                    square1.grid(column=0, row=0, padx=10, pady=10, sticky="news")
                    square2.grid(column=1, row=0, padx=10, pady=10, sticky="news")
                    square3.grid(column=2, row=0, padx=10, pady=10, sticky="news")
                    # second column
                    square4 = Square(self.frame,self)
                    square5 = Square(self.frame,self)
                    square6 = Square(self.frame,self)
                    self.squares.append([square4,square5,square6])
                    square4.grid(column=0, row=1, padx=10, pady=10, sticky="news")
                    square5.grid(column=1, row=1, padx=10, pady=10, sticky="news")
                    square6.grid(column=2, row=1, padx=10, pady=10, sticky="news")
                    # third column
                    square7=Square(self.frame,self)
                    square8=Square(self.frame,self)
                    square9=Square(self.frame,self)
                    self.squares.append([square7,square8,square9])
                    square7.grid(column=0, row=2, padx=10, pady=10, sticky="news")
                    square8.grid(column=1, row=2, padx=10, pady=10, sticky="news")
                    square9.grid(column=2, row=2, padx=10, pady=10, sticky="news")


# class SidePanel(ttk.Frame):
#     def __init__(self,parent,style):
#         super().__init__(parent)
#         self.style = style
#         self.columnconfigure((0),weight=1,uniform='a')
#         self.rowconfigure((0,1,2),weight=1,uniform='a')
#         self.style.configure('Label.TFrame',background='green')
#         self.style.configure('Btn.TButton',background='brown',foreground = 'black',font=('Cantarell',20))
#         ttk.Button(self,text='New game',style='Btn.TButton').grid(row=0,column=0,padx=10,pady=10)
#         ttk.Button(self,text='ScoreBoard',style='Btn.TButton').grid(row=1,column=0,padx=10,pady=10)
#         ttk.Button(self,text='About',style='Btn.TButton').grid(row=2,column=0,padx=10,pady=10)
#         self['style'] = 'Label.TFrame'
#         self.place(relwidth=.3,x=0,relheight=1)


class Square(ttk.Frame):
    def __init__(self, parent,window):
        self.played_value = tk.StringVar()
        self.window = window
        super().__init__(master=parent)
        self.button = ttk.Button(
            self,
            textvariable=self.played_value,
            command=self.button_clicked,
            style="X.TButton",
        )
#         self.button['style'] = 'O.TButton'
        self.button.pack(expand=True, fill="both")

    def button_clicked(self):
          self.played_value.set(current_player)
          self.button['state']='disabled'
          change_player()
          self.window.game.check_win()
    
    def handle_lose(self):
        self.button['state']='disable'
        # self.button['style'] = 'over.TButton'
    
    def handle_win(self):
        self.button['state']='enable'
        self.button['style'] = 'win.TButton'
                    

class Game:
    def __init__(self, window, squares):
        self.window = window
        self.squares = squares
        self.winner = ''
        self.winning_squares = []

    def check_win(self):

        if (self.squares[0][0].played_value.get()== self.squares[0][1].played_value.get()== self.squares[0][2].played_value.get()!= ""):
            self.winning_squares.append([self.squares[0][0], self.squares[0][1], self.squares[0][2]])
            self.winner = self.squares[0][0].played_value.get()
            print(self.winner)

        if ( self.squares[1][0].played_value.get()== self.squares[1][1].played_value.get()== self.squares[1][2].played_value.get()!= ""):
            self.winning_squares.append([self.squares[1][0], self.squares[1][1], self.squares[1][2]])
            self.winner = self.squares[1][0].played_value.get()

        if (self.squares[2][0].played_value.get()== self.squares[2][1].played_value.get()== self.squares[2][2].played_value.get()!= ""):
            self.winning_squares.append([self.squares[2][0], self.squares[2][1], self.squares[2][2]])
            self.winner = self.squares[2][0].played_value.get()

        if (self.squares[0][0].played_value.get()== self.squares[1][0].played_value.get()== self.squares[2][0].played_value.get()!= ""):
            self.winning_squares.append([self.squares[0][0], self.squares[1][0], self.squares[2][0]])
            self.winner = self.squares[0][0].played_value.get()

        if (self.squares[0][1].played_value.get() == self.squares[1][1].played_value.get()== self.squares[2][1].played_value.get()!= ""):
            self.winning_squares.append([self.squares[0][1], self.squares[1][1], self.squares[2][1]])
            self.winner = self.squares[0][1].played_value.get()

        if (self.squares[0][2].played_value.get()== self.squares[1][2].played_value.get()== self.squares[2][2].played_value.get()!= ""):
            self.winning_squares.append([self.squares[0][2], self.squares[1][2], self.squares[2][2]])
            self.winner = self.squares[0][2].played_value.get()

        if (self.squares[0][0].played_value.get()== self.squares[1][1].played_value.get()== self.squares[2][2].played_value.get()!= ""):
            self.winning_squares.append([self.squares[0][0], self.squares[1][1], self.squares[2][2]])
            self.winner = self.squares[0][0].played_value.get()

        if (self.squares[2][0].played_value.get()== self.squares[1][1].played_value.get()== self.squares[0][2].played_value.get()!= ""):
            self.winning_squares.append([self.squares[2][0], self.squares[1][1], self.squares[0][2]])
            self.winner = self.squares[2][0].played_value.get()
        
        if len(self.winning_squares) > 0:
            for square in self.winning_squares[0]:
                square.handle_win()
            for row in self.squares:
                for square in row:
                    if square.played_value.get() != self.winner  and square.played_value.get()!= '':
                        print(self.winner)
                        square.handle_lose()


App('Tic-Tac-Toe Game',(500,500))
