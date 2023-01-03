# import tkinter as tk

# #Create a window and add a title
# window = tk.Tk()
# window.title("Greet")

# #Main code
# my_label = tk.Label(window,text= "Enter your name :")
# my_label.grid(row=0, column=0)

# name_label = tk.Label(window, text= " ")
# name_label.grid(row=1,column=0)

# def greet():
#     name = "Hello, " + my_text_box.get()
#     name_label.config(text = name)
    
# my_button = tk.Button(window, text="Hello!",command = greet)
# my_button.grid(row=1,column=1)

# my_text_box = tk.Entry(window, width = 20)
# my_text_box.grid(row = 0, column = 1)

# #Start the infinite loop which watches for changes 
# window.mainloop()

print("**********")

# import tkinter as tk

# #Create a window and add a title
# window = tk.Tk()
# window.title("Greet")

# #Main code
# my_label = tk.Label(window,text= "Enter your name :")
# my_label.grid(row=0, column=0)

# name_label = tk.Label(window, text= " ")
# name_label.grid(row=1,column=0)

# def greet():
#     name = "Hello, " + my_text_box.get()
#     name_label.config(text = name)
    
# my_button = tk.Button(window, text="Hello!",command = greet)
# my_button.grid(row=1,column=1)

# my_text_box = tk.Entry(window, width = 20)
# my_text_box.grid(row = 0, column = 1)

# #Start the infinite loop which watches for changes 
# window.mainloop()

print("**********")
#Exercise

# from tkinter import *

# window = Tk()
# window.title("Temperature Converter")
# window.geometry("400x400")

# text_box = Entry(window, width = 10)
# text_box.place(x = 30, y = 0)

# label_1 = Label(window, text = "Celsius")
# label_1.place(x = 100, y = 0)

# label_2 = Label(window, text = " ")
# label_2.place(x = 0, y = 20)

# def convert ():
#     con = float(text_box.get())* (9/5) + 32
#     F = "is equal to "+ str(con) +" Fahrenheit"
#     label_2.config(text = F)

# button = Button(window, text = "Convert", command = convert)
# button.place(x = 35, y = 45)

# window.mainloop()

print("**********")

#Exercise 2

# from tkinter import *
# from PIL import Image, ImageTk

# window = Tk()
# window.title("Image Resizing")
# window.geometry("500x500")
# window.config(bg = '#00CCFF')

# label_1 = Label(window, width = 10, text = " Width ", foreground = "red")
# label_1.place(x = 10, y = 0)

# box_1 = Entry(window, width=10, foreground = "orange")
# box_1.place(x = 100, y = 0)

# label_2 = Label(window, width = 10, text = "Height", foreground = "Red")
# label_2.place(x = 10, y = 25)

# box_2 = Entry(window, width=10, foreground = "orange")
# box_2.place(x = 100, y = 25)

# disp_img = Label(window)
# disp_img.place(x = 100, y = 150)

# def resize():
#     image = Image.open("PY4Y\Level_2\images\png30.png")
#     w = int(box_1.get())
#     h = int(box_2.get())
#     resizing = image.resize((w,h))
#     img = ImageTk.PhotoImage(resizing)
#     disp_img.config(image = img)
#     disp_img.image = img


# button = Button(window, text = "Resize", command = resize, foreground = "brown", width = 8)
# button.place(x = 60, y = 50)

# window.mainloop()

print("**********")

# from tkinter import *

# window = Tk()
# window.title("Temperature Converter")
# window.geometry("400x400")

# text_box = Entry(window, width = 12)
# text_box.grid(row = 0, column = 1)

# label_1 = Label(window, text = "Celsius", foreground='Blue')
# label_1.grid(row = 0, column = 2)

# label_2 = Label(window, width = 10, text = " ", background = "Red", foreground='Yellow')
# label_2.grid(row = 1, column = 1)

# label_3 = Label(window, text = "is equal to", foreground='Green')
# label_3.grid(row = 1, column = 0)

# label_4 = Label(window, text = " Fahrenheit", foreground='Green')
# label_4.grid(row = 1, column = 2)

# def convert ():
#     con = float(text_box.get())* (9/5) + 32
#     F = con
#     label_2.config(text = F)

# button = Button(window, text = "Convert", command = convert, foreground='Orange')
# button.grid(row = 2, column = 1)

# window.mainloop()

# print("**********")
# from tkinter import *
# from tkinter import messagebox as mb

# ws = Tk()
# ws.title('MessageBox')
# ws.geometry('300x300')

# def answer ():
#     mb.showerror("Answer", "Sorry, no answer available")

# def callback():
#     if mb.askyesno('Verify', "Really quit?"):
#         mb.showwarning('Yes', 'Not yet implemented')
#     else:
#         mb.showinfo('No', 'Quit has been called')

# Button(ws, text = 'Quit', command = callback).pack()
# Button(ws, text = 'Answer', command = answer).pack()
# ws.mainloop()


