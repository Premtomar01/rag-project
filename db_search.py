import sqlite3

DB_PATH = "database/employee.db"


def connect_database():
    """
    Create database connection.
    """

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    return conn


def fetch_all_employees(conn):
    """
    Fetch all employees.
    """

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    return cursor.fetchall()


def find_employee(question, employees):
    """
    Search employee name inside user question.
    """

    question = question.lower()

    for employee in employees:

        if employee["name"].lower() in question:

            return employee

    return None


def convert_to_dictionary(employee):
    """
    Convert sqlite row into dictionary.
    """

    if employee is None:
        return None

    return dict(employee)


def search_database(question):
    """
    Search employee information from database.

    Returns:
        Dictionary
        or
        None
    """

    try:

        conn = connect_database()

        employees = fetch_all_employees(conn)

        employee = find_employee(question, employees)

        conn.close()

        return convert_to_dictionary(employee)

    except Exception as e:

        print("Database Error :", e)

        return None


# ------------------------------------
# Testing
# ------------------------------------

if __name__ == "__main__":

    questions = [

        "What is Rahul salary?",

        "Show Amit department",

        "What is Priya email?",

        "Who is Rohit?",

        "Employee Rahul"

    ]

    for question in questions:

        print("=" * 60)

        print(question)

        print(search_database(question))