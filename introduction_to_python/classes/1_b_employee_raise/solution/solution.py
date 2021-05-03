class Employee:

    def __init__(self,name,employee_id,salary,years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company

    def give_raises():
        if Employee.years_at_company<=5:
            Employee.salary = Employee.salary+5000
        elif 5<employee_lst.years_at_company<10:
            Employee.salary = Employee.salary+8000
        else:
            Employee.salary = Employee.salary+10000