class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, emp):
        self.employees.append(emp)
        
    def search_by_age(self, target_age):
        result = []
        for emp in self.employees:
            if emp.age == target_age:
                result.append(emp)
        return result
    
    def search_by_name(self, target_name):
        result = []
        for emp in self.employees:
            if emp.name.lower() == target_name.lower():
                result.append(emp)
        return result
    
    def search_by_salary(self, condition, target_salary):
        result = []
        for emp in self.employees:
            if condition == '<' and emp.salary < target_salary:
                result.append(emp)
            elif condition == '>' and emp.salary > target_salary:
                result.append(emp)
            elif condition == '<=' and emp.salary <= target_salary:
                result.append(emp)
            elif condition == '>=' and emp.salary >= target_salary:
                result.append(emp)
        return result

def main():
    db = EmployeeDatabase()
    
    db.add_employee(Employee("161E90", "Raman", 41, 56000))
    db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    db.add_employee(Employee("171G30", "Ajay", 45, 44000))
    
    print("Search Parameters:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        target_age = int(input("Enter age to search: "))
        result = db.search_by_age(target_age)
    elif choice == 2:
        target_name = input("Enter name to search: ")
        result = db.search_by_name(target_name)
    elif choice == 3:
        condition = input("Enter condition (<, >, <=, >=): ")
        target_salary = int(input("Enter salary to search: "))
        result = db.search_by_salary(condition, target_salary)
    else:
        print("Invalid choice")
        return
    
    print("Search Results:")
    for emp in result:
        print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    main()
