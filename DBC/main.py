import mysql.connector  

connection = mysql.connector.connect(
            host="localhost",
            user="root",            
            password="Darkevil002",
            database="contact_info"      
        )

cursor = connection.cursor()

cursor.execute("use contact_info")
if connection.is_connected():
    print("Successfully connected to MySQL database!")

while True:

    print('''
    1.ADD
    2.DELETE
    3.UPDATE
    4.VIEW
    5.EXIT
    ''')

    choice = int(input("Enter your choice: "))


    if choice == 1:
        name = input("Enter name: ")
        phone_number = int(input("Enter Phone number: "))
        Email=input('Enter the Email: ')

        sql = "INSERT INTO contacts (name, phone_number,Email) VALUES (%s, %s,%s)"
        val = (name, phone_number,Email)

        cursor.execute(sql, val)
        connection.commit()
        print("Data inserted successfully")

        print()

    elif choice == 2:
        name = input("Enter name to delete: ")
        sql = "DELETE FROM contacts WHERE name = %s"
        val = (name,)

        cursor.execute(sql, val)
        connection.commit()
        print("Data deleted successfully")

        print()

    elif choice == 3:
        name = input("Enter name to update: ")
        new_phone_number = int(input("Enter new phone number: "))
        new_email=input('Enter the new Email: ')

        sql = "UPDATE contact SET phone_number = %s,Email=%s WHERE name = %s"
        val = (new_phone_number,new_email, name)

        cursor.execute(sql, val)
        connection.commit()
        print("Data updated successfully")

        print()

    elif choice == 4:
        sql = "SELECT * FROM contacts"
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            print(f"Name: {row[0]}, Phone Number: {row[1]},Email:{row[2]}")

        print()

    elif choice == 5:
        print("Exiting")
        break

    else:
        print("Invalid choice Please try again")
        print()