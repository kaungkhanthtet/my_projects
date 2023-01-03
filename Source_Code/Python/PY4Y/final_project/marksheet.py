from tkinter import *

ws = Tk()
ws.title('Marksheet Application')
ws.geometry('500x300')
ws.config(bg = '#FFFFCC')

Label(ws,text = 'Name :', width = 10, bg = '#FFFFCC', font = 'Times 10').grid(row = 0, column = 0)
Label(ws,text = 'Roll.No :', width = 10, bg = '#FFFFCC', font = 'Times 10').grid(row = 1, column = 0)
Label(ws,text = 'Srl.No', width = 10, bg = '#CCFFCC', font = 'Times 10').grid(row = 2, column = 0)
Label(ws,text = '1 :', width = 10, bg = '#FFFFCC', font = 'Calibri 10 bold').grid(row = 3, column = 0)
Label(ws,text = '2 :', width = 10, bg = '#FFFFCC', font = 'Calibri 10 bold').grid(row = 4, column = 0)
Label(ws,text = '3 :', width = 10, bg = '#FFFFCC', font = 'Calibri 10 bold').grid(row = 5, column = 0)
Label(ws,text = '4 :', width = 10, bg = '#FFFFCC', font = 'Calibri 10 bold').grid(row = 6, column = 0)
Label(ws,text = '5 :', width = 10, bg = '#FFFFCC', font = 'Calibri 10 bold').grid(row = 7, column = 0)
Label(ws,text = '6 :', width = 10, bg = '#FFFFCC', font = 'Calibri 10 bold').grid(row = 8, column = 0)

Label(ws,text = 'Subject', width = 15, bg = '#CCFFCC', font = 'Times 10').grid(row = 2, column = 1)
Label(ws,text = 'Myanmar', width = 15, font = 'Verdana 10 ', bg = '#FFFFCC').grid(row = 3, column = 1)
Label(ws,text = 'English', width = 15, font = 'Verdana 10 ', bg = '#FFFFCC').grid(row = 4, column = 1)
Label(ws,text = 'Mathematics', width = 15, font = 'Verdana 10 ', bg = '#FFFFCC').grid(row = 5, column = 1)
Label(ws,text = 'Science', width = 15, font = 'Verdana 10 ', bg = '#FFFFCC').grid(row = 6, column = 1)
Label(ws,text = 'Computer Science', width = 15, font = 'Verdana 10 ', bg = '#FFFFCC').grid(row = 7, column = 1)
Label(ws,text = 'History', width = 15, font = 'Verdana 10 ', bg = '#FFFFCC').grid(row = 8, column = 1)

name = Entry(ws, width = 20)
name.grid(row = 0, column = 1)

roll_num = Entry(ws, width = 20)
roll_num.grid(row = 1, column = 1)

Label(ws,text = 'Grade (A, B, C, D, E, F)', width = 17, bg = '#CCFFCC', font = 'Times 10').grid(row = 2, column = 2)

Myan = Entry(ws, width = 20)
Myan.grid(row = 3, column = 2)

Eng = Entry(ws, width = 20)
Eng.grid(row = 4, column = 2)

Maths = Entry(ws, width = 20)
Maths.grid(row = 5, column = 2)

Sci = Entry(ws, width = 20)
Sci.grid(row = 6, column = 2)

Cs = Entry(ws, width = 20)
Cs.grid(row = 7, column = 2)

His = Entry(ws, width = 20)
His.grid(row = 8, column = 2)

Label(ws, text = ' ', bg = '#FFFFCC').grid(row = 0,column = 3)

Label(ws,text = 'Credit Obtained', width = 12, bg = '#CCFFCC', font = 'Times 10').grid(row = 2, column = 4)
b = Label(ws,text = ' ', width = 12, bg = '#FFFFCC')
b.grid(row = 3, column = 4)
e = Label(ws,text = ' ', width = 12, bg = '#FFFFCC')
e.grid(row = 4, column = 4)
m = Label(ws,text = ' ', width = 12, bg = '#FFFFCC')
m.grid(row = 5, column = 4)
s = Label(ws,text = ' ', width = 12, bg = '#FFFFCC')
s.grid(row = 6, column = 4)
cs = Label(ws,text = ' ', width = 12, bg = '#FFFFCC')
cs.grid(row = 7, column = 4)
h = Label(ws,text = ' ', width = 12, bg = '#FFFFCC')
h.grid(row = 8, column = 4)

