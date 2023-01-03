from tkinter import *
import random
from tkinter import messagebox
from turtle import delay

ws = Tk()
ws.title("Guessing Number")
ws.geometry('300x200')
ws.config(bg = '#FFFF99')

Label(ws, text='Number Guessing Game', font = 'Calibri 18', width = 22, bg = "#CCFFCC", relief = 'solid').place(x=15, y=20)

box = Entry(ws, width=20, relief = 'ridge')
box.place(x=85, y=80)

label = Label(ws, width = 35, text=" ", font = 'Calibri', relief = 'flat', bg = '#66FF66')
label.place(x=8, y=165)

attempt = 5

def guess():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    choice = random.randint(0, 9)
    result = nums[choice]
    input = int(box.get())
    global attempt
    attempt -= 1
    if input == result:
        label.config(text= "Your number is correct!")
        box.delete(0, END)
    elif attempt == 0:
        label.config(text = 'You have no attempt left. Try again!')
    elif input > result:
        label.config(text = str(input) + " is greater. You have only " + str(attempt) + " attempt left.")
    else:
        label.config(text = str(input) + " is lower. You have only " + str(attempt) + " attempt left.")
    box.delete(0, END)

              

button = Button(ws, text="Guess", command=guess, relief = 'groove')
button.place(x=125, y=120)

ws.mainloop()
