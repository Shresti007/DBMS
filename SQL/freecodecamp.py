import sqlite3
from employee import Employee
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('surya.db')
c = conn.cursor()
# c.execute("""CREATE TABLE employee (
            #first text,
            #last text,
            #pay integer)
             #""")
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Surya', 'Teja', 60000)
emp_3 = Employee('Nandini', 'lakshmi', 40000)

c.execute("INSERT INTO employee VALUES(?,?,?)",(emp_1.first, emp_1.last, emp_1.pay))
conn.commit()
c.execute("INSERT INTO employee VALUES (:first, :last, :pay)",{'first': emp_2.first,'last': emp_2.last,'pay': emp_2.pay })
conn.commit()
c.execute("select * from employee where last ='TEJA'")
print(c.fetchall())
conn.commit()
conn.close()