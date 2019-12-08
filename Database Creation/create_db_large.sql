CREATE TABLE Student (
student_ID Varchar(20),
name Varchar(40),
department Varchar(40),
year Int,
PRIMARY KEY (name)
);


CREATE TABLE Bus (
bus_number Varchar(40),
start_hour Int,
End_hour Int,
PRIMARY KEY (bus_number)
);

CREATE TABLE Take_Leave (
Student_name Varchar(40),
Bus_number Varchar(40),
bus_date date,
PRIMARY KEY (Student_name, Bus_number,bus_date),
FOREIGN KEY(Student_name) REFERENCES Student (name),
FOREIGN KEY(Bus_number) REFERENCES Bus (bus_number)
);


CREATE TABLE Bus_Station (
name Varchar(40) ,
location Varchar(40),
PRIMARY KEY (name)
);

CREATE TABLE Stop (
Bus_Station_name Varchar(40),
Bus_number Varchar(40),
PRIMARY KEY (Bus_Station_name, Bus_number),
FOREIGN KEY(Bus_Station_name) REFERENCES Bus_Station (name),
FOREIGN KEY(Bus_number) REFERENCES Bus (bus_number)
);



CREATE TABLE Google_Map_Review (
Student_name Varchar(40),
Bus_Station_name Varchar(40),
Score Int,
PRIMARY KEY (Student_name, Bus_Station_name),
FOREIGN KEY(Student_name) REFERENCES Student (name),
FOREIGN KEY(Bus_Station_name) REFERENCES Bus_Station (name)
);


CREATE TABLE Apartment (
name Varchar(40),
location Varchar(40),
PRIMARY KEY (name)
);


CREATE TABLE Near_Apt_Bus (
Apartment_name Varchar(40),
Bus_Station_name Varchar(40),
PRIMARY KEY (Apartment_name, Bus_Station_name),
FOREIGN KEY(Apartment_name) REFERENCES Apartment (name),
FOREIGN KEY(Bus_Station_name) REFERENCES Bus_Station (name)
);



CREATE TABLE Live (
student_name Varchar(40),
Apartment_name Varchar(40),
PRIMARY KEY (student_name,Apartment_name),
FOREIGN KEY(student_name) REFERENCES Student (name),
FOREIGN KEY(Apartment_name) REFERENCES Apartment (name)
);



CREATE TABLE School_Building (
name Varchar(40),
location Varchar(40),
department Varchar(40),
PRIMARY KEY (name)
);

CREATE TABLE Take_Class (
student_name Varchar(40),
School_Building_name Varchar(40),
PRIMARY KEY (student_name, School_Building_name),
FOREIGN KEY(student_name) REFERENCES Student (name),
FOREIGN KEY(School_Building_name) REFERENCES School_Building (name)
);


CREATE TABLE Near_Apt_School (
Apartment_name Varchar(40),
School_Building_name Varchar(40),
PRIMARY KEY (Apartment_name, School_Building_name),
FOREIGN KEY(Apartment_name) REFERENCES Apartment (name),
FOREIGN KEY(School_Building_name) REFERENCES School_Building (name)
)
