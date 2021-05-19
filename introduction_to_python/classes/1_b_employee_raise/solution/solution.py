class Employee:

    def __init__(self,name,employee_id,salary,years_at_company):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.years_at_company = years_at_company



def give_raises(employee_lst):
    for i in employee_lst:
        if i.years_at_company<=5:
            i.salary = i.salary+5000
        elif 5<i.years_at_company<10:
            i.salary = i.salary+8000
        else:
            i.salary = i.salary+10000