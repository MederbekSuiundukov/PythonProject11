class Employee:
    def __init__(self, id=None, name=None, position=None, salary=None, hire_date=None):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date

    def __str__(self):
        return f"Employee(ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Hire Date: {self.hire_date})"

    # Getters and Setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_hire_date(self):
        return self.hire_date

    def set_hire_date(self, hire_date):
        self.hire_date = hire_date