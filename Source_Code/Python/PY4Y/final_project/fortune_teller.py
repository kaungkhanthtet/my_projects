import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import random
from tkinter import ttk
from tkinter import messagebox as mb

ws = tk.Tk()
ws.title('Fortune Teller')
ws.geometry('515x700')
ws.config(bg = '#192841')

tk.Label(ws, text = 'Name :', width = 30, font = 'Consolas 10 bold', bg = "#CCFFFF").place(x = 18, y = 20)
tk.Label(ws, text = 'Birth Date :', width = 30, font = 'Consolas 10 bold', bg = "#CCFFFF").place(x = 18, y = 50)
tk.Label(ws, text = 'Number of Questions', width = 30, font = 'Consolas 10 bold', bg = "#CCFFFF").place(x = 18, y = 80)
tk.Label(ws, text = 'Content you want to ask', width = 30, font = 'Consolas 10 bold', bg = "#CCFFFF").place(x = 18, y = 140)

years = [j for j in range(1900,2013)]
year_cb = ttk.Combobox(ws, values = years, width = 5, font = 'Bahnschrift 10 bold', foreground = '#3399FF')
year_cb.place(x = 405, y = 50)
year_cb.set("YEAR")

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months_cb = ttk.Combobox(ws, values = months, width = 10, font = 'Bahnschrift 10 bold', foreground = '#3399FF')
months_cb.place(x = 250, y = 50)
months_cb.set("MONTH")

days = [i for i in range (1,32)]
days_cb = ttk.Combobox(ws, values = days, width = 4, font = 'Bahnschrift 10 bold', foreground = '#3399FF')
days_cb.place(x = 349, y = 50)
days_cb.set("DAY")

name = tk.Entry(ws, width = 30, font = 'Bahnschrift 10 bold', relief='solid', fg = '#3399FF')
name.place(x = 250, y = 20)

options_1 = [1, 3, 5, 10]
cb_1 = ttk.Combobox(ws, values = options_1, width = 13, font='Carlito 10 bold', foreground = '#33FF00')
cb_1.place(x = 18, y = 110)
cb_1.set("0")

options_2 = ["Relationship", "Finance", "Career", "Health", "Personality", "Potential"]
cb_2 = ttk.Combobox(ws, values = options_2, width = 13, font='Carlito 10 bold', foreground = '#33FF00')
cb_2.place(x = 18, y = 170)
cb_2.set("Options")

def choice():
    global attempts
    attempts = int(cb_1.get())

pic_6 = Image.open("PY4Y/final_project\img\ok.png").resize((30,30))
pic_7 = ImageTk.PhotoImage(pic_6)
Con = Button(ws, image = pic_7, command = choice, bg = '#192841', relief = 'flat')
Con.place(x = 140, y = 103)

