import sqlite3

def search_database(question):

    conn=sqlite3.connect("database/employee.db")

    cursor=conn.cursor()

    question=question.lower()

    if "rahul" in question:

        cursor.execute("SELECT * FROM employees WHERE name='Rahul'")

    elif "amit" in question:

        cursor.execute("SELECT * FROM employees WHERE name='Amit'")

    elif "priya" in question:

        cursor.execute("SELECT * FROM employees WHERE name='Priya'")

    else:

        conn.close()

        return None

    result=cursor.fetchone()

    conn.close()

    return result