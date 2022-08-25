import sqlite3
conn = sqlite3.connect("demo.db")
cur = conn.cursor()
# cur.execute("drop table student")
cur.execute("CREATE TABLE student(id INT PRIMARY KEY, name TEXT, marks REAL)")
# cur.execute("DROP TABLE student")
cur.execute("INSERT INTO student VALUES(1001,'Surya',77.66)")
cur.execute("INSERT INTO student VALUES(1002,'Teja',88.66)")
cur.execute("INSERT INTO student VALUES(1003,'Nandini',80.66)")
cur.execute("INSERT INTO student VALUES(1004,'Lakshmi',75.66)")
cur.execute("INSERT INTO student VALUES(1005,'Sankara',79.66)")
res = cur.execute("SELECT MIN(marks),MAX(marks),AVG(marks) FROM student")
print(res.fetchall())
cur.execute("DELETE FROM student WHERE id=1001")
cur.execute("DELETE FROM student WHERE id=1002")
res = cur.execute("SELECT * FROM student")
print(res.fetchall())
cur.execute("DELETE FROM student WHERE id=1003")
res = cur.execute("SELECT * FROM student")
print(res.fetchall())
conn.rollback()
res = cur.execute("SELECT * FROM student")
print(res.fetchall())
cur.execute("UPDATE student SET marks = 100 WHERE id >=1003")
res = cur.execute("SELECT * from student")
print(res.fetchall())
conn.commit()

"""
CREATE TABLE student(id INT PRIMARY KEY, name TEXT, marks REAL)
DROP TABLE student

INSERT INTO student VALUES(1001,'abc',55.66)

SELECT * FROM student
SELECT * FROM student WHERE cond
SELECT MIN(marks) FROM student

DELETE FROM student WHERE id=1001
UPDATE student SET marks = 100 WHERE id >=1003

commit - saving the changes
rollback - delete / update of rows

"""