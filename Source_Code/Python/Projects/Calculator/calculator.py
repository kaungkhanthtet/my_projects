import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

ws = tk.Tk()
ws.title('Calculator')
ws.geometry('310x400')
ws.config(bg='White')

lines = []
line = '___'
for j in range(25):
    lines.append(line)
Label(ws, text=lines, width=41, bg='White').place(x=9, y=123)

His = tk.Button(ws, text='H', width=4, relief='flat').place(x=10, y=102)
Con = tk.Button(ws, text='UC', width=4, relief='flat').place(x=55, y=102)
More = tk.Button(ws, text='More', width=4, relief='flat').place(x=100, y=102)
Del = tk.Button(ws, text='Del', width=4, relief='flat').place(x=260, y=102)

# Buttons

Clr = tk.Button(ws, text='C', width=5, font=20, relief='flat').place(x=10, y=150)
Brt = tk.Button(ws, text='()', width=5, font=20, relief='flat').place(x=85, y=150)
Per = tk.Button(ws, text='%', width=5, font=20, relief='flat').place(x=160, y=150)
Div = tk.Button(ws, text='/', width=5, font=20, relief='flat').place(x=235, y=150)

# Seven
pic_7 = Image.open("Projects\Calculator\cc_img\seven.png").resize((40, 40))
pic_se = ImageTk.PhotoImage(pic_7)
Seven = tk.Button(ws, image=pic_se, relief='flat', bg='white')
Seven.place(x=20, y=200)

a = 1
while a == 1:
    if Seven == 0:
        print("0")
    elif Seven == 0:
        print("Not 0")
    
# Eight
pic_8 = Image.open("Projects\Calculator\cc_img/number-8.png").resize((40, 40))
pic_ei = ImageTk.PhotoImage(pic_8)
Eight = tk.Button(ws, image=pic_ei, relief='flat', bg='white')
Eight.place(x=95, y=200)

# Nine
pic_9 = Image.open("Projects\Calculator\cc_img/number-9.png").resize((40, 40))
pic_ni = ImageTk.PhotoImage(pic_9)
Nine = tk.Button(ws, image=pic_ni, relief='flat', bg='White')
Nine.place(x=170, y=200)

# Multi
pic_x = Image.open("Projects\Calculator\cc_img\letter-x.png").resize((40, 40))
pic_mult = ImageTk.PhotoImage(pic_x)
Multi = tk.Button(ws, image=pic_mult, relief='flat', bg='White')
Multi.place(x=245, y=200)

# Four
pic_4 = Image.open("Projects\Calculator\cc_img/number-four.png").resize((40, 40))
pic_four = ImageTk.PhotoImage(pic_4)
Four = tk.Button(ws, image=pic_four, relief='flat', bg='white')
Four.place(x=20, y=250)

# Five
pic_5 = Image.open("Projects\Calculator\cc_img/number-5.png").resize((40, 40))
pic_five = ImageTk.PhotoImage(pic_5)
Five = tk.Button(ws, image=pic_five, relief='flat', bg='white')
Five.place(x=95, y=250)

# Six
pic_6 = Image.open("Projects\Calculator\cc_img\six.png").resize((40, 40))
pic_six = ImageTk.PhotoImage(pic_6)
Six = tk.Button(ws, image=pic_six, relief='flat', bg='White')
Six.place(x=170, y=250)

# Sub
pic_Sub = Image.open("Projects\Calculator\cc_img\minus.png").resize((40, 40))
pic_sub = ImageTk.PhotoImage(pic_Sub)
Sub = tk.Button(ws, image=pic_sub, relief='flat', bg='White')
Sub.place(x=245, y=250)

# One
pic_1 = Image.open("Projects\Calculator\cc_img/number-one.png").resize((40, 40))
pic_one = ImageTk.PhotoImage(pic_1)
One = tk.Button(ws, image=pic_one, relief='flat', bg='white')
One.place(x=20, y=300)

# Two
pic_2 = Image.open("Projects\Calculator\cc_img/number-2.png").resize((40, 40))
pic_two = ImageTk.PhotoImage(pic_2)
Two = tk.Button(ws, image=pic_two, relief='flat', bg='white')
Two.place(x=95, y=300)

# Three
pic_3 = Image.open("Projects\Calculator\cc_img/number-3.png").resize((40, 40))
pic_three = ImageTk.PhotoImage(pic_3)
Three = tk.Button(ws, image=pic_three, relief='flat', bg='White')
Three.place(x=170, y=300)

# Add
pic_Add = Image.open("Projects\Calculator\cc_img/add.png").resize((40, 40))
pic_add = ImageTk.PhotoImage(pic_Add)
Add = tk.Button(ws, image=pic_add, relief='flat', bg='White')
Add.place(x=245, y=300)

Minus = tk.Button(ws, text='+/-', width=5, font=20, relief='flat').place(x=10, y=350)

# Dot
pic_Dot = Image.open("Projects\Calculator\cc_img/full-stop.png").resize((40, 40))
pic_dot = ImageTk.PhotoImage(pic_Dot)
Dot = tk.Button(ws, image=pic_dot, relief='flat', bg='White')
Dot.place(x=170, y=350)

# Equal
pic_Eq = Image.open("Projects\Calculator\cc_img\equal.png").resize((40, 40))
pic_eq = ImageTk.PhotoImage(pic_Eq)
Equal = tk.Button(ws, image=pic_eq, relief='flat', bg='white')
Equal.place(x=245, y=350)

# Zero
pic_0 = Image.open("Projects\Calculator\cc_img\zero.png").resize((40, 40))
pic_ze = ImageTk.PhotoImage(pic_0)
Zero = tk.Button(ws, image=pic_ze, relief='flat', bg='white')
Zero.place(x=95, y=350)

ws.mainloop()
