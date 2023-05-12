import mysql.connector as connector
import math
from tkinter import *
import webbrowser

root = Tk()
root.title("GYM Management System")
#root.configure(bg="Black")
root['background']='#FFD700'
root.geometry("1400x700")
#Value Holders
lgvalue = StringVar()
lg2value = StringVar()
menuvalue = StringVar()



lgf1 = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=60, width=60,pady=10)
#lgf1.pack(pady=5,side=TOP)
lgf1.grid(sticky=N)


ls = Label(lgf1, text="Enter Database password", relief=GROOVE)
ls.grid()
lsentry = Entry(lgf1,textvariable=lgvalue,show="*")
lsentry.grid(row=0, column=3)

    
#Function for login1
def login():
    passwd=''
    passwd=lgvalue.get()
    if passwd == 'qpashish2002':
        lgr=Label(lgf1, text="Logged in Database Successfully")
        lgr.grid()
        global con
        con = connector.connect(host='localhost', port='3306',
                            user='root', password=passwd)
        login2()
        b2=Button(lgf2,text="submit",command=login2,background="blue",fg='White')
        b2.grid(row=3, column=3)
    
        
    else:
        lgw=Label(lgf1, text="Log in into Database Unsuccessfully")
        lgw.grid()

#Function for login2
def login2():
    #System Password
    global lgf2
    lgf2 = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=100, width=100,pady=10)
#lgf2.pack(pady=5,side=TOP)
    lgf2.grid(row=0,column=2,padx=5,pady=5)
    passwd2=''
    ls2r=Label(lgf2, text="Enter System Security password", relief=GROOVE)
    ls2r.grid(row=0, column=3)
    ls2entry = Entry(lgf2,textvariable=lg2value,show="*")
    ls2entry.grid(row=0, column=5)
        
    passwd2=ls2entry.get()
    if  passwd2=='abc123':
        lg2r=Label(lgf2, text="Logged in System Successfully")
        lg2r.grid(row=2, column=5)
        global c
        c = con.cursor()
        c.execute('show databases')
        dl = c.fetchall()  # Fetched all databases in this variable
        dl2 = []
        for i in dl:
            dl2.append(i[0])

        if 'dbmsdb' in dl2:
            sql = 'use dbmsdb'
            c.execute(sql)
        else:
            sql1 = '''create database dbmsdb'''
            c.execute(sql1)
            sql2 = '''use dbmsdb'''
            c.execute(sql2)
            sql3 = '''create table user(user_ID integer,user_name varchar(100),package integer,trainer_name varchar(50),trainer_type varchar(10))'''
            c.execute(sql3)
            #sql4 
            sql4 = '''create table trainer(trainer_id integer,trainer_name varchar(50),salary integer,trainer_type varchar(10))'''
            c.execute(sql4)
            sql5 = '''create table  equipment(equ_name varchar(100), Qauntity varchar(100),cost varchar(100))'''
            c.execute(sql5)

            con.commit()

        mainmenu()

    else:
            lg2w=Label(lgf2, text="Logged in System Failure", relief=GROOVE)
            lg2w.grid(row=2, column=5)
            
        
#Options for Menu
def options():

    choice=menuvalue.get()
    while True:
        if choice == '1':
            user()
            break
        elif choice == '2':
            trainer()
            break
        elif choice == '3':
            equipment()
            break
        elif choice == '4':
            NetIncome()
            break

        elif choice == '5':
            root.destroy()
            break
        
        else:
            print("\n********* Thank You *********** \n")
            break

        

