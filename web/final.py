# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:54:09 2019

@author: zyy19
"""
import psycopg2
import connection
from bottle import route, run, template, request

@route('/')
def main():
    return template("main")


@route('/results/')
def results():
    return template("results")

@route('/edit/<student_id>')
def edit(student_id):
    cursor.execute("SELECT * FROM student where student_id = '"+str(student_id)+"'")
    record = cursor.fetchall()[0]
    return template("edit", data=record)


@route('/edit',  method='POST')
def edit_student():
    student_name = request.forms.get('name')
    student_id = request.forms.get('ID')
    department = request.forms.get('Department')
    year = request.forms.get('Year')
    
    
    cursor.execute("SELECT * FROM student where name = '"+str(student_name)+"'")
    record = cursor.fetchall()
    if record:
        cursor.execute("DELETE FROM live where student_name = '"+str(student_name)+"'")
        cursor.execute("DELETE FROM take_class where student_name = '"+str(student_name)+"'")
        cursor.execute("DELETE FROM take_leave where student_name = '"+str(student_name)+"'")
        cursor.execute("DELETE FROM google_map_review where student_name = '"+str(student_name)+"'")
        cursor.execute("DELETE FROM student where name = '"+str(student_name)+"'")
    cursor.execute("INSERT INTO student VALUES ('" +str(student_id)+"'," +
                                               "'" +str(student_name)+"',"+
                                               "'" +str(department)+"',"+
                                               str(year) + ")")
    return "Successfully Update!"


@route('/add_student')
def add():
    return template("add_student")


@route('/add_student',  method='POST')
def add_student():
    student_name = request.forms.get('name')
    student_id = request.forms.get('ID')
    department = request.forms.get('Department')
    year = request.forms.get('Year')
    
    cursor.execute("SELECT * FROM student where name = '"+str(student_name)+"'")
    record = cursor.fetchall()
    if len(record) > 0:
        return "This Student Already Exists!"
    
    
    cursor.execute("insert into student values ('" + str(student_id) + "', "+
                                               "'" + str(student_name) + "', "+
                                               "'" + str(department) + "', "+
                                               str(year) + " )")

    return "Successfully Add!"


@route('/delete/<student_id>')
def delete(student_id):
    cursor.execute("SELECT * FROM student where student_id = '"+str(student_id)+"'")
    records = cursor.fetchall()
    if len(records) > 0:
        return template("delete", data=records[0])
    else:
        return template("main")


@route('/delete/<student_id>',  method='POST')
def delete_student(student_id):
    cursor.execute("SELECT * FROM student where student_id = '"+str(student_id)+"'")
    record = cursor.fetchall()[0]
    student_name = record[1]
    cursor.execute("DELETE FROM live where student_name = '"+str(student_name)+"'")
    cursor.execute("DELETE FROM take_class where student_name = '"+str(student_name)+"'")
    cursor.execute("DELETE FROM take_leave where student_name = '"+str(student_name)+"'")
    cursor.execute("DELETE FROM google_map_review where student_name = '"+str(student_name)+"'")
    cursor.execute("DELETE FROM student where name = '"+str(student_name)+"'")
    
    return "Successfully Delete!"



@route('/',  method='POST')
def display():
    student_name = request.forms.get('name').strip()
    student_id = request.forms.get('ID').strip()
    Department = request.forms.get('Department').strip()
    query = "SELECT * FROM student where" 
    if len(student_name) > 0:
        query += " name like '%"+str(student_name) + "%'"
    if len(student_id) > 0:
        query += " and student_id = '" + str(student_id) + "'"
    if len(Department) > 0:
        query += " and department = '" + str(Department) + "'"
        
    if len(student_name) == 0 and len(student_id)== 0 and len(Department) == 0:
        query = "SELECT * FROM student" 
    
    cursor.execute(query)
    records = cursor.fetchmany(20)
    return template('results',data=records)


@route('/show_bus/<student_id>')
def show_bus(student_id):
    cursor.execute("select student.name,\
       student.student_id,\
       student.department,\
       student.year,\
       take_leave.bus_date,\
       bus.bus_number,\
       bus.start_hour,\
       bus.end_hour\
       from student\
       inner join take_leave on student.name = take_leave.student_name\
       inner join bus on take_leave.bus_number = bus.bus_number\
       where student.student_id = '"+str(student_id) +"'")
    
    record = cursor.fetchall()
    return template('show_bus',data=record)


@route('/add_bus/<student_id>')
def add_bus(student_id):
    cursor.execute("select student.name,\
       student.student_id,\
       student.department,\
       student.year,\
       take_leave.bus_date,\
       bus.bus_number,\
       bus.start_hour,\
       bus.end_hour\
       from student\
       inner join take_leave on student.name = take_leave.student_name\
       inner join bus on take_leave.bus_number = bus.bus_number\
       where student.student_id = '"+str(student_id) +"'")
     
    record = cursor.fetchall()[0]
    print(record)
    
    return template('add_bus', data=record)


@route('/add_bus',  method='POST' )
def add_bus_record():
    student_name = request.forms.get('name')
    #student_id = request.forms.get('ID')
    #department = request.forms.get('Department')
    #year = request.forms.get('Year')
    date = request.forms.get('date')
    number = request.forms.get('number')
    start_hour = request.forms.get('start')
    end_hour = request.forms.get('end')
    
    
    cursor.execute("select * from take_leave where bus_number = '%s' and student_name = '%s'"
                    % (str(number),str(student_name)))
    record = cursor.fetchall()
    if len(record) > 0:
        return "Please Change the Bus Number!"
    
    cursor.execute("insert into bus values ('"+str(number)+"',"+
                    str(start_hour) + "," + str(end_hour) + ")")
    cursor.execute("insert into take_leave values ('"+str(student_name)+"','"+
                    str(number) + "','" +  str(date) + "')")
    return "Successfully Add!"
    



if __name__ == '__main__':    
    # Connect to an existing database
    conn = psycopg2.connect(host=connection.url, dbname=connection.database, 
        user=connection.user, password=connection.password)
    
    cursor = conn.cursor()

    run(host='localhost', port=8080, debug=True)
    conn.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    