from  tkinter import *

import os
from tkinter import ttk
from tkinter import messagebox



def get_connection():
    import pymysql as sql
    con = sql.connect(
        host="localhost",
        user="root",
        password="krishbyl@123",
        database="kutta"
    )
    return con




def login():
    user = e1.get()
    pwd = e2.get()

    if user == "" or pwd == "":
        messagebox.showerror("Error", "All fields required")
        return

    if user == "krishna" and pwd == "krishna":
        top.destroy()
        import subprocess
        subprocess.Popen(["python", "second.py"])
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


#import subprocess
#subprocess.Popen(["python", "second.py"])

def user_login():
    name = e3.get()
    last = e4.get()
    city = e5.get()
    age = e6.get()
    gender = e7.get()

    if name == "" or last == "" or city == "" or age == "" or gender == "":
        messagebox.showerror("Error", "All fields required")
        return

    top.destroy()
    import third
    third.open_user()



top = Tk()
top.geometry('1200x700')
top.configure(bg="black")


t1 = Label(text="LOGIN AS A ADMIN", bg="white",fg="red",font="Arial 20 bold")
t1.place(x=100,y=50)


t1 = Label(text="Name", bg="white",fg="green",font="Arial 15 bold")
t1.place(x=100,y=150)
e1 = Entry(bg="Brown",fg="white", font="Arial 10 bold")
e1.place(x=220,y=150)



t1 = Label(text="Password", bg="white",fg="green",font="Arial 15 bold")
t1.place(x=100,y=200)
e2 = Entry(bg="Brown",fg="white", font="Arial 10 bold")
e2.place(x=220,y=200)

b2=Button(text="Login",bg="black",fg="red",font="Arial 20 bold", command=login)
b2.place(x=220,y=250)







t1 = Label(text="LOGIN AS A USER", bg="white",fg="red",font="Arial 20 bold")
t1.place(x=800,y=50)



g1 = Label(text="Name", bg="white",fg="blue",font="Arial 15 bold")
g1.place(x=800,y=150)
e3 = Entry(bg="Brown",fg="white", font="Arial 10 bold")
e3.place(x=920,y=150)

g2 = Label(text="Last Name", bg="white",fg="blue",font="Arial 15 bold")
g2.place(x=800,y=200)
e4 = Entry(bg="Brown",fg="white", font="Arial 10 bold")
e4.place(x=920,y=200)


g3 = Label(text="City", bg="white",fg="blue",font="Arial 15 bold")
g3.place(x=800,y=250)
e5 = Entry(bg="Brown",fg="white", font="Arial 10 bold")
e5.place(x=920,y=250)

g4 = Label(text="Age",bg="white",fg="blue",font="Arial 15 bold")
g4.place(x=800,y=300)
e6 = Entry(bg="Brown",fg="white", font="Arial 10 bold")
e6.place(x=920,y=300)



g4 = Label(text="Gender",bg="white",fg="blue",font="Arial 15 bold")
g4.place(x=800,y=350)
e7= Entry(bg="Brown",fg="white", font="Arial 10 bold")
e7.place(x=920,y=350)


button1 =Button(text="Login", bg="black", fg="red",font="Arial 20 bold", command=user_login)
button1.place(x=920,y=450)


top.mainloop()