def mainmenu():  #done
    mmf = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=200, width=100,pady=10)
    #mmf.pack(pady=5,side=TOP)
    mmf.grid(row=0,column=1,padx=5,pady=2)
    welcome_label= Label(mmf, text="WELCOME TO Gym Managenment system", relief=GROOVE)
    user_label= Label(mmf, text="1) User",border=5,relief=RIDGE)
    trainer_label = Label(mmf, text="2) Trainer",border=5,relief=RIDGE)
    Equipment_labels = Label(mmf, text="3)EQUIPMENT",border=5,relief=RIDGE)

    income_label = Label(mmf, text="4)Income",border=5,relief=RIDGE)
    exit_label = Label(mmf, text="5) EXIT",border=5,relief=RIDGE)
        #Pack text for our form
    welcome_label.grid(row=3, column=2,pady=5)
    user_label.grid(row=5, column=2)
    trainer_label.grid(row=7, column=2)
    Equipment_labels.grid(row=9, column=2)

    income_label.grid(row=13, column=2)
    exit_label.grid(row=15, column=2)
    ls2 = Label(mmf, text="Select Option",relief= SUNKEN)
    ls2.grid(row=17, column=2,pady=5)
    lsentry2 = Entry(mmf,textvariable=menuvalue)
    lsentry2.grid(row=19, column=2)
    menubutton=Button(mmf,text="submit",command=options,background="blue",fg='White')
    menubutton.grid(row=20, column=2,pady=5)

b1=Button(lgf1,text="submit",command=login,background="blue",fg='White')
b1.grid(row=0, column=5)

def Cname():#done
    sql = "select trainer_id,trainer_Name,trainer_type from trainer"
    c= con.cursor()
    c.execute(sql)
    d = c.fetchall()
    Available_trainer_label = Label(userframe, text=("<---- Available trainer ---->"),border=5,relief=RIDGE)
    Available_trainer_label.pack()
    print("<---- Available trainer ---->")
    for i in d:
        Available_Cook_label2 = Label(userframe, text=(str(i[0]), "---", str(i[1])),border=5,relief=RIDGE)
        Available_Cook_label2.pack()
        print(i[0], "---", i[1])
    return

def user():
    global userframe
    userframe = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=150, width=100,pady=10)
    userframe.grid(row=4,column=1,pady=2,padx=2)
    global user_input1
    global user_Costomer
    global user_id
    global user_package
    global user_trainer_type
    global user_trainer_name

    user_input1 = StringVar()
    user_Costomer = StringVar()
    user_package = StringVar()
    user_id = IntVar()
    user_trainer_type = StringVar()
    user_trainer_name=StringVar()

    label1 = Label(userframe, text="User :: 1. Add 2. Remove 3. Display :",relief= SUNKEN)
    #label1.grid(row=2, column=2,pady=5)
    label1.pack(pady=2)

    entry1 = Entry(userframe,textvariable=user_input1)
    #entry1.grid(row=4, column=2,pady=5)
    entry1.pack(pady=2)

    button=Button(userframe,text="submit",command=user_oprations,background="blue",fg='White')
    #button.grid(row=6, column=1)
    button.pack(pady=5)

    def clear_text():
            
            userframe.destroy()

    reset_button=Button(userframe,text="Reset",command=clear_text,background="red",fg='White')
    #Dish_reset_button.grid(row=6, column=3)
    reset_button.pack(pady=5)

