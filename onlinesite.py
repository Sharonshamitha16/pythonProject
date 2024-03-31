import tkinter as tk
from tkinter import *
from tkinter import messagebox

import mysql.connector
from PIL import Image, ImageTk

connection = mysql.connector.connect(host = "localhost",user = "root",password = "Sharon@1602",database = "company")
cursor = connection.cursor()
connection.commit()
cursor.close()

mycursor = connection.cursor()
mycursor.execute("SELECT * FROM login_reg")
myresult = mycursor.fetchall()


def insert(scr9,username_txt,passwd_txt,addr_txt,email_txt,phone_txt):

    username = username_txt.get()
    passwd = passwd_txt.get()
    addr = addr_txt.get()
    email = email_txt.get()
    phone = phone_txt.get()

    connection = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "company")
    insert1 = ("insert into login_reg(username,passwd,addr,email,phone)values('"+username+"','"+passwd+"','"+addr+"','"+email+"',"+phone+")")
    cursor = connection.cursor()
    cursor.execute(insert1)
    connection.commit()
    cursor.close()

    mycursor = connection.cursor()
    mycursor.execute("select * from login_reg")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def submit():

    username = username_txt.get()
    passwd = passwd_txt.get()

    print("USERNAME :" +username)
    print("PASSWORD :" +passwd)

    scr1 = tk.Tk()
    root.destroy()
    scr1.geometry("1300x650+0+0")
    scr1.title("WELCOME TO SHOPPING CITY")
    scr1.configure(background ="THISTLE")


    flag = 0
    for x in myresult:
        if str(x[0]) == str(username) and str(x[1]) == str(passwd):
            flag = 1
            break

    if flag ==1:

        wlcme_frame = tk.Frame(scr1,bd = 0,relief = RIDGE)
        wlcme_frame.place(x = 50,y = 50,width = 1350,height = 700)

        lbl_username = tk.Label(wlcme_frame,text = "WELCOME TO SHOPPING CITY", font = ("ALGERIAN",40,"bold"),fg = "MAROON2")
        lbl_username.place(x = 0,y = 30,relwidth = 1)

        lbl_username = tk.Label(wlcme_frame,text = "Welcome "+ username,font = ("ALGERIAN",30,"bold"),fg = "PURPLE3")
        lbl_username.place(x = 0,y = 200,relwidth = 1)

        categ_btn = tk.Button(wlcme_frame,text = "VIEW CATEGORIES",font = ("ALGERIAN",30),bg = "LIGHT SKY BLUE",fg = "BLUE",command = categories)
        categ_btn.place(x = 450,y = 430,width = 500,height = 100)

    else:

        lbl_username = tk.Label(scr1,text = "USERNAME OR PASSWORD IS INCORRECT",font = ("ALGERIAN",30,"bold"),fg = "DARK VIOLET",bg = "PINK")
        lbl_username.place(x = 350,y = 200)

        lbl_username = tk.Label(scr1,text = "PLEASE TRY AGAIN",font = ("ALGERIAN",30,"bold"),fg = "DARK VIOLET",bg = "PINK")
        lbl_username.place(x = 520,y = 300)


def reg():

    scr9 = tk.Toplevel()
    scr9.title("SIGN UP FORM")
    scr9.geometry("1300x650+0+0")
    scr9.configure(bg = "LIGHT SKY BLUE")

    username_var1 = tk.StringVar()
    passwd_var1 = tk.StringVar()
    addr_var1 = tk.StringVar()
    email_var1 = tk.StringVar()
    phone_var1 = tk.StringVar()

    load1 = Image.open("register.png")
    photo1= ImageTk.PhotoImage(load1)
    img1_lbl = tk.Label(scr9,image = photo1)
    img1_lbl.image = photo1
    img1_lbl.place(x = 50,y = 65)

    reg_frame = tk.Frame(scr9,bd = 2,relief = RIDGE)
    reg_frame.place(x = 800,y = 50,width = 600,height = 700)

    login_lbl = tk.Label(reg_frame,text = "REGISTER HERE", font = ("ALGERIAN",25,"bold"),fg = "DARK ORCHID")
    login_lbl.place(x = 0,y = 30,relwidth = 1)

    username_lbl = tk.Label(reg_frame,text = "USERNAME :",font = ("ALGERIAN",20),fg = "DEEPPINK2")
    username_lbl.place(x = 50,y = 130)
    username_txt = tk.Entry(reg_frame,textvariable = username_var1,font = ("FOOTLIGHT MT LIGHT",20),bg = "SNOW",fg = "DEEPSKYBLUE2")
    username_txt.place(x = 250,y = 130)

    passwd_lbl = tk.Label(reg_frame,text = "PASSWORD :",font = ("ALGERIAN",20),fg = "DEEPPINK2")
    passwd_lbl.place(x = 50,y = 230)
    passwd_txt = tk.Entry(reg_frame,textvariable = passwd_var1,font = ("FOOTLIGHT MT LIGHT",20),bg = "SNOW",fg = "DEEPSKYBLUE2",show = "*")
    passwd_txt.place(x = 250,y = 230)

    addr_lbl = tk.Label(reg_frame,text = "ADDRESS :",font = ("ALGERIAN",20),fg = "DEEPPINK2")
    addr_lbl.place(x = 50,y = 330)
    addr_txt = tk.Entry(reg_frame,textvariable = addr_var1,font = ("FOOTLIGHT MT LIGHT",20),bg = "SNOW",fg = "DEEPSKYBLUE2")
    addr_txt.place(x = 250,y = 330)

    email_lbl = tk.Label(reg_frame,text = "EMAIL :",font = ("ALGERIAN",20),fg = "DEEPPINK2")
    email_lbl.place(x = 50,y = 430)
    email_txt = tk.Entry(reg_frame,textvariable = email_var1,font = ("FOOTLIGHT MT LIGHT",20),bg = "SNOW",fg = "DEEPSKYBLUE2")
    email_txt.place(x = 250,y = 430)

    phone_lbl = tk.Label(reg_frame,text = "PHONE NO :",font = ("ALGERIAN",20),fg = "DEEPPINK2")
    phone_lbl.place(x = 50,y = 530)
    phone_txt = tk.Entry(reg_frame,textvariable = phone_var1,font = ("FOOTLIGHT MT LIGHT",20),bg = "SNOW",fg = "MAGENTA")
    phone_txt.place(x = 250,y = 530)

    reg_btn = tk.Button(reg_frame,text = "REGISTER",font = ("ALGERIAN",20),bg = "ALICE BLUE",fg = "DARK ORCHID",command = lambda: insert(scr9,username_txt,passwd_txt,addr_txt,email_txt,phone_txt))
    reg_btn.place(x = 200,y = 630,width = 200,height = 50)


