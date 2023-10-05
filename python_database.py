import sqlite3

def addCustomer():
    conn = sqlite3.connect('MyBank.db')
    c = conn.cursor()
    cid = int(input("Enter Customer Id : "))

    c.execute("select Balance from Customer where CID = (?);", (cid,))
    result = c.fetchall()
    # print(result)
    if len(result) > 0:
        print("Record already exists...")
        exit()

    cName = input("Enter Customer Name : ")
    FName = input("Enter Customer's Father Name : ")
    PhoneNo = int(input("Enter Customer Phone No.: "))
    Balance = 0
    Trans_Type = "Cr"

    sql = """INSERT INTO Customer values
              ({}, '{}', '{}', {}, {}, '{}');""".format(cid, cName, FName, PhoneNo, Balance, Trans_Type)

    print(sql)
    try:
        # Execute the SQL command
        c.executescript(sql)
        # Commit your changes in the database
        conn.commit()
        print("data inserted successfully...")
    except:
        # Rollback in case there is any error
        conn.rollback()
        print('Error')
    conn.close()

def deposit():
    conn = sqlite3.connect('MyBank.db')
    c = conn.cursor()
    cid = int(input("Enter the customer ID : "))

    c.execute("select Balance from Customer where CID = (?);", (cid,))
    result = c.fetchall()
    if len(result) == 0:
        print("Record not found...")
        exit()
    # print(result)
    preBal = result[0][0]         # [(1800, ),
                                   # (11500, 'Sumit')]

    amt = int(input("Enter the amount you want to deposit :"))
    amt = amt + preBal

    sql = """UPDATE Customer SET Balance = {}, Trans_Type = 'Cr'
             WHERE CID = {};
          """.format(amt, cid)
    print(sql)
    try:
        # Execute the SQL command
        c.executescript(sql)
        # Commit your changes in the database
        conn.commit()
        print("data updated successfully...")
    except:
        # Rollback in case there is any error
        conn.rollback()
        print('Error')
    conn.close()

def withdraw():
    conn = sqlite3.connect('MyBank.db')
    c = conn.cursor()
    cid = int(input("Enter the customer ID : "))

    c.execute("select Balance from Customer where CID = (?);", (cid,))
    result = c.fetchall()
    if len(result) == 0:
        print("Record not found...")
        exit()

    amt = int(input("Enter the amount you want to withdraw :"))

    # sel = "SELECT Balance FROM Customer where cid = {};".format(cid)
    c.execute("select Balance from Customer where cid = (?);", (cid,))
    result = c.fetchall()
    # print(result)
    bal = result[0][0]
    # print(bal)
    if bal < amt:
        print("Insufficient Balance")
    else:
        bal = bal - amt
        sql = """UPDATE Customer SET Balance = {}, Trans_Type = 'Dr'
                     WHERE CID = {};
                  """.format(bal, cid)
        print(sql)
        try:
            # Execute the SQL command
            c.executescript(sql)
            # Commit your changes in the database
            conn.commit()
            print("data updated successfully...")
        except:
            # Rollback in case there is any error
            conn.rollback()
            print('Error')
    conn.close()

def viewBalance():
    conn = sqlite3.connect('MyBank.db')
    c = conn.cursor()
    cid = int(input("Enter custumor id : "))
    c.execute("select CID, cName, Balance from Customer where cid = {};".format(cid))
    result = c.fetchall()
    # print(result)
    print('CID , CName,  Balance')
    for i in result:
        print(i)
    conn.close()

def viewCustomerList():
    conn = sqlite3.connect('MyBank.db')
    c = conn.cursor()
    c.execute("select * from Customer;")
    result = c.fetchall()
    # print(result)
    print('CID , CName,  FName, Phone No., Balance, Trans_Type')
    for i in result:
        print(i)
    conn.close()

while (True):
    print("\n\n==========Banking Project========")
    print("1: Add Customer")
    print("2: Deposit Money")
    print("3: Withdraw Money")
    print("4: View Balance")
    print("5: View Customer List")
    print("6: Exit")

    print("\n")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        addCustomer()
    elif ch == 2:
        deposit()
    elif ch == 3:
        withdraw()
    elif ch == 4:
        viewBalance()
    elif ch == 5:
        viewCustomerList()
    elif ch == 6:
        exit()
    else:
        print("You have entered the wrong choice, Try again...")