def user_oprations():#done
    choice = user_input1.get()
    if choice == '1':

        Name_label = Label(userframe, text=" Name : ",relief= SUNKEN)
        #label.grid(row=8, column=2,pady=5)
        Name_label.pack(pady=2)
        Name_entry1 = Entry(userframe,textvariable=user_Costomer)
        #Name_entry1.grid(row=10, column=2,pady=5)
        Name_entry1.pack(pady=2)

        labe2 = Label(userframe, text="id: ",relief= SUNKEN)
       # label.grid(row=12, column=2,pady=5)
        labe2.pack(pady=2)
        entry2 = Entry(userframe,textvariable=user_id)
        #entry1.grid(row=14, column=2,pady=5)
        entry2.pack(pady=2)
        
        labe3 = Label(userframe, text="package: ",relief= SUNKEN)
       # label.grid(row=12, column=2,pady=5)
        labe3.pack(pady=2)
        entry3 = Entry(userframe,textvariable=user_package)
        #entry1.grid(row=14, column=2,pady=5)
        entry3.pack(pady=2)
        
        labe4 = Label(userframe, text="trainer type: ",relief= SUNKEN)
       # label.grid(row=12, column=2,pady=5)
        labe4.pack(pady=2)
        entry4 = Entry(userframe,textvariable=user_trainer_type)
        #entry1.grid(row=14, column=2,pady=5)
        entry4.pack(pady=2)        

        Cname()

        label = Label(userframe, text="trainered By: ",relief= SUNKEN)
        label.pack(pady=2)
        #label.grid(row=16, column=2,pady=5)
        entry1 = Entry(userframe,textvariable=user_trainer_name)
        entry1.pack(pady=2)
        #entry1.grid(row=18, column=2,pady=5)


        def user_oprations2():
            
            uc = user_Costomer.get()
            print(uc)
            ui = user_id.get()
            print(ui)
            
            up=user_package.get()
            print(up)
            
            utp=user_trainer_type.get()
            print(utp)
            
            ut = user_trainer_name.get()
            data = (ui, uc, up,utp,ut)
            sql = 'insert into user values(%s,%s,%s,%s,%s)'
            c = con.cursor()
            c.execute(sql, data)
            con.commit()
            data_label = Label(userframe, text="Data Entered Successfully",relief= SUNKEN)
            # Dish_data_label.grid(row=22, column=2,pady=5)
            data_label.pack(pady=2)

            
        
        button2=Button(userframe,text="submit",command=user_oprations2,background="blue",fg='White')
        #button2.grid(row=20, column=1)
        button2.pack(pady=2)

    elif choice == '2':

        label2 = Label(userframe, text=" Name : ",relief= SUNKEN)
        #Dish_Name_label2.grid(row=8, column=2,pady=5)
        label2.pack(pady=2)
        Name_entry2 = Entry(userframe,textvariable=user_Costomer)
        # Dish_Name_entry2.grid(row=10, column=2,pady=5)
        Name_entry2.pack(pady=2)

        

        def remove_user():
            ui = user_id.get()
            data = (ui,) 
            sql = 'delete from user_ID where user = %s' 
            c= con.cursor() 
            c.execute(sql,data) 
            con.commit() 
            data_label = Label(userframe, text="Data Deleted Successfully",relief= SUNKEN)
            #data_label.grid(row=14, column=2,pady=5)
            data_label.pack(pady=2)
            print("Data Updated Successfully")

        Dish_button3=Button(userframe,text="submit",command=remove_user,background="blue",fg='White')
        #Dish_button3.grid(row=12, column=2)
        Dish_button3.pack(pady=2)

    elif choice == '3':
        print("\n") 
        sql = "select * from user" 
        c= con.cursor() 
        c.execute(sql) 
        d = c.fetchall() 
        for i in d:
            Name_label_i = Label(userframe, text=(str(i[0]), "-", str(i[1]), "-", str(i[2])),relief= SUNKEN)
            #__label_i.grid(row=8, column=2,pady=5)
            Name_label_i.pack(pady=2)
            print(i[0], " -", i[1], "-", i[2]) 
        print("\n")
        Name_label = Label(userframe, text="\n",relief= SUNKEN)
        #Dish_Name_label.grid(row=9, column=2,pady=5) 
        Name_label.pack(pady=2)
    else:
        mainmenu()   

## Code for trainerS
def trainer():
    global trainerframe
    trainerframe = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=150, width=100,pady=10)
    trainerframe.grid(row=4,column=1,pady=2,padx=2)
    global trainer_id
    global trainer_name
    global Salary
    global trainer_type
    global Entry1


    trainer_id=StringVar()
    trainer_name=StringVar()
    Salary = StringVar()
    trainer_type = StringVar()
    Entry1= StringVar()


    trainer_label1 = Label(trainerframe, text="trainer :: 1. Add 2. Remove 3. Display  :",relief= SUNKEN)
    trainer_label1.grid(row=2, column=2,pady=5)
    trainer_entry1 = Entry(trainerframe,textvariable=Entry1)
    trainer_entry1.grid(row=4, column=2,pady=5)

    Dish_button=Button(trainerframe,text="submit",command=trainer_operation,background="blue",fg='White')
    Dish_button.grid(row=6, column=1)

    def reset_trainer():
            trainerframe.destroy()

    button=Button(trainerframe,text="Reset",command=reset_trainer,background="red",fg='White')
    button.grid(row=6, column=3)

