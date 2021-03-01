import streamlit as st,pyrebase,mysql.connector,cv2
import os
import PIL.Image
from PIL.Image import Image

st.title("Student Registration")
Name=st.text_input("Name")
Email=st.text_input("Email")
reg =st.text_input("Registration Number")
known_img=st.file_uploader("Upload Image", type=["png","jpg","jpeg"])

def save_uploadedfile(uploadedfile):
    with open(os.path.join("temp", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to temp".format(uploadedfile.name))

save_uploadedfile(known_img)

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(reg_num, Name, Email, Photo):
    mydb = mysql.connector.connect(host="localhost", database="giraffe", user="root", password="1234")
    my_cursor = mydb.cursor()
    sql_insert_blob_query = "INSERT INTO registration (Reg, NAME, EMAIL, Photo) VALUES (%s,%s,%s,%s)"
    empPicture = convertToBinaryData(Photo)
    # Convert data into tuple format
    insert_blob_tuple = (reg_num, Name, Email, Photo)
    result = my_cursor.execute(sql_insert_blob_query, insert_blob_tuple)
    mydb.commit()
    print("Image inserted successfully as a BLOB into students table", result)

insertBLOB(reg, Name, Email, 'temp/known.png')
st.success("Successfully Registered")