def click_here():
    m = months_cb.get()
    d = int(days_cb.get())
    global zs_l
    zs_l = Label(ws, width = 11, text = ' ', bg = '#192841', font='Carlito 12 bold', fg = 'White')
    zs_l.place(x = 313, y = 190)
    global zs
    zs = tk.Label(ws, bg = '#192841')
    zs.place(x = 320, y = 80)
    p_1 = Image.open("PY4Y/final_project\img/aquarius.png").resize((100,100))
    p_2 = Image.open("PY4Y/final_project\img\pisces.png").resize((100,100))
    p_3 = Image.open("PY4Y/final_project\img/aries.png").resize((100,100))
    p_4 = Image.open("PY4Y/final_project\img/taurus.png").resize((100,100))
    p_5 = Image.open("PY4Y/final_project\img\gemini.png").resize((100,100))
    p_6 = Image.open("PY4Y/final_project\img\cancer.png").resize((100,100))
    p_7 = Image.open("PY4Y/final_project\img\leo.png").resize((100,100))
    p_8 = Image.open("PY4Y/final_project\img/virgo.png").resize((100,100))
    p_9 = Image.open("PY4Y/final_project\img\libra.png").resize((100,100))
    p_10 = Image.open("PY4Y/final_project\img\scorpio.png").resize((100,100))
    p_11 = Image.open("PY4Y/final_project\img\sagittarius.png").resize((100,100))
    p_12 = Image.open("PY4Y/final_project\img\capricorn.png").resize((100,100))
    if (m == "January" and d >= 20) or (m == "February" and d <= 18):
        img_zs = ImageTk.PhotoImage(p_1) 
        zs_l.config(text = 'Aquarius')
    elif (m == "February" and d >= 19) or (m == "March" and d <= 20):
        img_zs = ImageTk.PhotoImage(p_2)
        zs_l.config(text = 'Pisces')
    elif (m == "March" and d >= 21) or (m == "April" and d <= 19):
        img_zs = ImageTk.PhotoImage(p_3)
        zs_l.config(text = 'Aries')
    elif (m == "April" and d >= 20) or (m == "May" and d <= 20):
        img_zs = ImageTk.PhotoImage(p_4)
        zs_l.config(text = 'Taurus')
    elif (m == "May" and d >= 21) or (m == "June" and d <= 20):
        img_zs = ImageTk.PhotoImage(p_5)
        zs_l.config(text = 'Gemini')
    elif (m == "June" and d >= 21) or (m == "July" and d <= 22):
        img_zs = ImageTk.PhotoImage(p_6)
        zs_l.config(text = 'Cancer')
    elif (m == "July" and d >= 23) or (m == "August" and d <= 22):
        img_zs = ImageTk.PhotoImage(p_7)
        zs_l.config(text = 'Leo')
    elif (m == "August" and d >= 23)or (m == "September" and d <= 22):
        img_zs = ImageTk.PhotoImage(p_8)
        zs_l.config(text = 'Virgo')
    elif (m == "September" and d >= 23)or (m == "October" and d <= 22):
        img_zs = ImageTk.PhotoImage(p_9)
        zs_l.config(text = 'Libra')
    elif (m == "October" and d >= 23) or (m == "November" and d <= 21):
        img_zs = ImageTk.PhotoImage(p_10)
        zs_l.config(text = 'Scorpio')
    elif (m == "November" and d >= 22) or (m == "December" and d <= 21):
        img_zs = ImageTk.PhotoImage(p_11)
        zs_l.config(text = 'Sagittarius')
    else:
        img_zs = ImageTk.PhotoImage(p_12)
        zs_l.config(text = 'Capricorn')
    zs.config(image = img_zs)
    zs.image = img_zs
    


pic_8 = Image.open("PY4Y/final_project\img\click.png").resize((40,40))
pic_9 = ImageTk.PhotoImage(pic_8)
Con = Button(ws, image = pic_9, command = click_here, bg = '#192841', relief = 'flat')
Con.place(x = 465, y = 25)

def exit():
    ws.quit()

def nQ():
    global attempts
    if attempts == 1:
        if mb.askyesno("NOTICE", "You have done your last question. \nPress 'yes' to exit and 'no' to restart the game."):
            ws.quit()
        else:
            zs_l.destroy()
            zs.destroy()
            name.delete(0, END)
            year_cb.set("YEAR")
            months_cb.set("MONTH")
            days_cb.set("DAY")
            cb_2.set("Options")
            cb_1.set("0")
            img.destroy()
            img_1.destroy()
            img_2.destroy()
            l_1.destroy()
            l_2.destroy()
            l_3.destroy()
            re_b.destroy()
            ex_b.destroy()
            ml.destroy()
            ml_1.destroy()
            ml_2.destroy()
    attempts -= 1
    cb_2.set("Options")
    img.destroy()
    img_1.destroy()
    img_2.destroy()
    l_1.destroy()
    l_2.destroy()
    l_3.destroy()
    re_b.destroy()
    ex_b.destroy()
    ml.destroy()
    ml_1.destroy()
    ml_2.destroy()
    
Label(ws, width = 69, height = 23, bg = '#C8E7F2').place(x = 14, y = 285)

#Cards' meanings
global new_normaltc_m, new_reversedtc_m