Label(ws,text = 'Total Credit', width = 10, bg = '#FFFFCC', font = 'Times 10 bold', fg = '#003300').grid(row = 9, column = 2)
Label(ws,text = 'AVG', width = 10, bg = '#FFFFCC', font = 'Times 10 bold', fg = '#003300').grid(row = 10, column = 2)

tc = Label(ws,text = ' ', width = 12, bg = '#CCCFFF')
tc.grid(row = 9, column = 4)
avg = Label(ws,text = ' ', width = 12, bg = '#00FFFF')
avg.grid(row = 10, column = 4)

def submit():
    path = "PY4Y/final_project\student_profile.txt"
    new_file = open(path,"a")
    text_line = name.get()+"/"+ roll_num.get()+"/"+ Myan.get()+"/"+ Eng.get()+"/"+ Maths.get()+"/"+ Sci.get()+"/"+Cs.get()+"/"+ His.get()+"\n"
    new_file.write(text_line)
    new_file.close()

    mm = Myan.get()
    en = Eng.get()
    ma = Maths.get()
    sci = Sci.get()
    c_s = Cs.get()
    his = His.get()

    #Myanmar
    if mm == "A":
        mm = 90
        b.config(text = mm)
    elif mm == "B":
        mm = 80
        b.config(text = mm)
    elif mm == "C":
        mm = 70
        b.config(text = mm)
    elif mm == "D":
        mm = 50
        b.config(text = mm)
    elif mm == "E":
        mm = 40
        b.config(text = mm)
    else:
        mm = 0
        b.config(text = mm)
    #English
    if en == "A":
        en = 90
        e.config(text = en)
    elif en == "B":
        en = 80
        e.config(text = en)
    elif en == "C":
        en = 70
        e.config(text = en)
    elif en == "D":
        en = 50
        e.config(text = en)
    elif en == "E":
        en = 40
        e.config(text = en)
    else:
        en = 0
        e.config(text = en)
    #Mathematics
    if ma == "A":
        ma = 90
        m.config(text = ma)
    elif ma == "B":
        ma = 80
        m.config(text = ma)
    elif ma == "C":
        ma = 70
        m.config(text = ma)
    elif ma == "D":
        ma = 50
        m.config(text = ma)
    elif ma == "E":
        ma = 40
        m.config(text = ma)
    else:
        ma = 0
        b.config(text = ma)
    #Science
    if sci == "A":
        sci = 90
        s.config(text = sci)
    elif sci == "B":
        sci = 80
        s.config(text = sci)
    elif sci == "C":
        sci = 70
        s.config(text = sci)
    elif sci == "D":
        sci = 50
        s.config(text = sci)
    elif sci == "E":
        sci = 40
        s.config(text = sci)
    else:
        sci = 0
        s.config(text = sci)
    #Computer Science
    if c_s == "A":
        c_s = 90
        cs.config(text = c_s)
    elif c_s == "B":
        c_s = 80
        cs.config(text = c_s)
    elif c_s == "C":
        c_s = 70
        cs.config(text = c_s)
    elif c_s == "D":
        c_s = 50
        cs.config(text = c_s)
    elif c_s == "E":
        c_s = 40
        cs.config(text = c_s)
    else:
        c_s = 0
        cs.config(text = c_s)
    #History
    if his == "A":
        his = 90
        h.config(text = his)
    elif his == "B":
        his = 80
        h.config(text = his)
    elif his == "c":
        his = 70
        h.config(text = his)
    elif his == "D":
        his = 50
        h.config(text = his)
    elif his == "E":
        his = 40
        h.config(text = his)
    else:
        his = 0
        h.config(text = his)
    total = mm+en+ma+sci+c_s+his
    tc.config(text = total)
    average = (mm+en+ma+sci+c_s+his)/6
    avg.config(text = average)

Button(ws, text = 'Submit', command = submit).grid(row = 11, column = 1)

ws.mainloop()
    

