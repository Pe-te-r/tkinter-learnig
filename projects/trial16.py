import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.geometry('1000x700')
window.title('different layout')
window.minsize(600,600)

menu_frame = ttk.Frame(window)
main_frame = ttk.Frame(window)

# menu widget
button1 = ttk.Button(menu_frame,text='button one')
button2 = ttk.Button(menu_frame,text='button two')
button3 = ttk.Button(menu_frame,text='button three')
scaler1 = ttk.Scale(menu_frame,from_=0,to=30,length=200,orient='vertical')
scaler2 = ttk.Scale(menu_frame,from_=0,to=30,length=200,orient='vertical')
# toggle frame
toggle_frame = ttk.Frame(menu_frame)
check1 = ttk.Checkbutton(toggle_frame, text="male")
check2 = ttk.Checkbutton(toggle_frame, text="female")

# main widget
# frame one
main_frame1 =ttk.Frame(main_frame)
label1= ttk.Label(main_frame1,text='label one',background='red')
button4= ttk.Button(main_frame1,text='button one')


main_frame2 =ttk.Frame(main_frame)
label2= ttk.Label(main_frame2,text='label one',background='blue')
button5= ttk.Button(main_frame2,text='button one')


# menu layout
menu_frame.columnconfigure([0,1,2,],weight=1,uniform='a')
menu_frame.rowconfigure([0,1,2,3,4],weight=1,uniform='a')

button1.grid(row=0,column=0,sticky='news',columnspan=2)
button2.grid(row=0,column=2,sticky='news')
button3.grid(row=1,column=0,columnspan=3,sticky='news')
scaler1.grid(row=2,column=0,rowspan=2 , sticky='ns')
scaler2.grid(row=2,column=2,rowspan=2 , sticky='ns')
toggle_frame.grid(row=4,column=0,columnspan=3,sticky='news')
check1.pack(side='left',expand=True)
check2.pack(side='left',expand=True)

# main layout
label1.pack(expand=True,fill='both')
button4.pack(expand=True,fill='both',pady=10)

label2.pack(expand=True,fill='both')
button5.pack(expand=True,fill='both',pady=10)

main_frame1.pack(side='left',expand=True,fill='both',padx=10,pady=10)
main_frame2.pack(side='left',expand=True,fill='both',padx=10,pady=10)

#window layout
menu_frame.place(x=0,y=0,relwidth=0.3,relheight=1)
main_frame.place(relx=0.3,relwidth=0.7,relheight=1,y=0)

window.mainloop()