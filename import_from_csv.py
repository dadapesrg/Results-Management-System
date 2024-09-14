import sqlite3
import csv

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

with open('result_student.csv', 'r') as file:
    no_record = 0
    for row in file:
        cursor.execute(
            "INSERT INTO result_student VALUES (?,?,?,?)", row.split(","))
        connection.commit()
        no_record += 1
connection.close()
print("\n{} Records transfered".format(no_record))
