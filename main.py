class Employee:
    # Class variable to store all assigned employee IDs
    assigned_ids = set()

    def __init__(self, name, emp_id, title, department):
        if not name or not emp_id or not title or not department:
            raise ValueError("Please enter valid values for employee.")
        
        if emp_id in Employee.assigned_ids:
            raise ValueError(f"Employee ID '{emp_id}' is not unique. Please choose a different ID.")

        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

        # Add the assigned employee ID to the set
        Employee.assigned_ids.add(emp_id)

    def get_department(self):
        return self.department

    def __str__(self):
        return f"Name: {self.name}, ID: {self.emp_id}, Title: {self.title}, Department: {self.department}"

    def remove(self):
        try:
            Employee.assigned_ids.remove(self.emp_id)
        except AttributeError:
            print("Invalid Employee ID")


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.remove()
                self.employees.remove(employee)
                return True
        return False

    def list_employees(self):
        print(f"Employees in {self.name} department:")
        for employee in self.employees:
            print(employee)

    def remove_all_employees(self):
        emp_ids = []
        for employee in self.employees:
            emp_ids.append(employee.emp_id)
            employee.remove()
            self.employees.remove(employee)
            del employee
        return emp_ids

    def __str__(self):
        return f"Department: {self.name}"


class Company:
    def __init__(self):
        self.departments = {}
        self.employees = {}

    def add_department(self, department_name, add_flag=False):
        if department_name and department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            if add_flag:
                print(f"Department '{department_name}' added successfully.")
        else:
            print(f"Department '{department_name}' already exists, or department name is invalid.")

    def remove_department(self, department_name):
        if department_name in self.departments:
            deleted_emp_ids = self.departments[department_name].remove_all_employees()
            del self.departments[department_name]
            for emp_id in deleted_emp_ids:
                self.employees.pop(emp_id)
            print(f"Department '{department_name}' removed successfully.")
        else:
            print(f"Department '{department_name}' not found.")

    def display_departments(self):
        print("List of Departments:")
        for department_name in self.departments:
            print(self.departments[department_name])

    def get_department(self, department_name):
        return self.departments.get(department_name, None)

    def get_employees(self):
        for employee in self.employees.values():
            print(employee)


def print_menu():
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. List Employees in Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. Display Departments")
    print("7. Display all company Employees")
    print("8. Exit")


def main():
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ")

        try:
            if choice == "1":
                name = input("Enter employee name: ")
                emp_id = input("Enter employee ID: ")
                title = input("Enter employee title: ")
                department = input("Enter employee department: ")

                # Add employee to department
                company.add_department(department)
                department_obj = company.get_department(department)

                try:
                    # Attempt to create an employee
                    employee = Employee(name, emp_id, title, department)
                except ValueError as e:
                    print(f"Error: {e}.")
                    continue

                department_obj.add_employee(employee)
                company.employees[emp_id] = employee
                print("Employee added successfully.")

            elif choice == "2":
                emp_id = input("Enter employee ID to remove: ")

                # Remove employee from department
                try:
                    employee = company.employees[emp_id]
                    department_name = employee.get_department()
                    department_obj = company.departments[department_name]
                    if department_obj.remove_employee(emp_id):
                        print(f"Employee with ID {emp_id} removed successfully.")
                        company.employees.pop(emp_id)

                except KeyError:
                    print(f"Employee with ID {emp_id} not found.")

            elif choice == "3":
                department = input("Enter department name: ")

                # List employees in department
                department_obj = company.get_department(department)
                if department_obj:
                    department_obj.list_employees()
                else:
                    print(f"Department '{department}' not found.")

            elif choice == "4":
                department_name = input("Enter department name to add: ")

                # Add department
                company.add_department(department_name, True)

            elif choice == "5":
                department_name = input("Enter department name to remove: ")

                # Remove department
                company.remove_department(department_name)

            elif choice == "6":
                # Display all departments
                company.display_departments()

            elif choice == "7":
                company.get_employees()

            elif choice == "8":
                print("Exiting Employee Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
