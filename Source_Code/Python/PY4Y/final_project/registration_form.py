from tkinter import *

ws = Tk()
ws.title('Registration Form')
ws.geometry("500x230")
ws.config(bg = '#CCCCFF')

Label(ws, text = '', bg = '#CCCCFF').grid(row = 0, column = 0)
Label(ws, text = "Course Registration Form", width = 23, font = "System 16").grid(row = 1, column = 0)

my_name = Label(ws, text = "Name :", width = 30, bg = '#CCCCFF', font = 'System', fg = 'White')
my_name.grid(row = 2, column = 0)

my_email = Label(ws, text = "Email :", width = 10, bg = '#CCCCFF', font = 'System', fg = 'White')
my_email.grid(row = 3, column = 0)

my_age = Label(ws, text = "Age :", width = 10, bg = '#CCCCFF', font = 'System', fg = 'White')
my_age.grid(row = 4, column = 0)

my_gender = Label(ws, text = "Gender :", width = 10, bg = '#CCCCFF', font = 'System', fg = 'White')
my_gender.grid(row = 5, column = 0)

my_number = Label(ws, text = "Contact number :", width = 20, bg = '#CCCCFF', font = 'System', fg = 'White')
my_number.grid(row = 6, column = 0)

my_course = Label(ws, text = "Select course :", width = 15, bg = '#CCCCFF', font = 'System', fg = 'White')
my_course.grid(row = 7, column = 0)

name = Entry(ws, width = 40, relief = 'flat')
name.grid(row = 2, column = 1)

email = Entry(ws, width = 40, relief = 'flat')
email.grid(row = 3, column = 1)

age = Entry(ws, width = 40, relief = 'flat')
age.grid(row = 4, column = 1)

num = Entry(ws, width = 40, relief = 'flat')
num.grid(row = 6, column = 1)

options = ("Male", "Female", "Other")
menu = StringVar()
menu.set("Choose your gender : ")
gender = OptionMenu(ws, menu, *options)
gender.grid(row = 5, column = 1)

options_1 = ("PY4Y", "UIX4E", "IGCSE(ICT)", "3D4Y", "WL4Y", "AI4Y", "RB4Y", "CCS", "CCT", "AL4Y", 'IGCSE(CS)')
menu_1 = StringVar()
menu_1.set("Choose your course : ")
course = OptionMenu(ws, menu_1, *options_1)
course.grid(row = 7, column = 1)

def submit():
    path = "PY4Y/final_project/ud.txt"
    new_file = open(path,"a")
    text_line = name.get()+"/"+ email.get()+"/"+ age.get()+"/"+ menu.get()+"/"+ num.get()+"/"+ menu_1.get()+"\n"
    new_file.write(text_line)
    new_file.close()

submittion = Button(ws, width = 20, text = "Submit", command = submit, relief = 'flat', bg = '#CCCCFF', font = 'Calibri 12 bold')
submittion.grid(row = 8, column = 0)

def clear():
    name.delete(0,END)
    email.delete(0,END)
    age.delete(0,END)
    num.delete(0,END)
    menu.set("Choose your gender : ")
    menu_1.set("Choose your course : ")

cleaning = Button(ws, width = 20, text = "Clear", command = clear, relief = 'flat', bg = '#CCCCFF', font = 'Calibri 12 bold')
cleaning.grid(row = 8, column = 1)

ws.mainloop()