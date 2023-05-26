import mysql.connector

mydb = mysql.connector.connect(user='sql8619611',
                               password='2QTInCNfQY',
                               host='sql8.freesqldatabase.com',
                               database='sql8619611',
                               port='3306')


def value(name, surname, gender):
    mycursor = mydb.cursor()
    execute_data = "INSERT INTO Test (`Name`, `Surname`, `Gender`) VALUES (%s, %s, %s)"
    data = (name, surname, gender)
    mycursor.execute(execute_data, data)
    mydb.commit()
