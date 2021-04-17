# Note:
The master_tool file has all the dashboards, registration forms and the attendance tool.

# SQL commands

### To create a table for faculty registration

create table facultyreg (Reg INT NOT NULL PRIMARY KEY, Name varchar(30) NOT NULL, Email varchar(30) NOT NULL, Password varchar(30) NOT NULL, Subject varchar(20));

###  To create a table for student registration

create table registration (Reg INT NOT NULL PRIMARY KEY, NAME varchar(30) NOT NULL, EMAIL varchar(30) NOT NULL,Photo LONGBLOB, password varchar(30) NOT NULL);

### To create a table for each subject

create table subject1 (Reg INT NOT NULL PRIMARY KEY);
create table subject2 (Reg INT NOT NULL PRIMARY KEY);
create table subject3 (Reg INT NOT NULL PRIMARY KEY);
create table subject4 (Reg INT NOT NULL PRIMARY KEY);
create table subject5 (Reg INT NOT NULL PRIMARY KEY);
