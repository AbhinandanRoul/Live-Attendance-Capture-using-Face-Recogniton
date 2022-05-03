# Note:
The master_tool file has all the dashboards, registration forms and the attendance tool.

# SQL commands

### To create a table for faculty registration

create table facultyreg (Reg INT NOT NULL PRIMARY KEY, Name varchar(30) NOT NULL, Email varchar(30) NOT NULL, Password varchar(30) NOT NULL, Subject varchar(20));

###  To create a table for student registration

create table registration (Reg INT NOT NULL PRIMARY KEY, NAME varchar(30) NOT NULL, EMAIL varchar(30) NOT NULL,Photo LONGBLOB, password varchar(30) NOT NULL);

### To create a table for each subject

create table subject1 (Reg INT NOT NULL PRIMARY KEY);<br>
create table subject2 (Reg INT NOT NULL PRIMARY KEY);<br>
create table subject3 (Reg INT NOT NULL PRIMARY KEY);<br>
create table subject4 (Reg INT NOT NULL PRIMARY KEY);<br>
create table subject5 (Reg INT NOT NULL PRIMARY KEY);<br>


### For Demo, the previous day attendance must be there for each subject<br>
If today `02-05-2022` then (take yesterday as absent)<br>
alter table subject1 add `01-05-2022` varchar(10);<br>
alter table subject2 add `01-05-2022` varchar(10);<br>
alter table subject3 add `01-05-2022` varchar(10);<br>
alter table subject4 add `01-05-2022` varchar(10);<br>
alter table subject5 add `01-05-2022` varchar(10);


## Populating SQL for demo:
/*alter table subject3 add `29-04-2022` varchar(10), 
add `30-04-2022` varchar(10), add `01-05-2022` varchar(10), add `02-05-2022` varchar(10);
insert into subject3 (`Reg`, `29-04-2022`,`30-04-2022`,`01-05-2022`,`02-05-2022`) values (19410123xx, 1,0,1,1);
select * from subject3;*/


