import tkinter as ttk
import pandas as pd

model=pd.read_pickle('houseprice.pickle')

app=ttk.Tk()
app.geometry('300x300')
app.title('House Price predictor')

ttk.Label(app, tex='Income').grid(row=0,column=0)
ttk.Entry(app, textvariable=income).grid(row=0,column=1)


app.mainloop()