def categories():

    scr2 = tk.Tk()
    scr2.title("CATEGORIES FORM")
    scr2.geometry("1300x650+0+0")
    scr2.configure(bg = "AQUAMARINE")

    load2 = Image.open("categories.jpeg")
    photo2= ImageTk.PhotoImage(load2)
    img2_lbl = tk.Label(scr2,image = photo2)
    img2_lbl.place(x = 0,y = 0)
    img2_lbl.image = photo2

    categ_frame = tk.Frame(scr2,bd = 0,relief = RIDGE)
    categ_frame.place(x = 500,y = 20,width = 600,height = 700)

    categ_lbl = tk.Label(categ_frame,text = "ALL CATEGORIES", font = ("ALGERIAN",30,"bold"),fg = "LIME GREEN")
    categ_lbl.place(x = 15,y = 30,relwidth = 1)

    btn_categ = tk.Button(categ_frame,text = "EATABLES",font = ("ALGERIAN",25),bg = "LAVENDER",fg = "DEEPSKYBLUE2",command = eatables)
    btn_categ.place(x = 130,y = 70,width = 350,height = 70)

    btn_categ = tk.Button(categ_frame,text = "ELECTRONICS",font = ("ALGERIAN",25),bg = "LAVENDER",fg = "DEEPSKYBLUE2",command = electronics)
    btn_categ.place(x = 130,y = 170,width = 350,height = 70)

    btn_categ = tk.Button(categ_frame,text = "SPORTS",font = ("ALGERIAN",25),bg = "LAVENDER",fg = "DEEPSKYBLUE2",command = sports)
    btn_categ.place(x = 130,y = 270,width = 350,height = 70)

    btn_categ = tk.Button(categ_frame,text = "MEN'S FASHION",font = ("ALGERIAN",25),bg = "LAVENDER",fg = "DEEPSKYBLUE2",command = menfashion)
    btn_categ.place(x = 130,y = 370,width = 350,height = 70)

    btn_categ = tk.Button(categ_frame,text = "WOMEN'S FASHION",font = ("ALGERIAN",25),bg = "LAVENDER",fg = "DEEPSKYBLUE2",command = womenfashion)
    btn_categ.place(x = 130,y = 470,width = 350,height = 70)

    btn_categ = tk.Button(categ_frame,text = "BAG AND LUGGAGES",font = ("ALGERIAN",25),bg = "LAVENDER",fg = "DEEPSKYBLUE2",command = bagandluggages)
    btn_categ.place(x = 130,y = 570,width = 350,height = 70)


def eatables():

    scr3 = tk.Toplevel()
    scr3.title("EATABLES FORM")
    scr3.geometry("1300x650+0+0")
    scr3.configure(bg = "MEDIUM PURPLE")

    eat_frame = tk.Frame(scr3,bd = 0,relief = RIDGE)
    eat_frame.place(x = 50,y = 50,width = 1350,height = 700)

    load3 = Image.open("Eatables.jpeg")
    photo3 = ImageTk.PhotoImage(load3)
    img3_lbl = tk.Label(eat_frame,image = photo3)
    img3_lbl.place(x = 0,y = 0)
    img3_lbl.image = photo3

    load4 = Image.open("Eatables.jpeg")
    photo4 = ImageTk.PhotoImage(load4)
    img4_lbl = tk.Label(eat_frame,image = photo4)
    img4_lbl.place(x = 750,y = 0)
    img4_lbl.image = photo4

    load5 = Image.open("Eatables.jpeg")
    photo5 = ImageTk.PhotoImage(load5)
    img5_lbl = tk.Label(eat_frame,image = photo5)
    img5_lbl.place(x = 500,y = 0)
    img5_lbl.image = photo5

    eat_lbl = tk.Label(eat_frame,text = "EATABLES", font = ("ALGERIAN",35,"bold"),fg = "BLUE2")
    eat_lbl.place(x = 0,y = 0,relwidth = 1)

    btn_eat = tk.Button(eat_frame,text = " COKE",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command = COKE)
    btn_eat.place(x = 80,y = 200,width = 300,height = 100)

    btn_eat = tk.Button(eat_frame,text = "LAYS",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command = LAYS)
    btn_eat.place(x = 500,y = 200,width = 300,height = 100)

    btn_eat = tk.Button(eat_frame,text = "HIDE & SEEK",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command = HIDEANDSEEK)
    btn_eat.place(x = 900,y = 200,width = 300,height = 100)

    btn_eat = tk.Button(eat_frame,text = "MAGGI",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command = MAGGI)
    btn_eat.place(x = 300,y = 450,width = 300,height = 100)

    btn_eat = tk.Button(eat_frame,text = "LIMCA",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command = LIMCA)
    btn_eat.place(x = 750,y = 450,width = 300,height = 100)