normaltc_m = ['End of Cycle', 'Beginnings', 'Change', 'Metamorphosis','Reflection', 
'reckoning', 'Awakening', 'Cause and Effect', 'Clarity', 'Truth', 'inner strength', 
'bravery', 'compassion', 'focus', 'middle path', 'patience', 'finding meaning', 
'direction', 'control', 'willpower', 'addiction', 'materialism', 'playfulness', 'authority', 
'structure', 'control', 'fatherhood', 'motherhood', 'fertility', 'nature', 'innocence', 'new beginnings', 
'free spirit', 'sacrifice', 'release', 'martyrdom', 'contemplation', 'search for truth', 'inner guidance', 
'tradition', 'conformity', 'morality', 'ethics', 'intuitive', 'unconscious', 'inner voice', 'partnerships', 
'duality', 'union', 'willpower', 'desire', 'creation', 'manifestation', 'unconscious', 'illusions', 
'intuition', 'hope', 'faith', 'rejuvenation',  'joy', 'success', 'celebration', 'positivity', 
'sudden upheaval', 'broken pride', 'disaster', 'fulfillment', 'harmony', 'completion', 
'change', 'cycles', 'inevitable fate']
new_normaltc_m = []  
for iii in normaltc_m:
    new_normaltc_m.append(iii.title())
    
reversedtc_m = ['fear of change', 'holding on', 'stagnation', 'decay', 'lack of self awareness', 'doubt', 
'self loathing', 'dishonesty', 'unaccountability', 'unfairness', 'self doubt', 'weakness', 'insecurity', 'extremes', 
'excess', 'lack of balance', 'lack of control', 'lack of direction', 'aggression', 'freedom', 'release', 
'restoring control', 'tyranny', 'rigidity', 'coldness', 'dependence', 'smothering', 'emptiness', 'nosiness', 
'recklessness', 'taken advantage of', 'inconsideration', 'stalling', 'needless sacrifice', 'fear of sacrifice', 
'loneliness', 'isolation', 'lost your way', 'rebellion', 'subversiveness', 'new approaches', 'lack of center', 
'lost inner voice', 'repressed feelings', 'loss of balance', 'one-sidedness', 'disharmony', 'tricker', 'illusions', 
'out of touch', 'confusion', 'fear', 'misinterpretation', 'faithlessness', 'discouragement', 'insecurity', 
'negativity', 'depression', 'sadness', 'disaster avoided', 'delayed disaster', 'fear of suffering', 'incompletion', 
'no closure', 'no control', 'clinging to control', 'bad luck']
new_reversedtc_m = []  
for jj in reversedtc_m:
    new_reversedtc_m.append(jj.title())


