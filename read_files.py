from openpyxl import load_workbook
import re
import mysql.connector


mydb = mysql.connector.connect(user='sql8619611',
                               password='2QTInCNfQY',
                               host='sql8.freesqldatabase.com',
                               database='sql8619611',
                               port='3306')

correct = []


def read(number):
    wb = load_workbook(f'files/plik{number}.xlsx')
    sheet_name = "DZIECI"
    if sheet_name in wb.sheetnames.pop(0).upper():

        ws = wb.worksheets[0]

        global mydb,  mycursor

        mycursor = mydb.cursor()

        for row in ws.iter_rows(min_row=2, min_col=4, max_col=4):
            for cell in row:
                if cell.value is None:
                    mydb.commit()
                    return
                elif cell.value in correct:
                    continue
                else:
                    name, surname = re.split(r'\s(?=[a-z][A-Z])|\s', cell.value, maxsplit=1)

                    ofnames = ['NIKOL', 'NICOLE', 'NIKOLE', 'NEL', 'BERNEIKE', 'DORIS', 'DOLORES', 'NELLY', 'SALOME']

                    if str(name[-1]).upper() != 'A' or str(name) == 'KUBA' and str(name).upper() not in ofnames:
                        value(name, surname, "M")
                    else:
                        value(name, surname, "F")

                    correct.append(cell.value)


def value(name, surname, gender):
    execute_data = "INSERT INTO Test (`Name`, `Surname`, `Gender`) VALUES (%s, %s, %s)"
    data = (name, surname, gender)
    mycursor.execute(execute_data, data)
