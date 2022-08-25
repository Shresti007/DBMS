import sqlite3


conn = sqlite3.connect('teja.db')
cur = conn.cursor()
print('Database opened')


cur.execute(" INSERT INTO employee_records(ID,NAME,DIVISION,STARS) VALUES(5,'James','Maintenance',4)")


def insert_record(ID,NAME,DIVISION,STARS):
    cur.execute(''' INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
    VALUES(?,?,?,?)''',(ID,NAME,DIVISION,STARS))

insert_record(1,'Surya','Hardware',5)
insert_record(2,'Teja','Rhishikesh',5)
insert_record(3,'mohan','Rudraprayag',5)
insert_record(4,'Venkat','nandak',5)
insert_record(5,'Ananta','devprayag',5)
insert_record(6,'Shresti','Gangotri',5)


def read_Data():
    # from math import *
    data = cur.execute(''' SELECT * FROM employee_records ORDER BY NAME''')
    for record in data:
        print('ID : '+str(record[0]))
        print('NAME : '+str(record[1]))
        print('DIVISION : '+str(record[2]))
        print('STARS : '+str(record[3])+'\n')


read_Data()

def update_record():
    cur.execute(''' UPDATE employee_records set STARS=3 WHERE ID=2 ''')
    print('Updated')


def delete_record():
    cur.execute(''' DELETE from employee_records WHERE ID = 1 ''')
    print('Deleted')

delete_record()

def check_Data():
    # from math import *
    data = cur.execute(''' SELECT NAME FROM employee_records WHERE ID =2''')
    x = data.fetchall()
    if x == []:
        print('Doesnt exist')
    else:
        print (x)

def update_record():
    cur.execute(''' UPDATE employee_records set STARS=3 WHERE ID=2 ''')
    print('Updated')

conn.commit()
conn.close()

















