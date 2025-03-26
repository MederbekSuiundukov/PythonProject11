from employee import Employee
from employeedao import EmployeeDAO

def main():

    dao = EmployeeDAO()


    employee1 = Employee(name="John Doe", position="Software Engineer", salary=75000.0, hire_date="2023-10-01")
    print("Inserted Employee: John Doe")


    retrieved_employee = dao.get_by_id(1)
    print("Retrieved Employee by ID:")
    print(retrieved_employee)

    print("All Employees:")
    for emp in dao.get_all():
        print(emp)


    employee1.set_salary(80000.0)
    dao.update(employee1)
    print("Updated Employee Salary:")
    print(dao.get_by_id(1))

    # Delete an employee
    dao.delete(1)
    print("Deleted Employee with ID 1")
    print("All Employees After Deletion:")
    for emp in dao.get_all():
        print(emp)

if __name__ == "__main__":
    main()