# from tkinter import *
# from PIL import ImageTk, Image


# ws = Tk()
# ws.title('Image Resize')
# ws.geometry('500x500')
# ws.config(bg = '#FFE873')

# Label(ws, text = 'Width', width = 8, background = "Red", foreground = "Yellow"). place(x = 0, y = 0)
# width = Entry(ws, width = 10)
# width.insert(END, 300)
# width.place(x = 80, y = 0)

# Label(ws, text = 'Height', width = 8, background = "Yellow", foreground = "Red").place(x = 0, y = 20)
# height = Entry(ws,width = 10)
# height.insert(END, 350)
# height.place(x = 80, y = 20)

# disp_img = Label(ws)
# disp_img.place(x = 80, y = 80)

# def resize():
#     image = Image.open("PY4Y\Level_2\images\png2.png")
#     w = int(width.get())
#     h = int(height.get())
#     resize_img = image.resize((w,h))
#     img = ImageTk.PhotoImage(resize_img)
#     disp_img.config(image = img)
#     disp_img.image = img

# resize_btn = Button(ws, text = 'Resize', command = resize)
# resize_btn.place(x = 50, y = 50)



# ws.mainloop()

print("**********")

# from tkinter import *
# from PIL import ImageTk, Image
# import webbrowser

# ws = Tk()
# ws.title('Youtube')
# ws.geometry('504x500')

# def openbrowser ():
#     webbrowser.open('https://www.youtube.com/')

# img = Image.open('PY4Y\Level_2\images\maxresdefault.jpg')


# resized_img = img.resize((500,500))
# bg = ImageTk.PhotoImage(resized_img)

# disp_img = Label(ws, image = bg).place(x = 0, y = 0)

# btn = Button(ws, text = 'EXPLORE MORE', command = openbrowser, width = 20, height = 1, relief = SOLID, font = ('arial', 18))
# btn.place(x = 100, y = 320)

# ws.mainloop()

# print("**********")