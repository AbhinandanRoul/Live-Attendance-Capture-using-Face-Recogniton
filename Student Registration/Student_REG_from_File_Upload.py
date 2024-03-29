import streamlit as st,pyrebase,mysql.connector,cv2
import os
import PIL.Image
from PIL.Image import Image
k=os.path.exists("temp")
if(k==False):
    os.mkdir("temp")
st.title("Student Registration")
Name=st.text_input("Name")
Email=st.text_input("Email")
reg =st.text_input("Registration Number")
known_img=st.file_uploader("Upload Image", type=["png","jpg","jpeg"])
if (st.button("Submit") == True):
    def convertToBinaryData(filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def insertBLOB(reg_num, Name, Email, Photo):
        mydb = mysql.connector.connect(host="localhost", database="giraffe", user="root", password="1234")
        my_cursor = mydb.cursor()
        sql_insert_blob_query = "INSERT INTO registration (Reg, NAME, EMAIL, Photo) VALUES (%s,%s,%s,%s)"
        converted_picture = convertToBinaryData(Photo)
        # Convert data into tuple format
        insert_blob_tuple = (reg_num, Name, Email, converted_picture)
        result = my_cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        mydb.commit()
        print("Image inserted successfully as a BLOB into students table", result)

    def save_uploadedfile(uploadedfile):
        with open(os.path.join("temp", uploadedfile.name), "wb") as f:
            f.write(uploadedfile.getbuffer()) # Writes the file to directory Local
        insertBLOB(reg, Name, Email, 'temp/{}'.format(uploadedfile.name)) # Calls function to insert the photo and details into SQL
        return st.success("Successfully Registered")

    if(known_img!=None):
        save_uploadedfile(known_img)
