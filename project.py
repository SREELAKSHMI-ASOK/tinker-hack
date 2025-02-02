import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="SYSTEM",database="OhNoNosh")
cur=mydb.cursor()


#------------FOR VIEWING MENU SECTION-----------------

def menu():
    query="select * from menu"
    cur.execute(query)
    menu=cur.fetchall()
    print("\n\n-\t-----CUISINE-----\t-\n\n")
    print("Item_Id\tItem_Name\tPRICE\tItem_Type")
    for i in menu:
        print(i[0],'\t',i[1],'\t',i[2],'\t',i[3])
    print("\n\n")
    yn=int(input("DO YOU WANT TO ORDER AN ITEM? type(1 for yes / 2 for going back to main page):"))
    if yn==1:
        byo()
    else:
        print("THANK YOU")
        print("\n\n","YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE","\n")
        return
    
#-----------FOR BOOKING ORDER---------------
    
def byo():
    ID=int(input("ENTER ITEM NO OF THE ITEM YOU WANT TO ORDER:"))
    QUANTITY=int(input("ENTER QUANTITY:"))
    NAME=input("ENTER YOUR NAME:")
    MOBNO=int(input("ENTER YOUR MOBILE NUMBER:"))
    ADDRESS=input("ENTER YOUR ADDRESS:")
    a="select * from menu where Item_Id={}".format(ID)
    cur.execute(a)
    a=cur.fetchall()
    b=a[0][2]
    c=QUANTITY*b
    ins="insert into customer values('{}',{},{},{},'{}',{})".format(NAME,ID,QUANTITY,MOBNO,ADDRESS,c)
    cur.execute(ins)
    print("\n","THANKS FOR YOUR ORDER","\n\n","YOUR ORDER HAS BEEN ORDERED SUCCESSFULLY")
    print("\n\n","YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE","\n")
    mydb.commit()

#--------------FOR VIEWING ORDER---------------
    
def vyo():
    mn=int(input("Enter your Mobile Nummber:"))
    cust="select * from customer where Mob_no={}".format(mn)
    print("\n","YOUR RECENT ORDERS","\n")
    cur.execute(cust)
    det=cur.fetchall()
    for i in det:
        A="select * from menu,customer where Mob_no={} and menu.Item_Id=customer.Item_Id".format(mn)
        cur.execute(A)
        B=cur.fetchall()
        for rec in B:
            print("Item_Id:",rec[0],"\n","Item_Name:",rec[1],"\n","Item_Type:",rec[3],"\n","Total_Price:",rec[9],"\n","Mob_no:",rec[7],"\n","Address:",rec[8],"\n")
    print("\n\n","YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE","\n")
    mydb.commit()
    
#--------------FOR CANCELLING ORDER-------------
    
def cyo():
    c=int(input("Enter your mobile number to delete:"))
    e="delete from customer where Mob_no={}".format(c)
    cur.execute(e)
    print("\n","YOUR ORDER HAS BEEN CANCELLED")
    print("\n\n","YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE","\n")
    mydb.commit()

#--------------FEEDBACK--------------

def fdbck():
    fd=input("Enter your name:")
    print("Write something about us -- ")
    fdi=input()
    q="insert into feedback values('{}','{}')".format(fd,fdi)
    cur.execute(q)
    print("\n","Thanks for your feedback :) ")
    print("\n\n","YOU HAVE BEEN REDIRECTED TO THE MAIN PAGE","\n")
    mydb.commit()


#--------WELCOME PAGE--------

def start():
    print("\n")
    print("\n")
    print("                    ____________________________________")
    print("                    ************************************")
    print("                    <<<<<<<<<<<<<WELCOME TO>>>>>>>>>>>>>")
    print("                    ====================================")
    print("                                  OHNONOSH              ")
    print("                    ====================================")
    print("                    ************************************")
    print("                    ____________________________________")
    print("\n")
    print("Press assigned keys for going forward")
    print("1.CUSTOMER\n2.EXIT")


#---------WELCOME PAGE 2----------

def start1():
    while True:
        print("\n")
        print("\n")
        print("1. VIEW MENU")
        print("2. VIEW YOUR ORDERS")
        print("3. CANCEL ORDER")
        print("4. FEEDBACK")
        print("5. EXIT")
        ch1=int(input("Enter your choice:"))
        if ch1==1:
            menu()
        elif ch1==2:
            vyo()
        elif ch1==3:
            cyo()
        elif ch1==4:
            fdbck()
        elif ch1==5:
            start()
            break
        else:
            print("\n\n","INVALID CHOICE","\n","TRY AGAIN")
            start1()
start()


#-------PAGE INFINITE LOOP-------

while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        start1()
    elif ch==2:
        print("THANK YOU")
        break
    else:
        print("\n\n","INVALID CHOICE","\n","TRY AGAIN")
        start()


    

    