def fun():
    #a
    global result
    if drew_card == chosen_card and chosen_card == a:
        m = new_normaltc_m
        random_taker = random.randrange(0,4)
        result = m[random_taker]
        #print('A')
    elif drew_card == chosen_card1 and chosen_card1 == a_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(0,4)
        result = m_r[random_taker_1]
        #print('Ar')
    #b
    elif drew_card == chosen_card and chosen_card == b:
        m = new_normaltc_m
        random_taker = random.randrange(4,7)
        result = m[random_taker]
        #print('B')
    elif drew_card == chosen_card1 and chosen_card1 == b_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(4,7)
        result = m_r[random_taker_1]
        #print('Br')

    #c
    elif drew_card == chosen_card and chosen_card == c:
        m = new_normaltc_m
        random_taker = random.randrange(7,10)
        result = m[random_taker]
        #print('C')
    elif drew_card == chosen_card1 and chosen_card1 == c_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(7,10)
        result = m_r[random_taker_1]
        #print('Cr')
    #d
    elif drew_card == chosen_card and chosen_card == d:
        m = new_normaltc_m
        random_taker = random.randrange(10,14)
        result = m[random_taker]
        #print('D')
    elif drew_card == chosen_card1 and chosen_card1 == d_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(10,13)
        result = m_r[random_taker_1]
        #print('Dr')
    #e
    elif drew_card == chosen_card and chosen_card == e:
        m = new_normaltc_m
        random_taker = random.randrange(14,17)
        result = m[random_taker]
        #print('E')
    elif drew_card == chosen_card1 and chosen_card1 == e_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(13,16)
        result = m_r[random_taker_1]
        #print('Er')
    #f
    elif drew_card == chosen_card and chosen_card == f:
        m = new_normaltc_m
        random_taker = random.randrange(17,20)
        result = m[random_taker]
        #print('F')
    elif drew_card == chosen_card1 and chosen_card1 == f_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(16,19)
        result = m_r[random_taker_1]
        #print('Fr')
    #g
    elif drew_card == chosen_card and chosen_card == g:
        m = new_normaltc_m
        random_taker = random.randrange(20,23)
        result = m[random_taker]
        #print('G')
    elif drew_card == chosen_card1 and chosen_card1 == g_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(19,22)
        result = m_r[random_taker_1]
        #print('Gr')
     #h
    elif drew_card == chosen_card and chosen_card == h:
        m = new_normaltc_m
        random_taker = random.randrange(23,27)
        result = m[random_taker]
        #print('H')
    elif drew_card == chosen_card1 and chosen_card1 == h_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(22,25)
        result = m_r[random_taker_1]
        #print('Hr')
    #i
    elif drew_card == chosen_card and chosen_card == ii:
        m = new_normaltc_m
        random_taker = random.randrange(27,30)
        result = m[random_taker]
        #print('I')
    elif drew_card == chosen_card1 and chosen_card1 == i_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(25,29)
        result = m_r[random_taker_1]
        #print('Ir')
    #j
    elif drew_card == chosen_card and chosen_card == j:
        m = new_normaltc_m
        random_taker = random.randrange(30,33)
        result = m[random_taker]
        #print('J')
    elif drew_card == chosen_card1 and chosen_card1 == j_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(29,32)
        result = m_r[random_taker_1]
        #print('Jr')
    #k
    elif drew_card == chosen_card and chosen_card == k:
        m = new_normaltc_m
        random_taker = random.randrange(33,36)
        result = m[random_taker]
        #print('K')
    elif drew_card == chosen_card1 and chosen_card1 == k_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(32,35)
        result = m_r[random_taker_1]
        #print('Kr')
    #l
    elif drew_card == chosen_card and chosen_card == l:
        m = new_normaltc_m
        random_taker = random.randrange(36,39)
        result = m[random_taker]
        #print('L')
    elif drew_card == chosen_card1 and chosen_card1 == l_one:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(35,38)
        result = m_r[random_taker_1]
        #print('Lr')
    #m
    elif drew_card == chosen_card and chosen_card == mm:
        m = new_normaltc_m
        random_taker = random.randrange(39,43)
        result = m[random_taker]
        #print('M')
    elif drew_card == chosen_card1 and chosen_card1 == m_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(38,41)
        result = m_r[random_taker_1]
        #print('Mr')
    #n
    elif drew_card == chosen_card and chosen_card == n:
        m = new_normaltc_m
        random_taker = random.randrange(43,46)
        result = m[random_taker]
        #print('N')
    elif drew_card == chosen_card1 and chosen_card1 == n_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(41,44)
        result = m_r[random_taker_1]
        #print('Nr')
    #o
    elif drew_card == chosen_card and chosen_card == o:
        m = new_normaltc_m
        random_taker = random.randrange(46,49)
        result = m[random_taker]
        #print('O')
    elif drew_card == chosen_card1 and chosen_card1 == o_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(44,47)
        result = m_r[random_taker_1]
        #print('Or')
    #p
    elif drew_card == chosen_card and chosen_card == p:
        m = new_normaltc_m
        random_taker = random.randrange(49,53)
        result = m[random_taker]
        #print('P')
    elif drew_card == chosen_card1 and chosen_card1 == p_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(47,50)
        result = m_r[random_taker_1]
        #print('Pr')
    #q
    elif drew_card == chosen_card and chosen_card == q:
        m = new_normaltc_m
        random_taker = random.randrange(53,56)
        result = m[random_taker]
        #print('Q')
    elif drew_card == chosen_card1 and chosen_card1 == q_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(50,53)
        result = m_r[random_taker_1]
        #print('Qr')
    #r
    elif drew_card == chosen_card and chosen_card == r:
        m = new_normaltc_m
        random_taker = random.randrange(56,59)
        result = m[random_taker]
        #print('R')
    elif drew_card == chosen_card1 and chosen_card1 == r_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(53,56)
        result = m_r[random_taker_1]
        #print('RR')
    #s
    elif drew_card == chosen_card and chosen_card == s:
        m = new_normaltc_m
        random_taker = random.randrange(59,63)
        result = m[random_taker]
        #print('S')
    elif drew_card == chosen_card1 and chosen_card1 == s_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(56,59)
        result = m_r[random_taker_1]
        #print('Sr')
    #t
    elif drew_card == chosen_card and chosen_card == t:
        m = new_normaltc_m
        random_taker = random.randrange(63,66)
        result = m[random_taker]
        #print('T')
    elif drew_card == chosen_card1 and chosen_card1 == t_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(59,62)
        result = m_r[random_taker_1]
        #print('Tr')
    #u
    elif drew_card == chosen_card and chosen_card == u:
        m = new_normaltc_m
        random_taker = random.randrange(66,69)
        result = m[random_taker]
        #print('U')
    elif drew_card == chosen_card1 and chosen_card1 == u_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(62,64)
        result = m_r[random_taker_1]
        #print('Ur')
    #v
    elif drew_card == chosen_card and chosen_card == v:
        m = new_normaltc_m
        random_taker = random.randrange(69,72)
        result = m[random_taker]
        #print('V')
    elif drew_card == chosen_card1 and chosen_card1 == v_1:
        m_r = new_reversedtc_m
        random_taker_1 = random.randrange(64,67)
        result = m_r[random_taker_1]
        #print('Vr')
    
