#### 17.11.2018
###Pakiety i moduły
`from sys`
from zjazd_3.Zadanie6 import Vector

from zjazd_4.mathematica.mathematica.geometry.figures import square_area
from zjazd_4.mathematica.mathematica.geometry.figures import triangle_area


def test_square_area():
    assert square_area(5) == 25


def test_triangle_area():
    assert triangle_area(4, 5) == 10

def square_area(n):
    return n ** 2


def triangle_area(base, height):
    return (base * height) / 2

print(__name__)
if __name__ = "main__"

http://api.nbp.pl/api/exchangerates/tables/A/?format=json
-----
import json
import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A/?format=json") as f:
    print(f)
    kursy = json.loads(f.read())

rates = kursy[0]['rates']
for r in rates:
    print(f"{r['code']} - {r['mid']}")
-----------
import json
import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/A/?format=json") as f:
    print(f)
    kursy = json.loads(f.read())

rates = kursy[0]['rates']
for r in rates:
    print(f"{r['code']} - {r['mid']}")

######

waluta = input("Jaka waluta z powyższej listy")
ile = float(input(f"Ile hcesz kupic {waluta}?"))

for r in rates:
    if r['code'] == waluta:
        result = ile *r['mid']

print("płacisz", result)
---------------------------
www.metaweather.com/api/
---------------------------
### 18.11.2018
####Biblioteki standardowe
import tkinter

---
# zadanie3 tkinter 
# 2 przykłady - drugi na GIT z użyciem GRID-a
import tkinter

def sumuj():
    a = float(a_entry.get())
    b = float(b_entry.get())
    wynik.configure(text = a+b)

root = tkinter.Tk()

a_label = tkinter.Label(master=root, text="Parametr a")
a_label.pack()

a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="Parametr a")
b_label.pack()

b_entry = tkinter.Entry(master=root)
b_entry.pack()


wynik_label = tkinter.Label(master=root, text="Wynik")
wynik_label.pack()
wynik = tkinter.Label(master=root, text=" - ")
wynik.pack()

policz_button = tkinter.Button(master=root, text="Policz", command=sumuj)
policz_button.pack()

root.title("Sumator")
root.mainloop()
---
# scv_example.py
# 
import csv

with open("dane/titanic_train.csv") as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    # print(data)
    dlugosci = set()
    for row in data:
        # print(row)
        dlugosci.add(len(row))
    print(dlugosci) # liczy ile kolumn ma każdy wiersz
-----
```python

# liczba osób z 0 i z 1 
# scv_example.py
import csv

with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    dlugosci = {}
    for row in data:
        # print(row)
        dlugosci[row['Survived']] = dlugosci.get(row['Survived'], 0) + 1
    print(dlugosci)  # liczy ile kolumn ma każdy wiersz
```
---------
https://realpython.com/python-csv/
---------
#### przyklad_tworzenia_pptx.py
##### zapisuje do Power Point-a
```python
from pptx import Presentation

prs = Presentation()

slide_layout = prs.slide_layouts[1]

slide = prs.slides.add_slide(slide_layout)
shapes = slide.shapes

title_shape = shapes.title

body_shape = shapes.placeholders[1]

title_shape.text = "Jakiś tekst"

tf = body_shape.text_frame
tf.text = "Zawartość tekst frame"

p = tf.add_paragraph()
p.text = "Kobiety"
p.level = 1

p = tf.add_paragraph()
p.text = "Przeżyło"
p.level = 1

prs.save('raport.pptx')
```
-------
```python
print()

```
### WYKRES
import matplotlib.pyplot as plt

dane = [70, 80]
index = ["konbiety", "mezczyzni"]
colors = ["r", "g"]

plt.bar(index, dane, color=colors)
plt.show()
------
Save ranges from Excel documents as images
https://pypi.org/project/excel2img/
------
# ipconfig
import os

x = os.system("ipconfig")
print(x)
-------
# scrapping
from requests import get

url = "https://plot.ly/python/static-image-export/"

response = get(url)
print(response)
---2 
from requests import get

url = "https://plot.ly/python/static-image-export/"

response = get(url)
print(response.text)
---
#REGEX
import re

patter = re.compile("\d{3}")

text = "123"

print(patter.findall(text))

----


