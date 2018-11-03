class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.worked_hours = 0

    def pay_salary(self):
        to_pay = self.worked_hours * self.stawka
        self.worked_hours = 0
        return to_pay

    def register_time(self, hours):
        self.worked_hours = hours


def test_employee():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.imie == "Jan"
    assert employee.nazwisko == "Nowak"
    assert employee.stawka == 100.0


def test_employee_pay_salary_with_no_worked_hours():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.pay_salary() == 0


def test_employee_pay_salary_with_worked_hours():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500


def test_employee_pay_salary_after_salary_was_payed():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0


def test_employee_pay_salary_overhours():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    assert employee.pay_salary() == 8 * 100 + 2 * 2 * 100


# Utwórz klasę Company. Ktora inicjalizuje sie z nazwa:
# >>> employee = Employee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> google = Company("google")
# >>> google.add_employee(employee)
# >>> google.size()
# 1
# >>> google.pay_all_salary()
# 500
# >>> google.pay_all_salary()
# 0
# >>> employee2 = Employee('Krzysztof', 'Nowak', 200.0)
# >>> employee2.register_time(5)
# >>> google.pay_all_salary()
# >>> google.add_employee(employee2)
# >>> google.pay_all_salary()
# 1000
