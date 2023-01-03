from tkinter import *
from datetime import date

ws = Tk()
ws.title('Age Calculator')
ws.geometry('420x250')
ws.config(bg = '#00FFCC')

Label(ws, text = "Name :", width = 10, fg = "#FF9933", font = 'Fixedsys 13 ', bg = '#00FFCC'). place(x = 60, y = 10)
Label(ws, text = "Year :", width = 10, fg = "#FF9933", font = 'Fixedsys 13 ', bg = '#00FFCC'). place(x = 60, y = 50)
Label(ws, text = "Month :", width = 10, fg = "#FF9933", font = 'Fixedsys 13 ', bg = '#00FFCC'). place(x = 60, y = 90)
Label(ws, text = "Day :", width = 10, fg = "#FF9933", font = 'Fixedsys 13 ', bg = '#00FFCC'). place(x = 60, y = 130)
label = Label(ws, text = " ", font = 'Calibri 10 bold', width = 20, bg = "#00CCFF")
label.place(x = 20, y = 210)
label_1 = Label(ws, text = " ", font = 'Calibri 10 bold', width = 28, bg = "#FFCC00")
label_1.place(x = 200, y = 210)

name = Entry(ws, width = 20, font = 'Verdana', relief = 'ridge')
name.place(x = 200, y = 10)

year = Entry(ws, width = 20, font = 'Verdana', relief = 'ridge')
year.place(x = 200, y = 50)

month = Entry(ws, width = 20, font = 'Verdana', relief = 'ridge')
month.place(x = 200, y = 90)

day = Entry(ws, width = 20, font = 'Verdana', relief = 'ridge')
day.place(x = 200, y = 130)

def calculate():
    today = date.today()
    y,m,d = int(year.get()),int(month.get()),int(day.get())
    birthDate = date(y,m,d)
    age = today.year-birthDate.year
    if age < 2:
        op = "a baby"
    elif age > 2 and age <= 10:
        op = "an underage"
    elif age > 10 and age < 20:
        op = "a teenager"
    else:
        op = "an adult"
    label.config(text = "You are "+op)
    label_1.config(text = str(name.get())+ ", your age is "+ str(age))

Button(ws, text = 'Calculate Age', width = 20, command = calculate, font = 'System 13', relief = 'solid', bg = 'Black', fg = 'White').place(x = 220, y = 170)



ws.mainloop()

