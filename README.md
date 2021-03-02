# Live-Attendance-Capture-using-Face-Recogniton
Live Video Feed Based Attendance Capture System
## Installation instructions
Update the path to an empty directory having only your photo<br>
`pip install -r requirements.txt`<br>
`streamlit run stapp.py`<br>
Go to the localhost link displayed in terminal<br>
PS- Don't Forget to chnage the photo paths<br>
SQL CODE to initialize attendance list<br>
`mysql> CREATE DATABASE giraffe`<br>
`mysql> USE giraffe`<br>
`mysql> CREATE TABLE attendancelist(Reg INT NOT NULL PRIMARY KEY, Name varchar(30) NOT NULL,
email VARCHAR(30) NOT NULL, CourseID varchar(30), Date varchar(30), Time varchar(30),
Status varchar (30));`<br>
SQL Code to Initialize Student Registration <br>
`CREATE DATABASE giraffe;`<br>
`USE giraffe;`<br>
 `CREATE TABLE registration(Reg INT NOT NULL PRIMARY KEY, NAME varchar(30) NOT NULL, EMAIL VARCHAR(30) NOT NULL, Photo LONGBLOB);`



