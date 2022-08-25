import sqlite3
conn = sqlite3.connect("demo.db")
cur = conn.cursor()
cur.execute("drop table Surya")
cur.execute("create table Surya(id int, name text, marks Real)")
cur.execute("insert into Surya VALUES(1,'teja', 55.66)")
cur.execute("insert into Surya VALUES(1,'nandini', 55.66)")
cur.execute("insert into Surya VALUES(1,'sravanti', 55.66)")

result = cur.execute("select * from Surya")
print(result.fetchall())

conn.commit()
conn.close()
# cur.execute("insert into Surya VALUES(1,'chandana', 55.66)")
conn = sqlite3.connect("demo.db")
cur = conn.cursor()
# result = cur.execute("select * from Surya")
result = cur.execute("select id, marks from Surya")
print(result.fetchall())

