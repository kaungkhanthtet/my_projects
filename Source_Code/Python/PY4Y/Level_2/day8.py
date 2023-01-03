#Drop - Down menu

#Integer

# from tkinter import *
#Create a window and add a title
# window = Tk()
# window.geometry("500x500")
# window.title("Greet")

#Main code

# options = (1,2,3)
# menu = IntVar()
# menu.set("choose : ")
# my_dropdown = OptionMenu(window, menu, *options)
# my_dropdown.grid()


#Start the infinite loop which watches for changes 
# window.mainloop()

#String

# from tkinter import *

# window = Tk()
# window.geometry("500x500")
# window.title("Programming")

# options = ("C++", "Java", "Python", "JavaScript", "Rust", "GoLang")
# menu = StringVar()
# menu.set("Select Any Language : ")
# my_dropdown = OptionMenu(window, menu, *options)
# my_dropdown.place(x = 160, y = 0)

# window.mainloop()

print("**********")

# from tkinter import *

# window = Tk()
# window.title("My Photo")
# window.geometry("700x1000")

# pic = PhotoImage(file = "PY4Y\Level_2\images\png2.png")
# img_lable = Label(window, image = pic).pack()

# window.mainloop()
print("**********")

# from tkinter import *
# from PIL import Image, ImageTk

# window = Tk()
# window.title("Image Resizing ...")
# window.geometry("300x300")

# myBaby= Image.open("PY4Y\Level_2\images\png2.png")

# #Resize the Image using resize method
# resized_image= myBaby.resize((300,300))

# #Creating an image object that compatible with tkinter

# img = ImageTk.PhotoImage(resized_image)


# disp_img = Label(window, image=img)
# disp_img.grid(row=0, column=0)
# window. mainloop()

print("**********")

# def resize_func():
#     image = Image.open("images\8306105346_59d83438ed.jpg")
#     w = int(width.get())
#     h = int(height.get())
#     resize_img = image.resize((w, h))
#     img = ImageTk.PhotoImage(resize_img)
#     disp_img.config(image=img)
#     disp_img.image = img
