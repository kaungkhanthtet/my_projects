from tkinter import *
import random
from PIL import ImageTk, Image, Rotate

ws = Tk()
ws.title('Magic 8 Ball')
ws.geometry('350x470')
ws.config(bg = '#99FFFF')

input_1 = Entry(ws, width = 47, font = 'Times 10 bold', fg = '#000066', relief = 'flat')
input_1.place(x = 8, y = 30)

label_1 = Label(ws, width = 40, text = " ", background= '#99FFFF', font = 'Comic 10 bold', fg = '#006600', relief = 'flat')
label_1.place(x = 15, y = 80)
label_2 = Label(ws, width = 40, text = " ", background= '#99FFFF', font = 'Comic 10 bold', fg = '#006600', relief = 'flat')
label_2.place(x = 10, y = 100)
label_3 = Label(ws, width = 40, text = " ", background= '#99FFFF', font = 'Comic 10 bold', fg = '#006600', relief = 'flat')
label_3.place(x = 15, y = 410)

def start():
    name = "Hello, "+ input_1.get() +" welcome to Magic 8 Ball"
    label_1.config(text = name)
    letter = "Ask me for an advice then press the icon below"
    label_2.config(text = letter)
    global input_2
    input_2 = Entry(ws, width = 55)
    input_2.place(x = 8, y = 130)

def button():
    global st_b
    st_b = Button(ws, width = 15, text = "Start", command = start, relief = 'ridge', font = 'Courier 10 bold', fg = '#FFFFFF', bg = '#FFCC00')
    st_b.place(x = 110, y = 50)


b = Button(ws, text = 'Enter your name:', command = button, relief='flat', background= '#99FFFF', font = 'System 10', fg = '#FF3300')
b.place(x = 115, y = 0)

def clear ():
    input_1.delete(0,END)
    input_2.destroy()
    label_1.config(text = " ")
    label_2.config(text = " ")
    label_3.config(text = " ")
    st_b.destroy()
    cl_b.destroy()
    
def shake():
    ans = ["Most likely", "Very doubtful", "I'm not sure. Ask me again.", "As I see it, yes.", "My sources say no", "Cannot predict now", "Makes no difference to me, do or don't - whatever.", "Yes, I think on balance that is right choice."]
    choice = random.randint(0,7)
    output = choice
    op = ans[output]
    label_3.config(text = op)
    global cl_b
    cl_b = Button(ws, width = 15, text = "Clear", command = clear, relief = 'solid', bg = '#FF6633', font = 'Arial 10 bold', fg = '#FFFFFF')
    cl_b.place(x = 110, y = 435)

pic = PhotoImage(file = 'PY4Y/final_project\img\8.png')
b_1 = Button(ws, image = pic, command = shake, relief = "flat", background= '#99FFFF')
b_1.place(x = 60, y = 170)

ws.mainloop()

