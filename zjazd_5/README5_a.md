### 02.12.2018 
####MVC
Model
Vidok
Controller

##Dash
https://dash.plot.ly/installation

`
pip install dash==0.31.1  # The core dash backend
pip install dash-html-components==0.13.2  # HTML components
pip install dash-core-components==0.38.1  # Supercharged components
pip install dash-table==3.1.7  # Interactive DataTable component (new!)
`
przykład: ```ex_1.py```
https://dash.plot.ly/getting-started

open in webview http://127.0.0.1:8050/

---
* ex_3.py
http://flask.pocoo.org/
request
response



---
* nginx -serwer http 
* bing.com -wyszukiwarka [https://www.bing.com/?toWww=1&redig=D4CBD3C91B214C33921F6735AFD767ED]

---
* http.apache.com
* https://httpd.apache.org/

---
otwórz cmd i  wpisz > ping wp.pl

---
dane.gov.pl -zbiory danych

---

## Django
https://docs.djangoproject.com/en/2.1/
https://www.pythonanywhere.com/ -utworzenie apki w chmurze za free
werkzeug.pocoo.org
www.heroku -utworzenie apki w chmurze za free
vipserv.org -utworzenie apki w chmurze za free

`pip install django`

www.humblebundle.com -shop with pycharm and python

TERMINAL:
w katalogu django_examples (startproject + nazwa projektu)
`django-admin startproject exercises`

`(venv) C:\Users\kurs\PycharmProjects\bootcamp\zjazd_5\django_examples\exercises>python manage.py`
`zjazd_5\django_examples\exercises>python manage.py runserver`

* admin.dane.gov.pl -example, panel administratora

---
zjazd_5\django_examples\exercises>python manage.py
zjazd_5\django_examples\exercises>python manage.py createsuperuser

błąd bo nie mamy pliku - trzeba najpierw zrobic migrate:
- plik ktory powie bazie danych jakie zmiany ma dokonac na istniejacych tabe;ach
python manage.py migrate
zjazd_5\django_examples\exercises>python manage.py createsuperuser

--
sqlite browser -do podgladu bazyu danych
https://sqlitebrowser.org/

---
\zjazd_5\django_examples\exercises>python manage.py createsuperuser

wejdz na db browser for sql
sprawdzam dodanie użytkownika
nastepnie moge sie zalogowac na:

http://127.0.0.1:8000/admin/

---
(venv) C:\Users\kurs\PycharmProjects\bootcamp\zjazd_5\django_examples\exercises>python manage.py runserver
http://127.0.0.1:8000/admin/

#### MVC
Model-View-Controller

#### MVT django
https://www.tutorialspoint.com/django/django_overview.htm

#### Widoki

---
w pliku urls.py mozemy dodac funkcje....
```python
"""
from django.contrib import admin
from django.http import HttpResponse, response
from django.urls import path

def main_page(request):
    return HttpResponse(content="To jest main page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main_page)
]
```
(venv) C:\Users\kurs\PycharmProjects\bootcamp\zjazd_5\django_examples\exercises>python manage.py runserver

---
python manage.py startapp mainpage

nastepnie:
```python

from django.contrib import admin

from django.urls import path

from zjazd_5.django_examples.exercises.mainpage.views import main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main_page),
]

```

a w pliku powstalym views.py
```python
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, response

def main_page(request):
    return HttpResponse(content="To jest main page")
```

Do uruchomienia przeglądarki:
(venv) C:\Users\kurs\PycharmProjects\bootcamp\zjazd_5\django_examples\exercises>python manage.py runserver

---
uruchom debugger
postaw kropke i wejdz na strone odpowiednia
- mozna podejrzez zapytania
- kto jest zalogowany
- jaka jest metoda
- 

---
