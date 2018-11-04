03112018
Wprowadzenie do klas
print(azor)
print(type(azor))
print(dir(azor))
print(azor.gatunek)
print(rudolf.gatunek)

dziedziczenie
jupyter - do analizy danych

Do uruchomienia jupyter:
jupyter-noptebook [wpisz w folderze gdzie znajduje sie formularz jupyter]

----------------------------------------------
# Utwórz klasę Company. Ktora inicjalizuje sie z nazwa:
# >>> employee = Employee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> google = Company("google")
# >>> google.add_employee(employee)
# >>> google.size()
# >>> 1
# >>> google.pay_all_salary()
# >>> 500
# >>> google.pay_all_salary()
# >>> 0


----------------------------------------------


def count_total_price(self):
    sum_ = 0
    for e in self.entries:
        sum_ += e.product.price * e.quantity
        return sum_

----------------------------------------------
be1 = (1, "woda", 10)
be2 = (2, "Piwo", 23)
be3 = (3, "Ser", 4)
basket_entry = (be1, be2, be3)
basket_entry = (be1.name, be2, be3)
print(be1)
(1, 'woda', 10)
print(be1, be2, be3)
(1, 'woda', 10) (2, 'Piwo', 23) (3, 'Ser', 4)
------
be1
Out[14]: (1, 'woda', 10)
------
print(be1)
(1, 'woda', 10)
------
str(be1)
Out[16]: "(1, 'woda', 10)"
-----
f'{be1}'
Out[18]: "(1, 'woda', 10)"