def fun_1(def_label):
    fun()
    finalr = result
    def_label.config(text = finalr)

def draw():
    global attempts
    if attempts == 0:
        if mb.askyesno("WARNING", "You haven't said how many times will you pull the cards yet. \nOr would you like to exit from this app? \nPress 'yes' to exit and 'no' to restart."):
            ws.quit()
        else:
            mb.showinfo("NOTICE", "You can continue your game by filling how many times you would like to do.")
            return attempts
    global img
    img = tk.Label(ws, bg = '#C8E7F2')
    img.place(x = 20, y = 320)
    global img_1
    img_1 = tk.Label(ws, bg = '#C8E7F2')
    img_1.place(x = 182, y = 320)
    global img_2
    img_2 = tk.Label(ws, bg = '#C8E7F2')
    img_2.place(x = 343, y = 320)

    #Card_Meaning Labels
    global ml, ml_1, ml_2
    ml = Label(ws, text = ' ', width = 23, font = "Calibri 13 bold")
    ml.place(x = 40, y = 572)
    ml_1 = Label(ws, text = ' ', width = 23, font = "Calibri 13 bold")
    ml_1.place(x = 153, y = 604)
    ml_2 = Label(ws, text = ' ', width = 23, font = "Calibri 13 bold")
    ml_2.place(x = 260, y = 572)

    global a,b,c,d,e,f,g,h,ii,j,k,l,mm,n,o,p,q,r,s,t,u,v
    a = Image.open("PY4Y/final_project\img\death.png").resize((150,250))
    b = Image.open("PY4Y/final_project\img\judgement.png").resize((150,250))
    c = Image.open("PY4Y/final_project\img\justice.png").resize((150,250))
    d = Image.open( "PY4Y/final_project\img\strength.png").resize((150,250))
    e = Image.open("PY4Y/final_project\img/temperance.png").resize((150,250))
    f = Image.open("PY4Y/final_project\img/the_chariot.png").resize((150,250))
    g = Image.open("PY4Y/final_project\img/the_devil.png").resize((150,250))
    h = Image.open("PY4Y/final_project\img/the_emperor.png").resize((150,250))
    ii = Image.open("PY4Y/final_project\img/the_empress.png").resize((150,250))
    j = Image.open("PY4Y/final_project\img/the_fool.png").resize((150,250))
    k = Image.open("PY4Y/final_project\img/the_hanged_man.png").resize((150,250))
    l = Image.open("PY4Y/final_project\img/the_hermit.png").resize((150,250))
    mm = Image.open("PY4Y/final_project\img/the_hierophant.png").resize((150,250))
    n = Image.open("PY4Y/final_project\img/the_high_priestess.png").resize((150,250))
    o = Image.open("PY4Y/final_project\img/the_lovers.png").resize((150,250))
    p = Image.open("PY4Y/final_project\img/the_magician.png").resize((150,250))
    q = Image.open("PY4Y/final_project\img/the_moon.png").resize((150,250))
    r = Image.open("PY4Y/final_project\img/the_star.png").resize((150,250))
    s = Image.open("PY4Y/final_project\img/the_sun.png").resize((150,250))
    t = Image.open("PY4Y/final_project\img/the_tower.png").resize((150,250))
    u = Image.open("PY4Y/final_project\img/the_world.png").resize((150,250))
    v = Image.open("PY4Y/final_project\img\wheel_of_fortune.png").resize((150,250))
    tarot = [a,b,c,d,e,f,g,h,ii,j,k,l,mm,n,o,p,q,r,s,t,u,v]
    global a_1, b_1, c_1, d_1, e_1, f_1, g_1, h_1, i_1, j_1, k_1, l_one, m_1, n_1, o_1, p_1, q_1, r_1, s_1, t_1, u_1, v_1
    a_1, b_1, c_1, d_1, e_1, f_1, g_1, h_1, i_1, j_1, k_1, l_one, m_1, n_1, o_1, p_1, q_1, r_1, s_1, t_1, u_1, v_1 = a.rotate(180), b.rotate(180), c.rotate(180), d.rotate(180), e.rotate(180), f.rotate(180), g.rotate(180), h.rotate(180), ii.rotate(180), j.rotate(180), k.rotate(180), l.rotate(180), mm.rotate(180), n.rotate(180), o.rotate(180), p.rotate(180), q.rotate(180), r.rotate(180), s.rotate(180), t.rotate(180), u.rotate(180), v.rotate(180)
    
    new_tarot = [a_1, b_1, c_1, d_1, e_1, f_1, g_1, h_1, i_1, j_1, k_1, l_one, m_1, n_1, o_1, p_1, q_1, r_1, s_1, t_1, u_1, v_1]
    global chosen_card, chosen_card1
    global i
    for i in range(0,3):
        choice = random.randrange(0,22)
        chosen_card = tarot[choice]
        choice_1 = random.randrange(0,22)
        chosen_card1 = new_tarot[choice_1]
        global drew_img, drew_card
        card = [chosen_card, chosen_card1]
        final_card = random.randrange(0,2)
        drew_card = card[final_card]   
        drew_img = ImageTk.PhotoImage(drew_card)
        if i == 0:
            img.config(image = drew_img)
            img.image = drew_img
            fun_1(ml)
            
        elif i == 1:
            img_1.config(image = drew_img)
            img_1.image = drew_img
            fun_1(ml_1)

        else:
            img_2.config(image = drew_img)
            img_2.image = drew_img
            fun_1(ml_2)
            
    #Tarot Card Labels
    global l_1, l_2, l_3
    l_1 = tk.Label(ws, text = 'Past', width = 10, bg = '#00FF99', font = "Calibri 13 bold", relief = 'raise')
    l_1.place(x = 50, y = 295)
    l_2 = tk.Label(ws, text = 'Present', width = 10, bg = '#FF0000', font = "Calibri 13 bold", relief = 'raise')
    l_2.place(x = 212, y = 295)
    l_3 = tk.Label(ws, text = 'Future', width = 10, bg = '#FFFF00', font = "Calibri 13 bold", relief = 'raise')
    l_3.place(x = 373, y = 295)

    #Buttons
    global pic_2, pic_3, re_b, pic_4, pic_5,ex_b
    pic_2 = Image.open("PY4Y/final_project\img\infinity.png").resize((50,50))
    pic_3 = ImageTk.PhotoImage(pic_2)
    re_b = tk.Button(ws, image = pic_3, command = nQ, bg = '#192841', relief = 'flat')
    re_b.place(x = 150, y = 640) 
    pic_4 = Image.open("PY4Y/final_project\img\log-out.png").resize((50,50))
    pic_5 = ImageTk.PhotoImage(pic_4) 
    ex_b = tk.Button(ws, image = pic_5, command = exit, bg = '#192841', relief = 'flat')
    ex_b.place(x = 310, y = 640)

pic = Image.open("PY4Y/final_project\img/tarot.png").resize((50,50))
pic_1 = ImageTk.PhotoImage(pic)
pull_card = tk.Button(ws, width = 50, image = pic_1, command = draw, bg = '#192841', relief = 'flat')
pull_card.place(x = 230, y = 225)

ws.mainloop()