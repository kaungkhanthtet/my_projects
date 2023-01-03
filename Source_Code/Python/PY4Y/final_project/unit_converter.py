from tkinter import *
from PIL import ImageTk, Image

ws = Tk()
ws.title('Unit Converter')
ws.geometry('330x270')
ws.config(bg = '#FFCC66')

label_1 = Label(ws, width = 22, text = 'Enter Your Number Below', bg = '#FFCC66', font = 'System 10 bold', fg = '#CC3300')
label_1.place(x = 25, y = 30)
label_2 = Label(ws, width = 20, text = 'Result below', bg = '#FFCC66', font = 'System 10 bold', fg = '#0066CC')
label_2.place(x = 20, y = 120)
label_3 = Label(ws, width = 20, text = " ", font = 'System 10 bold', fg = '#FF6600', bg = 'White')
label_3.place(x = 30, y = 165)
input = Entry(ws, width = 20, relief = 'flat', font = 'System 10 bold', fg = '#0066CC')
input.place(x = 30, y = 75)
pic = Image.open("PY4Y/final_project\img\down-arrow.png").resize((30,30))
img = ImageTk.PhotoImage(pic)
label_4 = Label(ws, image = img, bg = '#FFCC66').place(x = 150, y = 115)

options = ("m", "cm", "kg", "pounds")
menu = StringVar()
menu.set(" ")
unit = OptionMenu(ws, menu, *options)
unit.place(x = 220, y = 70)

options = ("m", "cm", "kg", "pounds")
menu_1 = StringVar()
menu_1.set(" ")
unit_1 = OptionMenu(ws, menu_1, *options)
unit_1.place(x = 220, y = 160)

def convert():
    num = float(input.get())
    ip = str(menu.get())
    ip_1 = str(menu_1.get())
    global result
    result = 0
    if ip == "m" and ip_1 == "cm":
        result = num * 100
        label_3.config(text = str(result))

    elif ip == "cm" and ip_1 == "m":
        result = num * 0.01
        label_3.config(text = str(result))

    elif ip == "kg" and ip_1 == "pounds":
        result = num * 2.205
        label_3.config(text = str(result))

    elif ip == "pounds" and ip_1 == "kg":
        result = num * 0.453592
        label_3.config(text = str(result))

    else:
        label_3.config(text = "ERROR!")
    
my_button = Button(ws, width = 20, text = "Convert", command = convert, font = 'System 10 bold', fg = '#0066CC', bg = '#FFFF66', relief = 'solid').place(x = 70, y = 220)


ws.mainloop()                                                                                                                                           