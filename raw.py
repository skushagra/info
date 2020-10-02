import tkinter
import time
import sqlite3
from tkinter import *
root =  tkinter.Tk()
root.geometry("550x500+300+300")

# SQLite Connection
conn = sqlite3.connect('info.s3db')
c = conn.cursor()
# c.execute("create table info(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name VARCHAR(30), age INT, mobile INT, address VARCHAR(200), gender VARCHAR(20) default 'Preffer not to say', nation VARCHAR(20), qualification varchar(20))") 




#root.resizable(0,0)
data = ""
fname=""
lname=""
age = 0 
mno = ""
address = ""
gender = ""
nation = ""
qualification = ""
lbl1 = Label(root,text= " ").grid(row=0 , column=0)
#lbl2 = Label(root,text= "        ").grid(row=1 , column=0)
#lbl3 = Label(root,text= " ").grid(row=2 , column=0)
lblx1 = Label(root,text= "First Name",anchor = W, font = ("Verdena", 7)).grid(row=1 , column=1)
lblx1 = Label(root,text= "Last Name",anchor = W, font = ("Verdena", 7)).grid(row=1 , column=3)
ent1 = Entry(root,width = 12,font = ("Verdena", 12), background = "#ffffff", fg = "#000000")
ent1.grid(row=2 , column=1)
lbl5 = Label(root,text= " ").grid(row=2 , column=2)
lbl6 = Label(root,text= " ").grid(row=2 , column=3)
lbl7 = Label(root,text= " ").grid(row=2 , column=4)
ent2 = Entry(root,width = 12,font = ("Verdena", 12), background = "#ffffff", fg = "#000000")
ent2.grid(row=2 , column=3)

lbl11 = Label(root, text = " ").grid(row= 3, column= 0 )
lbl12 = Label(root, text = " ").grid(row= 4, column= 0 )

lblx1 = Label(root,text= "Age",anchor = W, font = ("Verdena", 7)).grid(row=4 , column=1)
lblx2 = Label(root,text= "Mobile Number",anchor = W, font = ("Verdena", 7)).grid(row=4 , column=3)
ent3 = Entry(root,width = 12,font = ("Verdena", 12), background = "#ffffff", fg = "#000000")
ent3.grid(row=5 , column=1)
lbl8 = Label(root,text= " ").grid(row=2 , column=2)
lbl10 = Label(root,text= " ").grid(row=2 , column=4)
ent4 = Entry(root,width = 12,font = ("Verdena", 12), background = "#ffffff", fg = "#000000")
ent4.grid(row=5 , column=3)


lbl13 = Label(root, text = " ").grid(row= 6, column= 0 )
lbl14 = Label(root, text = " ").grid(row= 6, column= 0 )

lblx3 = Label(root,text= "Address",anchor = W, font = ("Verdena", 7)).grid(row=7 , column=1)
lblx4 = Label(root,text= "Gender",anchor = W, font = ("Verdena", 7)).grid(row=7 , column=3)
ent5 = Entry(root,width = 12,font = ("Verdena", 12), background = "#ffffff", fg = "#000000")
ent5.grid(row=8 , column=1)
lbl8 = Label(root,text= " ").grid(row=2 , column=2)
lbl10 = Label(root,text= " ").grid(row=2 , column=4)
ent6 = Entry(root,width = 12,font = ("Verdena", 12), background = "#ffffff", fg = "#000000")
ent6.grid(row=8 , column=3)

lbl15 = Label(root, text = " ").grid(row= 9, column= 0 )
lbl16 = Label(root, text = " ").grid(row= 9, column= 0 )

lblx5 = Label(root,text= "Nationality",anchor = W, font = ("Verdena", 7)).grid(row=10 , column=1)
lblx6 = Label(root,text= "Qualification",anchor = W, font = ("Verdena", 7)).grid(row=10 , column=3)
ent7 = Entry(root,width = 12,font = ("Verdena", 12), background = "#ffffff", fg = "#000000")
ent7.grid(row=11 , column=1)
lbl8 = Label(root,text= " ").grid(row=2 , column=2)
lbl10 = Label(root,text= " ").grid(row=2 , column=4)
ent8 = Entry(root,width = 12,font = ("Verdena", 12), background = "#ffffff", fg = "#000000")
ent8.grid(row=11 , column=3)


lbl17 = Label(root, text = " ").grid(row= 3, column= 0 )
lbl18 = Label(root, text = " ").grid(row= 3, column= 1 )
lbl19 = Label(root, text = " ").grid(row= 3, column= 2 )
lbl20 = Label(root, text = " ").grid(row= 3, column= 3 )
lbl21 = Label(root, text = " ").grid(row= 3, column= 4 )
lbl22 = Label(root, text = " ").grid(row= 3, column= 5 )
lbl23 = Label(root, text = " ").grid(row= 3, column= 6 )
lbl24 = Label(root, text = " ").grid(row= 3, column= 7 )
lbl25 = Label(root, text = " ").grid(row= 3, column= 8 )
lbl26 = Label(root, text = " ").grid(row= 3, column= 9 )
lbl27 = Label(root, text = " ").grid(row= 3, column= 10 )
lbl28 = Label(root, text = " ").grid(row= 3, column= 11 )
lbl29 = Label(root, text = " ").grid(row= 3, column= 12 )
lbl30 = Label(root, text = " ").grid(row= 3, column= 13 )
lbl31 = Label(root, text = " ").grid(row= 3, column= 14 )
lbl32 = Label(root, text = " ").grid(row= 3, column= 15 )
lbl33 = Label(root, text = " ").grid(row= 3, column= 16 )
lbl34 = Label(root, text = " ").grid(row= 3, column= 17 )



lbl35 = Label(root, text = " ").grid(row= 12, column= 0)
lbl36 = Label(root, text = " ").grid(row= 13, column= 0)
lbl37 = Label(root, text = " ").grid(row= 14, column= 0)
lbl38 = Label(root, text = " ").grid(row= 15, column= 0)
lbl39 = Label(root, text = " ").grid(row= 16, column= 0)
lbl44 = Label(root, text = "", textvariable=data, anchor = W, font = ("Verdena", 12), background = "#ffffff", fg = "#000000",)
lbl44.grid(row = 17, column = 0,columnspan = 5 )



def add_data():
	fname = ent1.get()
	lname = ent2.get()
	age = ent3.get()
	mno = ent4.get()
	address = ent5.get()
	gender = ent6.get()
	nation = ent7.get()
	qualification = ent8.get()
	o_name = fname + lname
	lst1 = list()
	lst1.extend([o_name, age, mno, address, gender, nation, qualification])
	c.execute("INSERT INTO info (name, age, mobile, address, gender, nation, qualification) VALUES (?,?,?,?,?,?,?)",lst1)
	data.set("Data added successfully!")
	time.sleep(2)
	data.set("")



btn1 = Button(root, text = "Add Data",font=("Verdena ", 10),relief = GROOVE,border = 2,bg = "#8B8B8B",fg = "#000000",highlightthickness=0,command = add_data, )
btn1.grid(row=3, column=18)

root.mainloop()