def trainer_operation():
    choice = Entry1.get()
    if choice == '1':

        trainer_name_label = Label(trainerframe, text="Trainer id : ",relief= SUNKEN)
        trainer_name_label.grid(row=8, column=2,pady=5)
        trainer_name_entry1 = Entry(trainerframe,textvariable=trainer_id)
        trainer_name_entry1.grid(row=9, column=2,pady=5)

        A_label = Label(trainerframe, text="trainer Name : ",relief= SUNKEN)
        A_label.grid(row=10, column=2,pady=5)
        A_entry1 = Entry(trainerframe,textvariable=trainer_name)
        A_entry1.grid(row=11, column=2,pady=5)

        D_label = Label(trainerframe, text="Salary : ",relief= SUNKEN)
        D_label.grid(row=12, column=2,pady=5)
        D_entry1 = Entry(trainerframe,textvariable=Salary)
        D_entry1.grid(row=13, column=2,pady=5)

        DOJ_label = Label(trainerframe, text="trainer type : ",relief= SUNKEN)
        DOJ_label.grid(row=14, column=2,pady=5)
        DOJ_entry1 = Entry(trainerframe,textvariable=trainer_type)
        DOJ_entry1.grid(row=15, column=2,pady=5)



        def trainer_operation2():
            ti = trainer_id.get()
            tn = trainer_name.get()
            ts = Salary.get()
            ttp =trainer_type.get()
            data = (ti,tn,ts,ttp)
            sql = 'insert into trainer values(%s,%s,%s,%s)'
            c = con.cursor() 
            c.execute(sql,data) 
            con.commit()
            trainer_data_label = Label(trainerframe, text="Data Entered Successfully",relief= SUNKEN)
            trainer_data_label.grid(row=18, column=2,pady=5)
            print("Data Entered Successfully")

        trainer_button2=Button(trainerframe,text="submit",command=trainer_operation2,background="blue",fg='White')
        trainer_button2.grid(row=20, column=1)

        def clear_text1():
            trainer_name_entry1.delete(0, END)
            trainer_id.delete(0, END)
            Salary.delete(0, END)
            trainer_type.delete(0, END)
           
        
        trainer_reset_button=Button(trainerframe,text="Reset",command=clear_text1,background="red",fg='White')
        trainer_reset_button.grid(row=20, column=3)

    elif choice == '2':
        trainer_Name_label2 = Label(trainerframe, text="trainer Name : ",relief= SUNKEN)
        trainer_Name_label2.grid(row=8, column=2,pady=5)
        trainer_Name_entry2 = Entry(trainerframe,textvariable=trainer_name)
        trainer_Name_entry2.grid(row=10, column=2,pady=5)

        Aadhar_Name_label2 = Label(trainerframe, text="id : ",relief= SUNKEN)
        Aadhar_Name_label2.grid(row=12, column=2,pady=5)
        Aadhar_Name_entry2 = Entry(trainerframe,textvariable=trainer_id)
        Aadhar_Name_entry2.grid(row=14, column=2,pady=5)

        def remove_trainer():
            
            ca = trainer_id.get()
            data = (ca) 
            sql = 'delete from trainer_id where trainer = %s ' 
            c=con.cursor() 
            c.execute(sql,data) 
            con.commit() 
            print("Data Updated Successfully")
            ab_label = Label(trainerframe, text="Data Removed Successfully",relief= SUNKEN)
            ab_label.grid(row=16, column=2,pady=5)
            print("Data Entered Successfully")

        remove_trainer_button3=Button(trainerframe,text="submit",command=remove_trainer,background="blue",fg='White')
        remove_trainer_button3.grid(row=15, column=2)


    elif choice == '3':
        sql = "select * from trainer" 
        c= con.cursor() 
        c.execute(sql) 
        d = c.fetchall() 
        for i in d:
            trainer_Name_label_i = Label(trainerframe, text=(str(i[0]), "-", str(i[1]), "-", str(i[2]),"-",str(i[3]),"-"),relief= SUNKEN)
            trainer_Name_label_i.grid(row=8, column=2,pady=5)
            
            #print("\n",i[0], "-" ,i[1], "-" ,i[2], "-" ,i[3], "-" ,i[4],"\n") 
            
    else:
            options()


