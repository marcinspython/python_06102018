class Employee(object):
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def pay_salary(self):
        to_pay = self.worked_hours salary




def test_employee():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.name == "Jan"
    assert employee.surname == "Nowak"
    assert employee.salary == 100.0

def test_employee_pay_salary_with_no_worked_hours():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.pay_salary() == 0

#
# def test_pay_sallary():
#     employee = Employee('Jan', 'Nowak', 100.0)
#     assert register_time == 10
#     assert pay_salary() == 1200

