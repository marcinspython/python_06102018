class PremiumEmployee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka

    def give_bonus(self):
        pass


def test_employee():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    assert employee.imie == "Jan"
    assert employee.nazwisko == "Nowak"
    assert employee.stawka == 100.0

def test_employee_pay_salary_with_bonus():
    employee = PremiumEmployee('Jan', 'Nowak', 100.0)
    employee
    assert employee.give_bonus() == 1000