def COKE():

    scr10 = tk.Toplevel()
    scr10.title("COKE - ADD TO CART")
    scr10.geometry("1300x650+0+0")
    scr10.configure(bg = "TOMATO")

    coke_frame = tk.Frame(scr10,bd = 0,relief = RIDGE)
    coke_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load6 = Image.open("coke.jpeg")
    photo6 = ImageTk.PhotoImage(load6)
    img6_lbl = tk.Label(coke_frame,image = photo6)
    img6_lbl.place(x = 300,y = 50)
    img6_lbl.image = photo6

    item_lbl = tk.Label(coke_frame,text = "COKE", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(coke_frame,text = "RUPEES : 35", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(coke_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart1)
    addcart_btn.place(x = 330,y = 530,width = 300,height = 50)


def addtocart1():

    scr11 = tk.Tk()
    scr11.title("COKE")
    scr11.geometry("1300x650+0+0")
    scr11.configure(bg = "SANDY BROWN")

    coke_frame = tk.Frame(scr11,bd = 2,relief = RIDGE)
    coke_frame.place(x = 460,y = 50,width = 600,height = 700)

    coke_lbl = tk.Label(coke_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    coke_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(coke_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(coke_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"COKE")

    username_lbl = tk.Label(coke_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(coke_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(coke_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(coke_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(coke_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 100,y = 520,width = 300,height = 50)


def insert1(prod_txt,username_txt,qty_txt):

    end_msg = messagebox.showinfo("THANKS","THANKS FOR SHOPPING!! VISIT AGAIN!!!")

    prod = prod_txt.get()
    username = username_txt.get()
    qty = qty_txt.get()

    connection = mysql.connector.connect(host = "localhost",user = "root",password = "password",database = "company")
    insert1 = ("insert into user_prod(prod,username,qty)values('"+prod+"','"+username+"',"+qty+")")
    cursor = connection.cursor()
    cursor.execute(insert1)
    connection.commit()
    cursor.close()

    mycursor = connection.cursor()
    mycursor.execute("select * from user_prod")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def LAYS():

    scr12 = tk.Toplevel()
    scr12.title("LAYS - ADD TO CART")
    scr12.geometry("1300x650+0+0")
    scr12.configure(bg = "ORANGE")

    lays_frame = tk.Frame(scr12,bd = 0,relief = RIDGE)
    lays_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load7 = Image.open("lays.jpeg")
    photo7 = ImageTk.PhotoImage(load7)
    img7_lbl = tk.Label(lays_frame,image = photo7)
    img7_lbl.place(x = 300,y = 50)
    img7_lbl.image = photo7

    item_lbl = tk.Label(lays_frame,text = "LAYS", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(lays_frame,text = "RUPEES : 20", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(lays_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart2)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart2():

    scr13 = tk.Tk()
    scr13.title("LAYS")
    scr13.geometry("1300x650+0+0")
    scr13.configure(bg = "SANDY BROWN")

    lays_frame = tk.Frame(scr13,bd = 2,relief = RIDGE)
    lays_frame.place(x = 460,y = 50,width = 600,height = 700)

    lays_lbl = tk.Label(lays_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    lays_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(lays_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(lays_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"LAYS")

    username_lbl = tk.Label(lays_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(lays_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(lays_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(lays_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(lays_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def HIDEANDSEEK():

    scr12 = tk.Toplevel()
    scr12.title("HIDE AND SEEK - ADD TO CART")
    scr12.geometry("1300x650+0+0")
    scr12.configure(bg = "SLATEBLUE2")

    hide_frame = tk.Frame(scr12,bd = 0,relief = RIDGE)
    hide_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load8 = Image.open("hide and seek.jpeg")
    photo8 = ImageTk.PhotoImage(load8)
    img8_lbl = tk.Label(hide_frame,image = photo8)
    img8_lbl.place(x = 300,y = 50)
    img8_lbl.image = photo8


    item_lbl = tk.Label(hide_frame,text = "HIDE AND SEEK", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(hide_frame,text = "RUPEES : 30", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(hide_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart3)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart3():

    scr15 = tk.Tk()
    scr15.title("HIDE AND SEEK")
    scr15.geometry("1300x650+0+0")
    scr15.configure(bg = "SANDY BROWN")

    hide_frame = tk.Frame(scr15,bd = 2,relief = RIDGE)
    hide_frame.place(x = 460,y = 50,width = 600,height = 700)

    hide_lbl = tk.Label(hide_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    hide_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(hide_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(hide_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"HIDE AND SEEK")

    username_lbl = tk.Label(hide_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(hide_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(hide_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(hide_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(hide_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def MAGGI():

    scr16 = tk.Toplevel()
    scr16.title("MAGGI - ADD TO CART")
    scr16.geometry("1300x650+0+0")
    scr16.configure(bg = "YELLOW")

    magg_frame = tk.Frame(scr16,bd = 0,relief = RIDGE)
    magg_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load9 = Image.open("maggi.jpeg")
    photo9 = ImageTk.PhotoImage(load9)
    img9_lbl = tk.Label(magg_frame,image = photo9)
    img9_lbl.place(x = 330,y = 50)
    img9_lbl.image = photo9

    item_lbl = tk.Label(magg_frame,text = "MAGGI", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(magg_frame,text = "RUPEES : 15", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(magg_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart4)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart4():

    scr17 = tk.Tk()
    scr17.title("MAGGI")
    scr17.geometry("1300x650+0+0")
    scr17.configure(bg = "SANDY BROWN")

    magg_frame = tk.Frame(scr17,bd = 2,relief = RIDGE)
    magg_frame.place(x = 460,y = 50,width = 600,height = 700)

    magg_lbl = tk.Label(magg_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    magg_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(magg_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(magg_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"MAGGI")

    username_lbl = tk.Label(magg_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(magg_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(magg_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(magg_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(magg_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def LIMCA ():

    scr17 = tk.Toplevel()
    scr17.title("LIMCA - ADD TO CART")
    scr17.geometry("1300x650+0+0")
    scr17.configure(bg = "LIGHTCYAN2")

    lim_frame = tk.Frame(scr17,bd = 0,relief = RIDGE)
    lim_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load10 = Image.open("limca2.jpeg")
    photo10 = ImageTk.PhotoImage(load10)
    img10_lbl = tk.Label(lim_frame,image = photo10)
    img10_lbl.place(x = 330,y = 50)
    img10_lbl.image = photo10

    item_lbl = tk.Label(lim_frame,text = "LIMCA", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(lim_frame,text = "RUPEES : 36", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(lim_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart5)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart5():

    scr18 = tk.Tk()
    scr18.title("LIMCA")
    scr18.geometry("1300x650+0+0")
    scr18.configure(bg = "SANDY BROWN")

    lim_frame = tk.Frame(scr18,bd = 2,relief = RIDGE)
    lim_frame.place(x = 460,y = 50,width = 600,height = 700)

    lim_lbl = tk.Label(lim_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    lim_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(lim_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(lim_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"LIMCA")

    username_lbl = tk.Label(lim_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(lim_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(lim_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(lim_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(lim_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def electronics():

    scr4 = tk.Toplevel()
    scr4.title("ELECTRONICS")
    scr4.geometry("1300x650+0+0")
    scr4.configure(bg = "DODGERBLUE2")

    ele_frame = tk.Frame(scr4,bd = 0,relief = RIDGE)
    ele_frame.place(x = 50,y = 50,width = 1350,height = 700)

    load11 = Image.open("bg.jpeg")
    photo11 = ImageTk.PhotoImage(load11)
    img11_lbl = tk.Label(ele_frame,image = photo11)
    img11_lbl.place(x = 0,y = 0)
    img11_lbl.image = photo11

    ele_lbl = tk.Label(ele_frame,text = "ELECTRONICS", font = ("ALGERIAN",35,"bold"),fg = "PURPLE2")
    ele_lbl.place(x = 15,y = 30,relwidth = 1)

    btn_ele = tk.Button(ele_frame,text = "DELL",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command = DELL)
    btn_ele.place(x = 80,y = 150,width = 250,height = 80)

    btn_ele = tk.Button(ele_frame,text = "LENOVO",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command =LENOVO)
    btn_ele.place(x = 500,y = 150,width = 250,height = 80)

    btn_ele = tk.Button(ele_frame,text = "SAMSUNG",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command =SAMSUNG )
    btn_ele.place(x = 900,y = 150,width = 250,height = 80)

    btn_ele = tk.Button(ele_frame,text = "REDMI",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command = REDMI)
    btn_ele.place(x = 80,y = 350,width = 250,height = 80)

    btn_ele = tk.Button(ele_frame,text = "HP",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command = HP)
    btn_ele.place(x = 500,y = 350,width = 250,height = 80)

    btn_ele = tk.Button(ele_frame,text = "HP MOUSE",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command = HP_MOUSE)
    btn_ele.place(x = 900,y = 350,width = 250,height = 80)

    btn_ele = tk.Button(ele_frame,text = "SONY PENDRIVE",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "DEEPPINK2",command = SONY_PENDRIVE)
    btn_ele.place(x = 450,y = 500,width = 400,height = 90)


def DELL ():

    scr19 = tk.Toplevel()
    scr19.title("DELL - ADD TO CART")
    scr19.geometry("1300x650+0+0")
    scr19.configure(bg = "GRAY33")

    dell_frame = tk.Frame(scr19,bd = 0,relief = RIDGE)
    dell_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load12 = Image.open("dell laptop.jpeg")
    photo12 = ImageTk.PhotoImage(load12)
    img12_lbl = tk.Label(dell_frame,image = photo12)
    img12_lbl.place(x = 330,y = 50)
    img12_lbl.image = photo12

    item_lbl = tk.Label(dell_frame,text = "DELL", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(dell_frame,text = "RUPEES : 45,000", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(dell_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart6)
    addcart_btn.place(x = 330,y = 500,width = 300,height = 100)


def addtocart6():

    scr20 = tk.Tk()
    scr20.title("DELL")
    scr20.geometry("1300x650+0+0")
    scr20.configure(bg = "THISTLE")

    dell_frame = tk.Frame(scr20,bd = 2,relief = RIDGE)
    dell_frame.place(x = 460,y = 50,width = 600,height = 700)

    dell_lbl = tk.Label(dell_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    dell_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(dell_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(dell_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"DELL")

    username_lbl = tk.Label(dell_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(dell_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(dell_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(dell_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(dell_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 530,width = 300,height = 50)


def LENOVO ():

    scr21 = tk.Toplevel()
    scr21.title("LENOVO - ADD TO CART")
    scr21.geometry("1300x650+0+0")
    scr21.configure(bg = "PALETURQUOISE1")

    leno_frame = tk.Frame(scr21,bd = 0,relief = RIDGE)
    leno_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load13 = Image.open("laptop.jpeg")
    photo13 = ImageTk.PhotoImage(load13)
    img13_lbl = tk.Label(leno_frame,image = photo13)
    img13_lbl.place(x = 330,y = 50)
    img13_lbl.image = photo13

    item_lbl = tk.Label(leno_frame,text = "LENOVO", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(leno_frame,text = "RUPEES : 20,000", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(leno_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart7)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart7():

    scr22 = tk.Tk()
    scr22.title("LENOVO")
    scr22.geometry("1300x650+0+0")
    scr22.configure(bg = "THISTLE")

    leno_frame = tk.Frame(scr22,bd = 2,relief = RIDGE)
    leno_frame.place(x = 460,y = 50,width = 600,height = 700)

    leno_lbl = tk.Label(leno_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    leno_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(leno_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(leno_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"LENOVO")

    username_lbl = tk.Label(leno_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(leno_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(leno_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(leno_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(leno_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def SAMSUNG():

    scr23 = tk.Toplevel()
    scr23.title("SAMSUNG - ADD TO CART")
    scr23.geometry("1300x650+0+0")
    scr23.configure(bg = "DARK SEA GREEN")

    sams_frame = tk.Frame(scr23,bd = 0,relief = RIDGE)
    sams_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load14 = Image.open("samsung.jpeg")
    photo14 = ImageTk.PhotoImage(load14)
    img14_lbl = tk.Label(sams_frame,image = photo14)
    img14_lbl.place(x = 330,y = 50)
    img14_lbl.image = photo14

    item_lbl = tk.Label(sams_frame,text = "SAMSUNG", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(sams_frame,text = "RUPEES : 10,949", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(sams_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart8)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart8():

    scr24 = tk.Tk()
    scr24.title("SAMSUNG")
    scr24.geometry("1300x650+0+0")
    scr24.configure(bg = "THISTLE")

    sams_frame = tk.Frame(scr24,bd = 2,relief = RIDGE)
    sams_frame.place(x = 460,y = 50,width = 600,height = 700)

    sams_lbl = tk.Label(sams_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    sams_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(sams_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(sams_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"SAMSUNG")

    username_lbl = tk.Label(sams_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(sams_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(sams_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(sams_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(sams_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def REDMI():

    scr25 = tk.Toplevel()
    scr25.title("REDMI - ADD TO CART")
    scr25.geometry("1300x650+0+0")
    scr25.configure(bg = "INDIAN RED")

    redmi_frame = tk.Frame(scr25,bd = 0,relief = RIDGE)
    redmi_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load15 = Image.open("redmi.jpeg")
    photo15 = ImageTk.PhotoImage(load15)
    img15_lbl = tk.Label(redmi_frame,image = photo15)
    img15_lbl.place(x = 330,y = 50)
    img15_lbl.image = photo15

    item_lbl = tk.Label(redmi_frame,text = "REDMI", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(redmi_frame,text = "RUPEES : 7000", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(redmi_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart9)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart9():

    scr26 = tk.Tk()
    scr26.title("REDMI")
    scr26.geometry("1300x650+0+0")
    scr26.configure(bg = "THISTLE")

    redmi_frame = tk.Frame(scr26,bd = 2,relief = RIDGE)
    redmi_frame.place(x = 460,y = 50,width = 600,height = 700)

    redmi_lbl = tk.Label(redmi_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    redmi_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(redmi_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(redmi_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"REDMI")

    username_lbl = tk.Label(redmi_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(redmi_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(redmi_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(redmi_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(redmi_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def HP():

    scr27 = tk.Toplevel()
    scr27.title("HP - ADD TO CART")
    scr27.geometry("1300x650+0+0")
    scr27.configure(bg = "DARK SEA GREEN")

    hp_frame = tk.Frame(scr27,bd = 0,relief = RIDGE)
    hp_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load16 = Image.open("hp lap ori.jpeg")
    photo16 = ImageTk.PhotoImage(load16)
    img16_lbl = tk.Label(hp_frame,image = photo16)
    img16_lbl.place(x = 330,y = 50)
    img16_lbl.image = photo16

    item_lbl = tk.Label(hp_frame,text = "HP", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(hp_frame,text = "RUPEES : 46,000", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(hp_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart10)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)

def addtocart10():

    scr28 = tk.Tk()
    scr28.title("HP")
    scr28.geometry("1300x650+0+0")
    scr28.configure(bg = "THISTLE")

    hp_frame = tk.Frame(scr28,bd = 2,relief = RIDGE)
    hp_frame.place(x = 460,y = 50,width = 600,height = 700)

    hp_lbl = tk.Label(hp_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    hp_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(hp_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(hp_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"HP")

    username_lbl = tk.Label(hp_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(hp_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(hp_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(hp_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(hp_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def HP_MOUSE():

    scr29 = tk.Toplevel()
    scr29.title("HP MOUSE - ADD TO CART")
    scr29.geometry("1300x650+0+0")
    scr29.configure(bg = "BISQUE3")

    hpmou_frame = tk.Frame(scr29,bd = 0,relief = RIDGE)
    hpmou_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load17 = Image.open("hp mouse.jpeg")
    photo17 = ImageTk.PhotoImage(load17)
    img17_lbl = tk.Label(hpmou_frame,image = photo17)
    img17_lbl.place(x = 330,y = 50)
    img17_lbl.image = photo17

    item_lbl = tk.Label(hpmou_frame,text = "HP MOUSE", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(hpmou_frame,text = "RUPEES : 349", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(hpmou_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart11)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart11():

    scr29 = tk.Tk()
    scr29.title("HP MOUSE")
    scr29.geometry("1300x650+0+0")
    scr29.configure(bg = "THISTLE")

    hpmou_frame = tk.Frame(scr29,bd = 2,relief = RIDGE)
    hpmou_frame.place(x = 460,y = 50,width = 600,height = 700)

    hpmou_lbl = tk.Label(hpmou_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    hpmou_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(hpmou_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(hpmou_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"HP MOUSE")

    username_lbl = tk.Label(hpmou_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(hpmou_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(hpmou_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(hpmou_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(hpmou_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def SONY_PENDRIVE():

    scr30 = tk.Toplevel()
    scr30.title("SONY PENDRIVE - ADD TO CART")
    scr30.geometry("1300x650+0+0")
    scr30.configure(bg = "SKYBLUE2")

    pend_frame = tk.Frame(scr30,bd = 0,relief = RIDGE)
    pend_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load18 = Image.open("sony pendrive.jpeg")
    photo18 = ImageTk.PhotoImage(load18)
    img18_lbl = tk.Label(pend_frame,image = photo18)
    img18_lbl.place(x = 330,y = 50)
    img18_lbl.image = photo18

    item_lbl = tk.Label(pend_frame,text = "SONY PENDRIVE", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(pend_frame,text = "RUPEES : 499", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(pend_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart12)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart12():

    scr31 = tk.Tk()
    scr31.title("SONY PENDRIVE")
    scr31.geometry("1300x650+0+0")
    scr31.configure(bg = "THISTLE")

    pend_frame = tk.Frame(scr31,bd = 2,relief = RIDGE)
    pend_frame.place(x = 460,y = 50,width = 600,height = 700)

    pend_lbl = tk.Label(pend_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    pend_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(pend_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(pend_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"DELL PENDRIVE")

    username_lbl = tk.Label(pend_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(pend_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(pend_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(pend_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(pend_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)

def sports():

    scr5 = tk.Toplevel()
    scr5.title("SPORTS")
    scr5.geometry("1300x650+0+0")
    scr5.configure(bg = "MAGENTA")

    spo_frame = tk.Frame(scr5,bd = 0,relief = RIDGE,bg = "KHAKI")
    spo_frame.place(x = 50,y = 50,width = 1350,height = 700)

    load = Image.open("sports.jpeg")
    photo = ImageTk.PhotoImage(load)
    img_lbl = tk.Label(spo_frame,image = photo)
    img_lbl.place(x = 0,y = 0)
    img_lbl.image = photo

    spo_lbl = tk.Label(spo_frame,text = "SPORTS", font = ("ALGERIAN",35,"bold"),fg = "DEEPPINK1")
    spo_lbl.place(x = 15,y = 30,relwidth = 1)

    btn_spo = tk.Button(spo_frame,text = "YONEX BAT",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "BLUE2",command = YONEX_BAT)
    btn_spo.place(x = 200,y = 200,width = 350,height = 100)

    btn_spo = tk.Button(spo_frame,text = "ARTENGO BAT",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "BLUE2",command = ARTENGO_BAT)
    btn_spo.place(x = 800,y = 200,width = 350,height = 100)

    btn_spo = tk.Button(spo_frame,text = "NIKE SHOES",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "BLUE2",command = NIKE_SHOES)
    btn_spo.place(x = 200,y = 450,width = 350,height = 100)

    btn_spo = tk.Button(spo_frame,text = "TENNIS BALL",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "BLUE2",command =TENNIS_BALL)
    btn_spo.place(x = 800,y = 450,width = 350,height = 100)


def YONEX_BAT():

    scr32 = tk.Toplevel()
    scr32.title("YONEX BAT - ADD TO CART")
    scr32.geometry("1300x650+0+0")
    scr32.configure(bg = "DEEP SKY BLUE")

    yon_frame = tk.Frame(scr32,bd = 0,relief = RIDGE)
    yon_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load19 = Image.open("yonex bat.jpeg")
    photo19 = ImageTk.PhotoImage(load19)
    img19_lbl = tk.Label(yon_frame,image = photo19)
    img19_lbl.place(x = 360,y = 50)
    img19_lbl.image = photo19

    item_lbl = tk.Label(yon_frame,text = "YONEX BAT", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(yon_frame,text = "RUPEES : 500", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(yon_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart20)
    addcart_btn.place(x = 330,y = 520,width = 350,height = 100)
def addtocart20():

    scr33 = tk.Tk()
    scr33.title("YONEX BAT")
    scr33.geometry("1300x650+0+0")
    scr33.configure(bg = "SLATEGRAY1")

    yon_frame = tk.Frame(scr33,bd = 2,relief = RIDGE)
    yon_frame.place(x = 460,y = 50,width = 600,height = 700)

    yon_lbl = tk.Label(yon_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    yon_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(yon_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(yon_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"YONEX BAT")

    username_lbl = tk.Label(yon_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(yon_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(yon_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(yon_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(yon_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def ARTENGO_BAT  ():

    scr34 = tk.Toplevel()
    scr34.title("ARTENGO BAT - ADD TO CART")
    scr34.geometry("1300x650+0+0")
    scr34.configure(bg = "SADDLE BROWN")

    art_frame = tk.Frame(scr34,bd = 0,relief = RIDGE)
    art_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load20 = Image.open("artengo bat.jpeg")
    photo20 = ImageTk.PhotoImage(load20)
    img20_lbl = tk.Label(art_frame,image = photo20)
    img20_lbl.place(x = 450,y = 50)
    img20_lbl.image = photo20

    item_lbl = tk.Label(art_frame,text = "ARTENGO BAT", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(art_frame,text = "RUPEES : 4127", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(art_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart21)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart21():

    scr35 = tk.Tk()
    scr35.title("ARTENGO BAT")
    scr35.geometry("1300x650+0+0")
    scr35.configure(bg = "SLATEGRAY1")

    art_frame = tk.Frame(scr35,bd = 2,relief = RIDGE)
    art_frame.place(x = 460,y = 50,width = 600,height = 700)

    art_lbl = tk.Label(art_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    art_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(art_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(art_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"ARTENGO BAT")

    username_lbl = tk.Label(art_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(art_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(art_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(art_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(art_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def NIKE_SHOES  ():

    scr36 = tk.Toplevel()
    scr36.title("NIKE SHOES - ADD TO CART")
    scr36.geometry("1300x650+0+0")
    scr36.configure(bg = "STEEL BLUE")

    nike_frame = tk.Frame(scr36,bd = 0,relief = RIDGE)
    nike_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load21 = Image.open("nike shoes.jpeg")
    photo21 = ImageTk.PhotoImage(load21)
    img21_lbl = tk.Label(nike_frame,image = photo21)
    img21_lbl.place(x = 330,y = 50)
    img21_lbl.image = photo21

    item_lbl = tk.Label(nike_frame,text = "NIKE SHOES", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(nike_frame,text = "RUPEES : 1660", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(nike_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart22)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart22():

    scr37 = tk.Tk()
    scr37.title("NIKE SHOES")
    scr37.geometry("1300x650+0+0")
    scr37.configure(bg = "SLATEGRAY1")

    nike_frame = tk.Frame(scr37,bd = 2,relief = RIDGE)
    nike_frame.place(x = 460,y = 50,width = 600,height = 700)

    nike_lbl = tk.Label(nike_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    nike_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(nike_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(nike_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"NIKE SHOES")

    username_lbl = tk.Label(nike_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(nike_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(nike_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(nike_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(nike_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def TENNIS_BALL  ():

    scr38 = tk.Toplevel()
    scr38.title("TENNIS BALL - ADD TO CART")
    scr38.geometry("1300x650+0+0")
    scr38.configure(bg = "GREEN YELLOW")

    tenn_frame = tk.Frame(scr38,bd = 0,relief = RIDGE)
    tenn_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load22 = Image.open("tennis ball.jpeg")
    photo22 = ImageTk.PhotoImage(load22)
    img22_lbl = tk.Label(tenn_frame,image = photo22)
    img22_lbl.place(x = 370,y = 50)
    img22_lbl.image = photo22

    item_lbl = tk.Label(tenn_frame,text = "TENNIS BALL", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(tenn_frame,text = "RUPEES : 115", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(tenn_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart23)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)

def addtocart23():

    scr39 = tk.Tk()
    scr39.title("TENNIS BALL")
    scr39.geometry("1300x650+0+0")
    scr39.configure(bg = "SLATEGRAY1")

    tenn_frame = tk.Frame(scr39,bd = 2,relief = RIDGE)
    tenn_frame.place(x = 460,y = 50,width = 600,height = 700)

    tenn_lbl = tk.Label(tenn_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    tenn_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(tenn_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(tenn_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"TENNIS BALL")

    username_lbl = tk.Label(tenn_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(tenn_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(tenn_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(tenn_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(tenn_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def menfashion():

    scr6 = tk.Toplevel()
    scr6.title("MEN'S FASHION")
    scr6.geometry("1300x650+0+0")
    scr6.configure(bg = "DARK TURQUOISE")

    men_frame = tk.Frame(scr6,bd = 0,relief = RIDGE)
    men_frame.place(x = 50,y = 50,width = 1350,height = 700)

    load23 = Image.open("men fshion.jpeg")
    photo23 = ImageTk.PhotoImage(load23)
    img23_lbl = tk.Label(men_frame,image = photo23)
    img23_lbl.place(x = 0,y = 0)
    img23_lbl.image = photo23

    men_lbl = tk.Label(men_frame,text = "MEN'S FASHION", font = ("ALGERIAN",35,"bold"),fg = "DEEPPINK")
    men_lbl.place(x = 0,y = 30,relwidth = 1)

    btn_men = tk.Button(men_frame,text = "RAYMOND BLAZZER",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "BLUE2",command =RAYMOND_BLAZER)
    btn_men.place(x = 400,y = 200,width = 550,height = 100)

    btn_men = tk.Button(men_frame,text = "PARK AVENUE SHIRT",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "BLUE2",command = PARKAVENUE_SHIRT)
    btn_men.place(x = 400,y = 400,width = 550,height = 100)


def RAYMOND_BLAZER():

    scr40 = tk.Toplevel()
    scr40.title("RAYMOND BLAZER - ADD TO CART")
    scr40.geometry("1300x650+0+0")
    scr40.configure(bg = "STEELBLUE2")

    ray_frame = tk.Frame(scr40,bd = 0,relief = RIDGE)
    ray_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load24 = Image.open("raymond blazzer.jpeg")
    photo24 = ImageTk.PhotoImage(load24)
    img24_lbl = tk.Label(ray_frame,image = photo24)
    img24_lbl.place(x = 370,y = 30)
    img24_lbl.image = photo24

    item_lbl = tk.Label(ray_frame,text = "RAYMOND BLAZER", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(ray_frame,text = "RUPEES : 3,790", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(ray_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart24)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart24():

    scr41 = tk.Tk()
    scr41.title("RAYMOND BLAZER")
    scr41.geometry("1300x650+0+0")
    scr41.configure(bg = "GAINSBORO")

    ray_frame = tk.Frame(scr41,bd = 2,relief = RIDGE)
    ray_frame.place(x = 460,y = 50,width = 600,height = 700)

    ray_lbl = tk.Label(ray_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    ray_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(ray_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(ray_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"RAYMOND BLAZZER")

    username_lbl = tk.Label(ray_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(ray_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(ray_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(ray_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(ray_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def PARKAVENUE_SHIRT():

    scr42 = tk.Toplevel()
    scr42.title("PARK AVENUE SHIRT - ADD TO CART")
    scr42.geometry("1300x650+0+0")
    scr42.configure(bg = "OLIVEDRAB1")

    park_frame = tk.Frame(scr42,bd = 0,relief = RIDGE)
    park_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load25 = Image.open("park avenue shirt.jpeg")
    photo25 = ImageTk.PhotoImage(load25)
    img25_lbl = tk.Label(park_frame,image = photo25)
    img25_lbl.place(x = 370,y = 20)
    img25_lbl.image = photo25

    item_lbl = tk.Label(park_frame,text = "PARK AVENUE SHIRT", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(park_frame,text = "RUPEES : 1,699", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(park_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart25)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart25():

    scr43 = tk.Tk()
    scr43.title("PARK AVENUE SHIRT")
    scr43.geometry("1300x650+0+0")
    scr43.configure(bg = "GAINSBORO")

    park_frame = tk.Frame(scr43,bd = 2,relief = RIDGE)
    park_frame.place(x = 460,y = 50,width = 600,height = 700)

    park_lbl = tk.Label(park_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    park_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(park_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(park_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"PARK AVENUE SHIRT")

    username_lbl = tk.Label(park_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(park_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(park_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(park_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(park_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def womenfashion():

    scr7 = tk.Toplevel()
    scr7.title("WOMEN'S FASHION")
    scr7.geometry("1300x650+0+0")
    scr7.configure(bg = "HOT PINK")

    women_frame = tk.Frame(scr7,bd = 0,relief = RIDGE,bg = "PINK")
    women_frame.place(x = 50,y = 50,width = 1350,height = 700)

    load26 = Image.open("dress.jpeg")
    photo26 = ImageTk.PhotoImage(load26)
    img26_lbl = tk.Label(women_frame,image = photo26)
    img26_lbl.place(x = 0,y = 0)
    img26_lbl.image = photo26

    women_lbl = tk.Label(women_frame,text = "WOMEN'S FASHION", font = ("ALGERIAN",35,"bold"),fg = "DEEPPINK")
    women_lbl.place(x = 0,y = 30,relwidth = 1)

    btn_women = tk.Button(women_frame,text = "SAREE",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "BLUE2", command = SAREES)
    btn_women.place(x = 150,y = 200,width = 400,height = 100)

    btn_women = tk.Button(women_frame,text = "SKIRT",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "BLUE2",command = SKIRTS)
    btn_women.place(x = 800,y = 200,width = 400,height = 100)

    btn_women = tk.Button(women_frame,text = "CHUDITHAR",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "BLUE2", command = CHUDITHAR)
    btn_women.place(x = 450,y = 450,width = 400,height = 100)


def SAREES():

    scr44 = tk.Toplevel()
    scr44.title("SAREE - ADD TO CART")
    scr44.geometry("1300x650+0+0")
    scr44.configure(bg = "PINK")

    sar_frame = tk.Frame(scr44,bd = 0,relief = RIDGE)
    sar_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load27 = Image.open("saree.jpeg")
    photo27 = ImageTk.PhotoImage(load27)
    img27_lbl = tk.Label(sar_frame,image = photo27)
    img27_lbl.place(x = 370,y = 20)
    img27_lbl.image = photo27

    item_lbl = tk.Label(sar_frame,text = "SAREE", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(sar_frame,text = "RUPEES : 2,518", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(sar_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart26)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart26():

    scr45 = tk.Tk()
    scr45.title("SAREE")
    scr45.geometry("1300x650+0+0")
    scr45.configure(bg = "PLUM2")

    sar_frame = tk.Frame(scr45,bd = 2,relief = RIDGE)
    sar_frame.place(x = 460,y = 50,width = 600,height = 700)

    sar_lbl = tk.Label(sar_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    sar_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(sar_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(sar_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"SAREE")

    username_lbl = tk.Label(sar_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(sar_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(sar_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(sar_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(sar_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def SKIRTS():

    scr46 = tk.Toplevel()
    scr46.title("SKIRT - ADD TO CART")
    scr46.geometry("1300x650+0+0")
    scr46.configure(bg = "SKY BLUE")

    ski_frame = tk.Frame(scr46,bd = 0,relief = RIDGE)
    ski_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load28 = Image.open("skirt.jpeg")
    photo28 = ImageTk.PhotoImage(load28)
    img28_lbl = tk.Label(ski_frame,image = photo28)
    img28_lbl.place(x = 330,y = 20)
    img28_lbl.image = photo28

    item_lbl = tk.Label(ski_frame,text = "SKIRT", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(ski_frame,text = "RUPEES : 629", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(ski_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart27)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart27():

    scr47 = tk.Tk()
    scr47.title("SKIRT")
    scr47.geometry("1300x650+0+0")
    scr47.configure(bg = "PLUM2")

    ski_frame = tk.Frame(scr47,bd = 2,relief = RIDGE)
    ski_frame.place(x = 460,y = 50,width = 600,height = 700)

    ski_lbl = tk.Label(ski_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    ski_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(ski_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(ski_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"SKIRT")

    username_lbl = tk.Label(ski_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(ski_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(ski_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(ski_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(ski_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def CHUDITHAR ():

    scr48 = tk.Toplevel()
    scr48.title("CHUDITHAR - ADD TO CART")
    scr48.geometry("1300x650+0+0")
    scr48.configure(bg = "CYAN")

    chu_frame = tk.Frame(scr48,bd = 0,relief = RIDGE)
    chu_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load29 = Image.open("chudithar.jpeg")
    photo29 = ImageTk.PhotoImage(load29)
    img29_lbl = tk.Label(chu_frame,image = photo29)
    img29_lbl.place(x = 380,y = 20)
    img29_lbl.image = photo29

    item_lbl = tk.Label(chu_frame,text = "CHUDITHAR", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(chu_frame,text = "RUPEES : 1,200", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(chu_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart28)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart28():

    scr49 = tk.Tk()
    scr49.title("CHUDITHAR")
    scr49.geometry("1300x650+0+0")
    scr49.configure(bg = "PLUM2")

    chu_frame = tk.Frame(scr49,bd = 2,relief = RIDGE)
    chu_frame.place(x = 460,y = 50,width = 600,height = 700)

    chu_lbl = tk.Label(chu_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    chu_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(chu_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(chu_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"CHUDITHAR")

    username_lbl = tk.Label(chu_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(chu_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(chu_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(chu_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(chu_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def bagandluggages():

    scr8 = tk.Toplevel()
    scr8.title("BAG AND LUGGAGES")
    scr8.geometry("1300x650+0+0")
    scr8.configure(bg = "DARK TURQUOISE")

    bag_frame = tk.Frame(scr8,bd = 0,relief = RIDGE,bg = "PINK")
    bag_frame.place(x = 50,y = 50,width = 1350,height = 700)

    load30 = Image.open("cart.jpeg")
    photo30 = ImageTk.PhotoImage(load30)
    img30_lbl = tk.Label(bag_frame,image = photo30)
    img30_lbl.place(x = 50,y = 0)
    img30_lbl.image = photo30

    bag_lbl = tk.Label(bag_frame,text = "BAG AND LUGGAGES", font = ("ALGERIAN",45,"bold"),fg = "DEEPPINK")
    bag_lbl.place(x = 15,y = 30,relwidth = 1)

    btn_bag = tk.Button(bag_frame,text = "AMERICAN TOURISTER BAG",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "BLUE2", command =AMERICANTOURISTER_BAG)
    btn_bag.place(x = 350,y = 230,width = 650,height = 100)

    btn_bag = tk.Button(bag_frame,text = "WILD CRAFT BAG",font = ("ALGERIAN",35),bg = "LAVENDER",fg = "BLUE2", command = WILDCRAFT_BAG)
    btn_bag.place(x = 350,y = 450,width = 650,height = 100)


def AMERICANTOURISTER_BAG():

    scr50 = tk.Toplevel()
    scr50.title("AMERICAN TOURISTER BAG - ADD TO CART")
    scr50.geometry("1300x650+0+0")
    scr50.configure(bg = "CORAL")

    ame_frame = tk.Frame(scr50,bd = 0,relief = RIDGE)
    ame_frame.place(x = 50,y = 50,width = 1000,height = 700)

    load31 = Image.open("american toutiter.jpeg")
    photo31 = ImageTk.PhotoImage(load31)
    img31_lbl = tk.Label(ame_frame,image = photo31)
    img31_lbl.place(x = 310,y = 40)
    img31_lbl.image = photo31

    item_lbl = tk.Label(ame_frame,text = "AMERICAN TOURISTER BAG", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(ame_frame,text = "RUPEES : 1,990", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(ame_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart29)
    addcart_btn.place(x = 330,y = 520,width = 350,height = 100)


def addtocart29():

    scr51 = tk.Tk()
    scr51.title("AMERICAN TOURISTER BAG")
    scr51.geometry("1300x650+0+0")
    scr51.configure(bg = "LEMONCHIFFON3")

    ame_frame = tk.Frame(scr51,bd = 2,relief = RIDGE)
    ame_frame.place(x = 460,y = 50,width = 600,height = 700)

    ame_lbl = tk.Label(ame_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    ame_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(ame_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(ame_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"AMERICAN TOURISTER BAG")

    username_lbl = tk.Label(ame_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(ame_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(ame_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(ame_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(ame_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


def WILDCRAFT_BAG():

    scr52 = tk.Toplevel()
    scr52.title("WILD CRAFT BAG - ADD TO CART")
    scr52.geometry("1300x650+0+0")
    scr52.configure(bg = "DARK SALMON")

    wild_frame = tk.Frame(scr52,bd = 0,relief = RIDGE)
    wild_frame.place(x = 50,y = 20,width = 1000,height = 700)

    load32 = Image.open("wildcraft.jpeg")
    photo32 = ImageTk.PhotoImage(load32)
    img32_lbl = tk.Label(wild_frame,image = photo32)
    img32_lbl.place(x = 390,y = 10)
    img32_lbl.image = photo32

    item_lbl = tk.Label(wild_frame,text = "WILD CRAFT BAG", font = ("ALGERIAN",40,"bold"),fg = "BROWN4")
    item_lbl.place(x = 0,y = 350,relwidth = 1)

    rps_lbl = tk.Label(wild_frame,text = "RUPEES : 1,540", font = ("ALGERIAN",40,"bold"),fg = "DARKORANGE3")
    rps_lbl.place(x = 0,y = 450,relwidth = 1)

    addcart_btn = tk.Button(wild_frame,text = "ADD TO CART",font = ("ALGERIAN",30,"bold"),bg = "ALICE BLUE",fg = "RED",command = addtocart19)
    addcart_btn.place(x = 330,y = 520,width = 300,height = 100)


def addtocart19():

    scr53 = tk.Tk()
    scr53.title("WILD CRAFT BAG")
    scr53.geometry("1300x650+0+0")
    scr53.configure(bg = "LEMONCHIFFON3")

    wild_frame = tk.Frame(scr53,bd = 2,relief = RIDGE)
    wild_frame.place(x = 460,y = 50,width = 600,height = 700)

    wild_lbl = tk.Label(wild_frame,text = "FILL DETAILS", font = ("ALGERIAN",30,"bold"),fg = "RED")
    wild_lbl.place(x = 0,y = 20,relwidth = 1)

    prod_lbl = tk.Label(wild_frame,text = "PRODUCT :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    prod_lbl.place(x = 50,y = 130)
    prod_txt = tk.Entry(wild_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED2")
    prod_txt.place(x = 50,y = 190)
    prod_txt.insert(0,"WILD CRAFT BAG")

    username_lbl = tk.Label(wild_frame,text = "USERNAME :",font =("ALGERIAN",25,"bold"),fg = "GREEN3")
    username_lbl.place(x = 50,y = 270)
    username_txt = tk.Entry(wild_frame,font = ("FOOTLIGHT MT LIGHT",25),bg ="SNOW",fg = "RED2")
    username_txt.place(x = 50,y = 330)

    qty_lbl = tk.Label(wild_frame,text = "QUANTITY :",font = ("ALGERIAN",25,"bold"),fg = "GREEN3")
    qty_lbl.place(x = 50,y = 410)
    qty_txt = tk.Entry(wild_frame,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "RED3")
    qty_txt.place(x = 50,y = 470)

    contd_btn = tk.Button(wild_frame,text = "CONTINUE",font = ("ALGERIAN",20,"bold"),bg = "ALICE BLUE",fg = "RED",command = lambda:insert1(prod_txt,username_txt,qty_txt))
    contd_btn.place(x = 180,y = 520,width = 300,height = 50)


root = tk.Tk()
root.title("LOGIN FORM")
root.geometry("1300x650+0+0")
root.configure(bg = "LIGHT PINK")

username_var = tk.StringVar()
passwd_var = tk.StringVar()

canvas = Canvas(root,width = 1700,height  = 1000)
canvas.pack()
img = PhotoImage(file ="shop.png")
canvas.create_image(0,0,anchor = NW,image = img)

login_frame = Frame(root,bd = 2,relief = RIDGE)
login_frame.place(x = 500,y = 50,width = 600,height = 700)

login_lbl = tk.Label(login_frame,text = "LOGIN HERE", font = ("ALGERIAN",30,"bold"),fg = "MAROON2")
login_lbl.place(x = 0,y = 30,relwidth = 1)

username_lbl = tk.Label(login_frame,text = "USERNAME :",font = ("ALGERIAN",25),fg = "BLUE")
username_lbl.place(x = 50,y = 150)
username_txt = tk.Entry(login_frame,textvariable = username_var,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "MAGENTA")
username_txt.place(x = 50,y = 220)

passwd_lbl = tk.Label(login_frame,text = "PASSWORD :",font = ("ALGERIAN",25),fg = "BLUE")
passwd_lbl.place(x = 50,y = 300)
passwd_txt = tk.Entry(login_frame,textvariable = passwd_var,font = ("FOOTLIGHT MT LIGHT",25),bg = "SNOW",fg = "MAGENTA",show = "*")
passwd_txt.place(x = 50,y = 370)

login_btn = tk.Button(login_frame,text = "LOGIN",font = ("ALGERIAN",20),bg = "PINK",fg = "BLUE",command = submit)
login_btn.place(x = 200,y = 450,width = 200,height = 50)

signup_btn = tk.Button(login_frame,text = "SIGN UP",font = ("ALGERIAN",20),bg = "PINK",fg = "BLUE",command = reg)
signup_btn.place(x = 200,y = 550,width = 200,height = 50)

username_var1 = tk.StringVar()
passwd_var1 = tk.StringVar()
email_var1 = tk.StringVar()
addr_var1 = tk.StringVar()
phone_var1 = tk.StringVar()

root.mainloop()
