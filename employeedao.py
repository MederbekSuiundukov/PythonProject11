import sqlite3
from employee import Employee

class EmployeeDAO:
    def __init__(self, db_name='employee_db.sqlite'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                salary REAL NOT NULL,
                hire_date TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def insert(self, employee):
        query = '''
        INSERT INTO employee (name, position, salary, hire_date)
        VALUES (?, ?, ?, ?);
        '''
        self.conn.execute(query, (employee.name, employee.position, employee.salary, employee.hire_date))
        self.conn.commit()

    def get_by_id(self, id):
        query = 'SELECT * FROM employee WHERE id = ?;'
        cursor = self.conn.execute(query, (id,))
        row = cursor.fetchone()
        if row:
            return Employee(row[0], row[1], row[2], row[3], row[4])
        return None

    def get_all(self):
        query = 'SELECT * FROM employee;'
        cursor = self.conn.execute(query)
        employees = []
        for row in cursor:
            employees.append(Employee(row[0], row[1], row[2], row[3], row[4]))
        return employees

    def update(self, employee):
        query = '''
        UPDATE employee
        SET name = ?, position = ?, salary = ?, hire_date = ?
        WHERE id = ?;
        '''
        self.conn.execute(query, (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        self.conn.commit()

    def delete(self, id):
        query = 'DELETE FROM employee WHERE id = ?;'
        self.conn.execute(query, (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()