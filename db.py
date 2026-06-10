import sqlite3

conn = sqlite3.connect("database/employee.db")

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS employees(

id INTEGER PRIMARY KEY,

name TEXT,

department TEXT,

leave_balance INTEGER,

salary INTEGER

)

""")

employees=[

(1,"Rahul","IT",8,50000),

(2,"Amit","HR",12,60000),

(3,"Priya","Finance",10,55000)

]

cursor.executemany(

"INSERT OR REPLACE INTO employees VALUES(?,?,?,?,?)",

employees

)

conn.commit()

conn.close()

print("Database Ready")