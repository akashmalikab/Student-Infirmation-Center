# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import sqlite3 
connection = sqlite3.connect('bond.db')
#print("Database created successfully")

mainWindow = tk.Tk()
mainWindow.geometry('2080x1000')
mainWindow.title("STUDENT INFORMATION CENTER")

heading_student = tk.Label(mainWindow, text="STUDENT INFORMATION CENTER",pady=(50),padx=(100),width='80',height='1',font=("Courier", 22))
heading_student.grid(row=0,column=0,columnspan=2)

name_student = tk.Label(mainWindow, text="Enter Name Of Student",pady=(30),padx=(50),width='70')
name_student.grid(row=1,column=0)

name_student= tk.Entry(mainWindow,width='60')
name_student.grid(row=1,column=1)

college_student = tk.Label(mainWindow, text="Enter College Of Student",pady=(30),padx=(50),width='70')
college_student.grid(row=2,column=0)

college_student = tk.Entry(mainWindow,width='60')
college_student.grid(row=2,column=1)

rollno_student = tk.Label(mainWindow, text="Enter RollNo Of Student",pady=(30),padx=(50),width='70')
rollno_student.grid(row=3,column=0)

rollno_student = tk.Entry(mainWindow,width='60')
rollno_student.grid(row=3,column=1)

phoneno_student = tk.Label(mainWindow, text="Enter PhoneNo Of Student",pady=(30),padx=(50),width='70')
phoneno_student.grid(row=4,column=0)

phoneno_student = tk.Entry(mainWindow,width='60')
phoneno_student.grid(row=4,column=1)

address_student = tk.Label(mainWindow, text="Enter Address Of Student",pady=(30),padx=(50),width='70')
address_student.grid(row=5,column=0)

address_student = tk.Entry(mainWindow,width='60')
address_student.grid(row=5,column=1)


def InsertData():
    name = name_student.get()
    college = college_student.get()
    rollno = rollno_student.get()
    phoneno = phoneno_student.get()
    address = address_student.get()
    
    connection.execute(" CREATE TABLE IF NOT EXISTS Details(NAME TEXT,COLLEGE TEXT,ROLL NO INTEGER,PHONENO INTEGER,ADDRESS TEXT) ;" )
    connection.execute(" INSERT INTO  Details VALUES ('"+name+"' , '"+college+"' ,"+rollno+" ,"+phoneno+" ,'"+address+"' ); ")
    connection.commit()
    
    
button = tk.Button(mainWindow, text="SUBMIT", command=lambda: InsertData(),pady=(10),padx=(50))
button.grid(row=6,column=0,columnspan=2)

def DeleteData():
    name = name_student.get()
    connection.execute("DELETE FROM Details WHERE NAME = '"+name+"' ; ")
    connection.commit()
    
    
button2 = tk.Button(mainWindow, text="DELETE", command=lambda: DeleteData(),pady=(10),padx=(50))
button2.grid(row=7,column=0,columnspan=2) 

def ShowData():
    cursor=connection.execute("SELECT * FROM Details ; ")
    for row in cursor:
        print("Student id is: ", row[2])
        print("Student name is: ", row[0])
        print("Stident college is: ", row[1])

    
    
button3 = tk.Button(mainWindow, text="DISPLAY", command=lambda: ShowData(),pady=(10),padx=(50))
button3.grid(row=8,column=0,columnspan=2)

mainWindow.mainloop()