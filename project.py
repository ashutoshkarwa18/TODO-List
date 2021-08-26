import tkinter
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import mysql.connector
import os
import time
import pandas as pd
import matplotlib.pyplot as plt


def addtasks():
    
    ids = taskInfo1.get()
    title = taskInfo2.get()
    descr = taskInfo3.get()
    hours = taskInfo4.get()
    
    inserttask = "insert into "+taskTable+" values('"+ids+"','"+title+"','"+descr+"','"+hours+"')"
    try:
        cur.execute(inserttask)
        con.commit()
        messagebox.showinfo('Success',"Task added successfully")
    except:
        messagebox.showinfo("Error","Can't add task into Database")
    
    print(ids)
    print(title)
    print(descr)
    print(hours)

    root.destroy()
    
def addTask(): 
    
    global taskInfo1,taskInfo2,taskInfo3,taskInfo4,Canvas1,con,cur,taskTable,root
    
    root = Tk()
    root.title("Add Task")
    root.minsize(width=400,height=400)
    root.geometry("600x500+445-70")
    root.iconbitmap("favicon.ico")
   
    mydatabase="project"

    con = pymysql.connect(host="localhost",user="root",password="Ashu0304@",database=mydatabase)
    cur = con.cursor()

    taskTable = "tasks" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#A9A9A9")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FF4500",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Tasks", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    lb1 = Label(labelFrame,text="Task ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    taskInfo1 = Entry(labelFrame)
    taskInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    taskInfo2 = Entry(labelFrame)
    taskInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    lb3 = Label(labelFrame,text="Description : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    taskInfo3 = Entry(labelFrame)
    taskInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    lb4 = Label(labelFrame,text="Time Required : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    taskInfo4 = Entry(labelFrame)
    taskInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    SubmitBtn = Button(root,text="ADD",bg='white', fg='black',command=addtasks)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

mypass = "Ashu0304@"
mydatabase="project"

taskTable = "tasks" 


def deleteTask():
    
    ids = taskInfo1.get()
    title = taskInfo2.get()
    
    if (ids=="" or title==""):
        messagebox.showinfo('Error',"All fields required")
    else:
        con = pymysql.connect(host="localhost",user="root",password="Ashu0304@",database=mydatabase)
        cursor = con.cursor()
        cursor.execute("delete from tasks where ids = '"+ids+"' and title='"+title+"'")
        cursor.execute("commit");

        taskInfo1.delete(0,'end')
        taskInfo2.delete(0,'end')
        messagebox.showinfo('Success',"Task Deleted successfully")
        con.close(); 

    root.destroy()
    
def delete(): 
    
    global taskInfo1,taskInfo2,taskInfo3,taskInfo4,Canvas1,con,cur,taskTable,root
    
    root = Tk()
    root.title("Delete Task")
    root.minsize(width=400,height=400)
    root.geometry("600x500+445-70")
    root.iconbitmap("favicon.ico")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#808080")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#00FF00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Task", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    lb2 = Label(labelFrame,text="Task ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35)
        
    taskInfo1 = Entry(labelFrame)
    taskInfo1.place(relx=0.3,rely=0.35, relwidth=0.62)

    lb3 = Label(labelFrame,text="Task Title : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.55)
        
    taskInfo2 = Entry(labelFrame)
    taskInfo2.place(relx=0.3,rely=0.55, relwidth=0.62)
    
    SubmitBtn = Button(root,text="Delete",bg='white', fg='black',command=deleteTask)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

mypass = "Ashu0304@"
mydatabase="project"
 
taskTable = "tasks" 


def updateTask():

    ids = taskInfo1.get()
    title = taskInfo2.get()
    hours = taskInfo4.get()

    if (ids=="" or title=="" or hours==""):
        messagebox.showinfo('Error',"All fields required")
    else:
        con = pymysql.connect(host="localhost",user="root",password="Ashu0304@",database=mydatabase)
        cursor = con.cursor()
        cursor.execute("update tasks set title='"+title+"', hours='"+hours+"' where ids='"+ids+"'")
        cursor.execute("commit");

        taskInfo1.delete(0,'end')
        taskInfo2.delete(0,'end')
        taskInfo4.delete(0,'end')
        messagebox.showinfo('Success',"Task Updated successfully")
        con.close();
    root.destroy()

def update(): 
    
    global taskInfo1,taskInfo2,taskInfo3,taskInfo4,Canvas1,con,cur,taskTable,root
    
    root = Tk()
    root.title("Update Task")
    root.minsize(width=400,height=400)
    root.geometry("600x500+445-70")
    root.iconbitmap("favicon.ico")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#A9A9A9")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#800000",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Update Task", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   

    lb1 = Label(labelFrame,text="Task ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.15)
        
    taskInfo1 = Entry(labelFrame)
    taskInfo1.place(relx=0.3,rely=0.15, relwidth=0.62)
    
    lb2 = Label(labelFrame,text="Task Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.25)
        
    taskInfo2 = Entry(labelFrame)
    taskInfo2.place(relx=0.3,rely=0.25, relwidth=0.62)

    lb3 = Label(labelFrame,text="Updated Task : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.55)
        
    taskInfo2 = Entry(labelFrame)
    taskInfo2.place(relx=0.3,rely=0.55, relwidth=0.62)

    lb4 = Label(labelFrame,text="Previous Hours : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.35)
        
    taskInfo4 = Entry(labelFrame)
    taskInfo4.place(relx=0.3,rely=0.35, relwidth=0.62)

    lb5 = Label(labelFrame,text="Updated Hours : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.65)
        
    taskInfo4 = Entry(labelFrame)
    taskInfo4.place(relx=0.3,rely=0.65, relwidth=0.62)
    
    SubmitBtn = Button(root,text="Update",bg='white', fg='black',command=updateTask)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


def analysis():

    csv_file='task.csv'
    data=pd.read_csv(csv_file)
    
    titles=data["title"]
    hour=data["hours"]

    x=[]
    y=[]

    x=list(titles)
    y=list(hour)

    plt.pie(y,labels=x,autopct='%.2f%%',shadow=True,startangle=140)
    plt.show()

def graph():
    import seaborn
    import pandas
    import matplotlib.pyplot as plt
    csv = pandas.read_csv("C:\\Users\\admin\\Desktop\\Demo projects\\task.csv")
    res = seaborn.barplot(x=csv['title'], y=csv['hours'])
    plt.show()


mydatabase="project"

con = pymysql.connect(host="localhost",user="root",password="Ashu0304@",database=mydatabase)
cur = con.cursor()
taskTable = "tasks" 
    
def View(): 
    
    root = Tk()
    root.title("View Tasks")
    root.minsize(width=400,height=400)
    root.geometry("600x500+445-70")
    root.iconbitmap("favicon.ico")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#808080")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Tasks", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.26,relwidth=0.8,relheight=0.60)
    y = 0.2
    
    Label(labelFrame, text="%-23s%-38s%-30s%-30s"%('ID','Title','Description','Time Required'),bg='black',fg='white').place(relx=0.07,rely=0.06)
    Label(labelFrame, text="--------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.14)
    getTasks = "select * from "+taskTable
    
    try:
        cur.execute(getTasks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-20s%-30s%-35s%-10s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.06
    except:
        messagebox.showinfo("Failed to fetch data from database")


    dataBtn = Button(root,text="Pie Chart",bg='#f7f1e3', fg='black',command=analysis)
    dataBtn.place(relx=0.6,rely=0.9, relwidth=0.18,relheight=0.08)

    graphBtn = Button(root,text="Graph",bg='#f7f1e3', fg='black',command=graph)
    graphBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.2,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

mydatabase="project"

con = pymysql.connect(host="localhost",user="root",password="Ashu0304@",database=mydatabase)
cur = con.cursor()

comptaskTable = "comptasks" 
    
def ViewComp(): 
    
    root = Tk()
    root.title("View Tasks")
    root.minsize(width=400,height=400)
    root.geometry("600x500+445-70")
    root.iconbitmap("favicon.ico")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#808080")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Completed Tasks", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.26,relwidth=0.8,relheight=0.60)
    y = 0.2
    
    Label(labelFrame, text="%-40s%-60s%-65s"%('ID','Title','Time Required'),bg='black',fg='white').place(relx=0.07,rely=0.06)
    Label(labelFrame, text="-------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.14)
    getTasks = "select * from "+comptaskTable
    
    try:
        cur.execute(getTasks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-40s%-60s%-65s"%(i[0],i[1],i[2]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.06
    except:
        messagebox.showinfo("Failed to fetch data from database")

    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def comptasks():
    
    ids = comptaskInfo1.get()
    title = comptaskInfo2.get()
    hours = comptaskInfo4.get()
    
    inserttask = "insert into "+comptaskTable+" values('"+ids+"','"+title+"','"+hours+"')"
    try:
        cur.execute(inserttask)
        con.commit()
        messagebox.showinfo('Success',"Task added successfully")
    except:
        messagebox.showinfo("Error","Can't add task into Database")
    
    print(ids)
    print(title)
    print(hours)

    root.destroy()
    
def compTask(): 
    
    global comptaskInfo1,comptaskInfo2,comptaskInfo3,comptaskInfo4,compCanvas1,con,cur,comptaskTable,root
    
    root = Tk()
    root.title("Completed Task")
    root.minsize(width=400,height=400)
    root.geometry("600x500+445-70")
    root.iconbitmap("favicon.ico")
   
    mydatabase="project"

    con = pymysql.connect(host="localhost",user="root",password="Ashu0304@",database=mydatabase)
    cur = con.cursor()

    comptaskTable = "comptasks" 

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#A9A9A9")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#4169E1",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Completed Tasks", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.35,relwidth=0.8,relheight=0.4)
        
    lb1 = Label(labelFrame,text="Task ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.32, relheight=0.08)
        
    comptaskInfo1 = Entry(labelFrame)
    comptaskInfo1.place(relx=0.3,rely=0.32, relwidth=0.62, relheight=0.08)
        
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.45, relheight=0.08)
        
    comptaskInfo2 = Entry(labelFrame)
    comptaskInfo2.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)
        
    lb3 = Label(labelFrame,text="Time Spent : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.58, relheight=0.08)
        
    comptaskInfo4 = Entry(labelFrame)
    comptaskInfo4.place(relx=0.3,rely=0.58, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(root,text="ADD",bg='white', fg='black',command=comptasks)
    SubmitBtn.place(relx=0.21,rely=0.88, relwidth=0.18,relheight=0.08)

    viewBtn = Button(root,text="View Tasks",bg='white', fg='black', command=ViewComp)
    viewBtn.place(relx=0.41,rely=0.88, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="QUIT",bg='white', fg='black', command=root.destroy)
    quitBtn.place(relx=0.61,rely=0.88, relwidth=0.18,relheight=0.08)

    root.mainloop()
  

mydatabase="project"

con = pymysql.connect(host="localhost",user="root",password="Ashu0304@",database=mydatabase)
cur = con.cursor()

def main():

    root = Toplevel()
    root.title("Dashboard")
    root.minsize(width=400,height=400)
    root.geometry("1920x800+0-25")
    root.iconbitmap("favicon.ico")

    load = Image.open("todo.png")
    render = ImageTk.PhotoImage(load)
    img = Label(root,image = render)
    img.place(x=0,y=0)

    headingFrame1 = Frame(root,bg="#87CEEB",bd=5)
    headingFrame1.place(relx=0.18,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to \n Your Personal Manager", bg='black', fg='white', font=('yesteryear',25))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #photo=PhotoImage(file=r"C:\Users\admin\Desktop\python-rait\Main Project\delete.png")
    #image=photo,compound=LEFT

    btn1 = Button(root,text="Add Your Task",bg='black',fg='white',font=('Courier',20),command=addTask)
    btn1.place(relx=0.26,rely=0.32, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Delete Task",bg='black', fg='white',font=('Courier',20),command=delete)
    btn2.place(relx=0.26,rely=0.42, relwidth=0.45,relheight=0.1)
                    
    btn3 = Button(root,text="Update Task",bg='black', fg='white',font=('Courier',20),command=update)
    btn3.place(relx=0.26,rely=0.52, relwidth=0.45,relheight=0.1)
                    
    btn4 = Button(root,text="View Task List",bg='black', fg='white',font=('Courier',20),command=View)
    btn4.place(relx=0.26,rely=0.62, relwidth=0.45,relheight=0.1)

    btn6 = Button(root,text="Completed Task",bg='black', fg='white',font=('Courier',20),command=compTask)
    btn6.place(relx=0.26,rely=0.72, relwidth=0.45,relheight=0.1)
                  
    btn5 = Button(root,text="EXIT",bg='grey',borderwidth=12, fg='black',font=('Courier',20,"bold"),command=root.destroy)
    #btn5.place(relx=0.36,rely=0.85, relwidth=0.30,relheight=0.1)
    btn5.place(x=593,y=685,relheight=0.1,relwidth=0.2)


    root.mainloop()








