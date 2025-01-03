import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
          def __init__(self, title,size=(500,600)):
                    super().__init__()
                    self.title(title)
                    self.geometry(f"{size[0]}x{size[1]}")
                    self.minsize(size[0], size[1])
                    SizeNotify(
                              self,
                              {300: self.small_layout, 600: self.medium_layout, 1000: self.large_layout},
                    )
                    self.frame = ttk.Frame(self)
                    self.frame.pack()
                    self.mainloop()

          def small_layout(self):
            self.frame.forget()
            self.frame = ttk.Frame(self)
            ttk.Label(self.frame, text="label 1", background="red").pack(
                expand=True, fill="both", padx=10, pady=10
            )
            ttk.Label(self.frame, text="label 2", background="green").pack(
                expand=True, fill="both", padx=10, pady=10
            )
            ttk.Label(self.frame, text="label 3", background="blue").pack(
                expand=True, fill="both", padx=10, pady=10
            )
            ttk.Label(self.frame, text="label 4", background="yellow").pack(
                expand=True, fill="both", padx=10, pady=10
            )
            self.frame.pack(expand=True, fill="both")

          def medium_layout(self):
            self.frame.forget()
            self.frame = ttk.Frame(self)
            self.frame.columnconfigure((0, 1), weight=1, uniform="a")
            self.frame.rowconfigure((0, 1), uniform="a", weight=1)
            ttk.Label(self.frame, text="label 1", background="red").grid(
                column=0, row=0, sticky="news", padx=10, pady=10
            )
            ttk.Label(self.frame, text="label 2", background="green").grid(
                row=0, column=1, sticky="news", padx=10, pady=10
            )
            ttk.Label(self.frame, text="label 3", background="blue").grid(
                row=1, column=1, sticky="news", padx=10, pady=10
            )
            ttk.Label(self.frame, text="label 4", background="yellow").grid(
                row=1, column=0, sticky="news", padx=10, pady=10)
            self.frame.pack(expand=True, fill="both")

          def large_layout(self):
                    self.frame.forget()
                    self.frame = ttk.Frame(self)
                    self.frame.columnconfigure((0, 1,2,3), weight=1, uniform="a")
                    self.frame.rowconfigure(0, uniform="a", weight=1)
                    ttk.Label(self.frame, text="label 1", background="red").grid(row=0, column=0, sticky="news", padx=10, pady=10)
                    ttk.Label(self.frame, text="label 2", background="green").grid(row=0, column=1, sticky="news", padx=10, pady=10)
                    ttk.Label(self.frame, text="label 3", background="blue").grid(row=0, column=2, sticky="news", padx=10, pady=10)
                    ttk.Label(self.frame, text="label 4", background="yellow").grid(row=0, column=3, sticky="news", padx=10, pady=10)
                    print('large layout')
                    self.frame.pack(expand=True, fill="both")
class SizeNotify():
          def __init__(self,window,size_dict):
                    self.window=window
                    self.size_dict = {key:value for key,value in sorted(size_dict.items())}
                    self.verified_size=None
                    self.window.bind('<Configure>',lambda event: self.check_size(event))
                    # self.window.update()
          
          def check_size(self,event):
                    if event.widget==self.window:
                              current_size =event.width
                              checked_size=None
                              for key,value in self.size_dict.items():
                                        delta = current_size -key
                                        print(delta)
                                        if delta >=0:
                                                  checked_size=key
                              
                              if checked_size != self.verified_size:
                                        self.verified_size=checked_size
                                        if self.verified_size is not None:
                                                  self.size_dict[checked_size]()
App('home')