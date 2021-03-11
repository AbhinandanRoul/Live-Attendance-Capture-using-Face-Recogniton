import mysql.connector, streamlit as st

# ------------------Subject Config---------------------------------
subject_ID = ['subject1', 'subject2', 'subject3', 'subject4', 'subject5']
subject_config = ['MTH1001', 'CSE1001', 'EET1001', 'CHM1001', 'ENG1001']
# ------------------Subject Config---------------------------------

st.header("Dashboard")
reg= st.text_input("Enter your registrationID")
password=st.text_input("Enter your password", type="password")
classID = st.selectbox("Select your subject", subject_config)

def password_validate(password):
    connection = mysql.connector.connect(host='localhost', database='giraffe', user='root', password='1234')
    cursor = connection.cursor()
    sql_validate = "select password FROM registration where Reg={}".format(reg)
    cursor.execute(sql_validate)
    result = cursor.fetchall()
    return result[0][0]


def findstudent(reg):
    connection = mysql.connector.connect(host='localhost', database='giraffe', user='root', password='1234')
    cursor = connection.cursor()
    sql_validate = "select NAME FROM registration where Reg={}".format(reg)
    cursor.execute(sql_validate)
    result = cursor.fetchall()
    st.write("The details are")
    for x in result:
        st.write("Name:",x[0])

def findattendance1(reg, subject_num):
    connection = mysql.connector.connect(host='localhost', database='giraffe', user='root', password='1234')
    cursor = connection.cursor()
    sql_attendance_subject="select * from `{subject}` where reg={registration}".format(subject=subject_num, registration=reg)
    cursor.execute(sql_attendance_subject)
    result = cursor.fetchall()
    st.write("Attendance for:", classID)
    count=0; total_present=0;
   # print(result[0][1])
    for k in result[0]:
        count += 1
        if(k=='1'):
            total_present+=1

    st.write("Total classes", count-1)
    st.write("Total present", total_present)
    st.write("Attendance Percentage", round((total_present/(count-1)*100),2))

if ((st.button("Submit") == True)):
    if (password==password_validate(reg)):
        st.success("Sucessfully Logged In")
        findstudent(reg)
        idx = subject_config.index(classID)
        classID_mapped = subject_ID[idx]
        findattendance1(reg,classID_mapped)
    else:
        st.error("Incorrect RegID or Password")
