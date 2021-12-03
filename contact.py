# Auther = Dhiraj Arya
# Github username = dhiraj80
# Email = dhirajkum00380@gmail.com

import sqlite3
import os.path

if not os.path.exists("Contact.db"):
    conn = sqlite3.connect('Contact.db')
    conn.execute("""
    create table Contact(
        st_Name varchar(50),
        st_Mobile varchar(10)
    )
    """)

def addcontact(name,num):
    conn = sqlite3.connect("Contact.db")
    data = ("insert into Contact VALUES (?,?)")
    f = (name,num)
    conn.execute(data,f)
    conn.commit()
    conn.close()


def viewcontact():
    conn = sqlite3.connect("Contact.db")
    data = conn.execute("select * from Contact")
    for i in data:
        print(f"Name- {i[0]} <---------> Mobile No- {i[1]}")

try:
    print('''
            1. New Contact Entry
            2. View Contact List
            3. Exit
            ''')

    while True:
        user = int(input("\nEnter A Value--> "))

        if user==1:
            print('Add Contacts........')
            name = input("Enter Name --> ")
            num = input("Enter Number --> ")
            addcontact(name,num)
            print('Contact Add Sucsful...')

        elif user==2:
            print("View Contacts........")
            viewcontact()

        else:
            exit()

except:
    exit()