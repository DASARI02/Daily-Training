import sqlite3


class EmployeeDatabase:
    def __init__(self, db_name="employee.db"):
        """Initialize the database connection and create the table if it doesn't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                empno INTEGER PRIMARY KEY,
                empname TEXT NOT NULL,
                location TEXT NOT NULL,
                deptid INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def add_employee(self, empno, empname, location, deptid):
        """Add a new employee to the database."""
        try:
            self.cursor.execute(
                "INSERT INTO employees (empno, empname, location, deptid) VALUES (?, ?, ?, ?)",
                (empno, empname, location, deptid)
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Employee with ID {empno} already exists.")

    def get_employee_by_id(self, empno):
        """Retrieve an employee by empno."""
        self.cursor.execute("SELECT * FROM employees WHERE empno = ?", (empno,))
        return self.cursor.fetchone()

    def update_employee(self, empno, deptid, location):
        """Update an employee's department and location."""
        self.cursor.execute(
            "UPDATE employees SET deptid = ?, location = ? WHERE empno = ?",
            (deptid, location, empno)
        )
        self.conn.commit()
        return self.cursor.rowcount > 0

    def get_all_employees(self):
        """Retrieve all employees."""
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()

    def get_employees_by_location(self, location):
        """Retrieve employees filtered by location."""
        self.cursor.execute("SELECT * FROM employees WHERE location = ?", (location,))
        return self.cursor.fetchall()

    def __del__(self):
        """Close the database connection when the object is deleted."""
        self.conn.close()
