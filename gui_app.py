# GUI - graphical user interface

#libraries
############
#1. Tkinter
#2. PyQT
#3. Turtle

import tkinter as ttk

app = ttk.Tk()
app.title('My App')
app.geometry('600x400')

ttk.Label(app, text ='Gungun jain').place(x=50,y=50)
ttk.Label(app, text ='from computer science and engineering').place(x=100,y=100)




app.mainloop()
