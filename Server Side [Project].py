import mysql.connector as mc

username=input("Enter your MySQL username: ")
password=input("Enter your MySQL password: ")
database=input("Enter your MySQL database: ")

db = mc.connect(host='localhost', user=username, password=password, database=database)
cursor = db.cursor()

def menu():
    while True:
        print("1. Add Records")
        print("2. Update Record")
        print("3. Delete Records")
        print("4. Display Records")
        print("5. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            if table=="furni_traders":
                trader_insertData()
            elif table=="construction":
                company_insertData()
            elif table=="comp_serv":
                centre_insertData()
            elif table=="catering":
                caterer_insertData()
        elif choice==2:
            updatedata()
        elif choice==3:
            deldata()
        elif choice==4:
            fetchdata()
        elif choice==5:
            print("Exiting")
            break
        else:
            print("Enter a valid choice!")

def fetchdata():
    sql="select * from %s" % table
    cursor.execute(sql)
    results=cursor.fetchall()
    for x in results:
        print(x)

def updatedata():
    update_argument=input("Enter the update argument: ")
    position_argument = input("Enter the position argument: ")
    sql = "update %s set %s where %s" % (table,update_argument,position_argument)
    cursor.execute(sql)
    print("Record Updated")
    db.commit()

def deldata():
    position_argument = input("Enter the position argument: ")
    sql = "delete from %s where %s" % (table,position_argument)
    cursor.execute(sql)
    db.commit()
    print("Record Deleted")

def trader_insertData():
    ans = "y"
    while ans=="y":
        id = int(input("Enter the trader ID: "))
        name = input("Enter the store's name: ")
        location = input("Enter the store's location: ")
        ratings = int(input("Enter a rating from 1 to 5: "))
        type = input("State whether the store is indoors or outdoors: ")
        contacts = input("Enter the store's email: ")

        sql = "insert into furni_traders values(%s,%s,%s,%s,%s,%s)"
        val = (id, name, location, ratings, type, contacts)
        cursor.execute(sql, val)
        db.commit()
        print("Records Added")
        ans = input("Do you want to enter more records? [y/n]: ")


def company_insertData():
    ans = "y"
    while ans=="y":
        id = int(input("Enter the construction company's ID: "))
        name = input("Enter the company's name: ")
        location = input("Enter the company's location: ")
        ratings = int(input("Enter a rating from 1 to 5: "))
        level = input("Enter the company's focus on construction: ")
        contacts = input("Enter the company's email: ")

        sql = "insert into construction values(%s,%s,%s,%s,%s,%s)"
        val = (id, name, location, ratings, level, contacts)
        cursor.execute(sql, val)
        db.commit()
        print("Records Added")
        ans = input("Do you want to enter more records? [y/n]: ")


def centre_insertData():
    ans = "y"
    while ans=="y":
        id = int(input("Enter the centre ID: "))
        name = input("Enter the centre's name: ")
        location = input("Enter the centre's location: ")
        ratings = int(input("Enter a rating from 1 to 5: "))
        type = input("Enter the type of centre: ")
        contacts = input("Enter the centre's email: ")

        sql = "insert into comp_serv values(%s,%s,%s,%s,%s,%s)"
        val = (id, name, location, ratings, type, contacts)
        cursor.execute(sql, val)
        db.commit()
        print("Records Added")
        ans = input("Do you want to enter more records? [y/n]: ")


def caterer_insertData():
    ans = "y"
    while ans=="y":
        id = int(input("Enter the caterer ID: "))
        name = input("Enter the caterer's name: ")
        location = input("Enter the caterer's location: ")
        ratings = int(input("Enter a rating from 1 to 5: "))
        type = input("State whether the caterer provides Veg or Non Veg: ")
        contacts = input("Enter the store's email: ")

        sql = "insert into catering values(%s,%s,%s,%s,%s,%s)"
        val = (id, name, location, ratings, type, contacts)
        cursor.execute(sql, val)
        db.commit()
        print("Records Added")
        ans = input("Do you want to enter more records? [y/n]: ")

while True:
    print("Select the table you need.")
    print("Type 1 for Traders")
    print("Type 2 for Companies")
    print("Type 3 for Centres")
    print("Type 4 for Caterers")
    print("Type 5 to Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        table="furni_traders"
        menu()
    elif ch==2:
        table="construction"
        menu()
    elif ch==3:
        table="comp_serv"
        menu()
    elif ch==4:
        table="catering"
        menu()
    elif ch==5:
        break
    else:
        print("Type a valid choice!")



