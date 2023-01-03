# age = 14
# name = "Kevin"
# to_print= f"My name is {name}. I am {age} years old."
# print(to_print)

print("**********")

# import random


# names = ["Nathan", "Kaung Khant Htet", "Sai Win Naing", "Htet Wai Yan Aung"]
# choice = random.randint(0,3)
# print(choice)
# print(names[choice])

# print("**********")

# import tkinter as tk
# # from tkinter import *
# #Create a window and add a title
# window = tk.Tk()
# window.title("Greet")

# def greet():
#     name = "Hello," + my_text_box.get()
#     name_label.config(text=name)

# def clear():
#     my_text_box.delete(0, tk.END)
#     name_label.config(text=" ")

# my_label = tk.Label(window, text="Enter your name:")
# my_label.grid(row=0, column=0) 
# name_label = tk.Label(window, text = " ")
# name_label.grid(row=1, column=0) 
# my_text_box = tk.Entry(window, width=20) 
# my_text_box.grid(row=0, column=1)


# my_button = tk.Button(window, text="Hello!", command=greet) 
# my_button.grid(row=1, column=1)

# clear_button = tk.Button(window, text="Clear", command=clear) 
# clear_button.grid(row=2, column=1)

# window.mainloop()

# print("**********")

# import tkinter as tk
# #Create a window and add a title
# window = tk.Tk()

# def clear():
#     var.set("Select any language:")

# options = ("C++","Java","Python","JavaScript", "Rust", "GoLang")
# var = tk.IntVar()
# var.set("Select any language:")
# my_dropdown = tk.OptionMenu(window, var, *options) 
# my_dropdown.grid()

# clear_button = tk.Button(window, text="Clear", command=clear) 
# clear_button.grid()

# window.mainloop()

print("**********")

from datetime import date
today = date.today()
print(today)
print(today.year)

birthDate = date(1998, 9, 10)
print(birthDate)

age = today.year-birthDate.year
print(age)

print("**********")