def equipment():
    global equipmentframe
    equipmentframe = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=150, width=100,pady=10)
    equipmentframe.grid(row=4,column=1,pady=2,padx=2)
    global NAME
    global Quantity
    global Cost
    

    NAME =StringVar()
    Quantity =StringVar()
    Cost = StringVar()


    Date_label2 = Label(equipmentframe, text="Equiement : ",relief= SUNKEN)
    #Date_label2.grid(row=11, column=2,pady=5)
    Date_label2.pack(pady=5)
    Date_entry2 = Entry(equipmentframe,textvariable=NAME)
    #Date_entry2.grid(row=12, column=2,pady=5)
    Date_entry2.pack()

    Customer_Name_label = Label(equipmentframe, text="quantity : ",relief= SUNKEN)
    Customer_Name_label.pack(pady=5)
    Customer_Name_entry2 = Entry(equipmentframe,textvariable=Quantity)
    Customer_Name_entry2.pack()

    Dish_Name_label2 = Label(equipmentframe, text="Cost : ",relief= SUNKEN)
    Dish_Name_label2.pack(pady=5)
    Dish_Name_label2_entry2 = Entry(equipmentframe,textvariable=Cost)
    Dish_Name_label2_entry2.pack()

    def reset_equipment():
            equipmentframe.destroy()
    

    def equipment_operations():


        dt = NAME.get() 
        cn = Cost.get() 
        lis = Quantity.get()
    
        
        data = (lis,dt,cn) 
        sql = 'insert into equipment values(%s,%s,%s)'
        c = con.cursor() 
        c.execute(sql,data) 
        con.commit() 
        #print("Total Amount : ",tc, "Rs")
        print("Data Entered Successfully") 
        equipment_data_label = Label(equipmentframe, text="Data Entered Successfully",relief= SUNKEN)
        equipment_data_label.pack()
        
    
    equipment_button=Button(equipmentframe,text="submit",command=equipment_operations,background="blue",fg='White')
    equipment_button.pack(pady=5)
    equipment_reset_button=Button(equipmentframe,text="Reset",command=reset_equipment,background="red",fg='White')
    equipment_reset_button.pack(pady=5)
    

def NetIncome():
    global netincomeframe
    netincomeframe = Frame(root, bg="grey", borderwidth=4, relief=RAISED, height=150, width=100,pady=10)
    netincomeframe.grid(row=4,column=1,pady=2,padx=2)
    def reset_netincome():
            netincomeframe.destroy()

    c= con.cursor() 
    sql = 'select package from user' 
    c.execute(sql) 
    d = c.fetchall() 
    oi = 0         #order income 
    for i in d:
        oi = oi + i[0] 
    print("Total Income from Orders : ",oi, "Rs") 
    _data_label = Label(netincomeframe, text="Total Income from Orders : Rs", relief= SUNKEN)
    _data_label.pack(pady=5)
    _label2 = Label(netincomeframe, text=oi, relief= SUNKEN)
    _label2.pack(pady=5)

    netincome_reset_button=Button(netincomeframe,text="Reset",command=reset_netincome,background="red",fg='White')
    netincome_reset_button.pack(pady=5)


root.mainloop()

