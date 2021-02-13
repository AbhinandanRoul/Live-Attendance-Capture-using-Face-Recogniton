# requirements: pip install mysql-connector-python
"""
mysql> CREATE DATABASE giraffe
mysql> USE giraffe
mysql> CREATE TABLE students(reg INT NOT NULL PRIMARY KEY, email VARCHAR(30) NOT NULL, name VARCHAR(30) NOT NULL, photo LONGBLOB);

"""

import mysql.connector

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(reg_num, emp_id, name, photo):
    mydb = mysql.connector.connect(host="localhost", database="giraffe", user="root", password="password123")
    my_cursor = mydb.cursor()
    sql_insert_blob_query = "INSERT INTO students (reg, email, name, photo) VALUES (%s,%s,%s,%s)"

    empPicture = convertToBinaryData(photo)

    # Convert data into tuple format
    insert_blob_tuple = (reg_num, emp_id, name, empPicture)
    result = my_cursor.execute(sql_insert_blob_query, insert_blob_tuple)
    mydb.commit()
    print("Image inserted successfully as a BLOB into students table", result)


insertBLOB(1941012333, "Bravish.Ghosh@outlook.com", "Bravish Ghosh", "/Users/loopglitch/Pictures/my_img1.jpg")
