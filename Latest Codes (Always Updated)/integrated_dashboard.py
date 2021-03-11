import streamlit as st, mysql.connector

st.title("REGISTRATION")
import streamlit as st

add_selectbox = st.sidebar.selectbox(
    "NAVIGTION",
    ("Student Registration", "Faculty Registration")
)
if(add_selectbox=="Student Registration"):
    import streamlit as st, pyrebase, mysql.connector, cv2
    import os
    import PIL.Image
    from PIL.Image import Image

    k = os.path.exists("temp")
    if (k == False):
        os.mkdir("temp")
    st.header("Student Registration")
    Name = st.text_input("Name")
    Email = st.text_input("Email")
    reg = st.text_input("Registration Number")
    password = st.text_input("Password", type="password")
    password_check = st.text_input("Re enter Password", type="password")
    if (password != password_check):
        st.warning("Passwords don't match")
    known_img = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if ((st.button("Submit") == True) and password == password_check):

        def convertToBinaryData(filename):
            # Convert digital data to binary format
            with open(filename, 'rb') as file:
                binaryData = file.read()
            return binaryData


        def insertBLOB(reg_num, Name, Email, Photo, password):
            mydb = mysql.connector.connect(host="localhost", database="giraffe", user="root", password="1234")
            my_cursor = mydb.cursor()
            sql_insert_blob_query = "INSERT INTO registration (Reg, NAME, EMAIL, Photo, password) VALUES (%s,%s,%s,%s,%s)"
            converted_picture = convertToBinaryData(Photo)
            # Convert data into tuple format
            insert_blob_tuple = (reg_num, Name, Email, converted_picture, password)
            result = my_cursor.execute(sql_insert_blob_query, insert_blob_tuple)
            mydb.commit()
            print("Image inserted successfully as a BLOB into students table", result)


        def save_uploadedfile(uploadedfile):
            with open(os.path.join("temp", uploadedfile.name), "wb") as f:
                f.write(uploadedfile.getbuffer())  # Writes the file to directory Local
            insertBLOB(reg, Name, Email, 'temp/{}'.format(uploadedfile.name),
                       password)  # Calls function to insert the photo and details into SQL
            return st.success("Successfully Registered")


        if (known_img != None):
            save_uploadedfile(known_img)
else:

    # ------------------Subject Config---------------------------------
    subject_ID = ['subject1', 'subject2', 'subject3', 'subject4', 'subject5']
    subject_config = ['MTH1001', 'CSE1001', 'EET1001', 'CHM1001', 'ENG1001']
    # ------------------Subject Config---------------------------------

    st.header("Faculty Registration")
    Name = st.text_input("Name")
    Email = st.text_input("Email")
    reg = st.text_input("Enter Faculty ID")
    password = st.text_input("Password", type="password")
    password_check = st.text_input("Re enter Password", type="password")
    if (password != password_check):
        st.warning("Passwords don't match")

    classID = st.selectbox("Select your subject", subject_config)
    if ((st.button("Submit") == True) and password == password_check):
        idx = subject_config.index(classID)
        classID = subject_ID[idx]
        def facultyregistration(Reg, Name, Email, Password, Subject):
            mydb = mysql.connector.connect(host="localhost", database="giraffe", user="root", password="1234")
            my_cursor = mydb.cursor()
            sql_insert_blob_query = "INSERT INTO facultyreg (Reg, Name, Email,Password, Subject) VALUES (%s,%s,%s,%s,%s)"
            insert_blob_tuple = (Reg, Name, Email,Password, Subject)
            result = my_cursor.execute(sql_insert_blob_query, insert_blob_tuple)
            mydb.commit()
        facultyregistration(reg, Name, Email, password, classID)
        st.success("You are registered")






