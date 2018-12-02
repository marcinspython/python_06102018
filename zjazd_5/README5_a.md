### 02.12.2018 

BOOK: Django Admin Cookbook
http://books.agiliq.com/projects/django-admin-cookbook/en/latest/

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

----------------
mathematica nowy projekt

python manage.py startapp maths "-w exercises nowy projekt"

w urls.py dodaje:
`    path("maths/<operation>/<int:arg_a>/<int:arg_b>", math_operations),`
nastepnie w nowym maths/views.py
```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def math_operations(request, operation, arg_a, arg_b):
    result = None
    if operation == "add":
        result = arg_a + arg_b
    elif operation == "sub":
        result = arg_a - arg_b

    return HttpResponse(result)
```
dodawanie typu zmiennej
`` path("maths/<operation>/<int:arg_a>/<int:arg_b>", math_operations),``

,,,
http://127.0.0.1:8000/maths/add/2/2
http://127.0.0.1:8000/maths/sub/2/2

---
dodawanie tych informacji do bazy danych:
definiujemy w pliku models - 
models.py 
- tworzymy klasę
```python
from django.db import models

# Create your models here.

class Math(models.Model):
    operation = models.CharField(max_length=10)
    arg_a = models.IntegerField()
    arg_b = models.IntegerField()


```
(venv) C:\Users\kurs\PycharmProjects\bootcamp\zjazd_5\django_examples\exercises>python manage.py makemigrations
w 
 settings.py
 
 
`INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'maths',
]`

exercises oznacz jako source root

```python
# Generated by Django 2.1.3 on 2018-12-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Math',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=10)),
                ('arg_a', models.IntegerField()),
                ('arg_b', models.IntegerField()),
            ],
        ),
    ]

```

(venv) C:\Users\kurs\PycharmProjects\bootcamp\zjazd_5\django_examples\exercises>python manage.py migrate

(venv) C:\Users\kurs\PycharmProjects\bootcamp\zjazd_5\django_examples\exercises>python manage.py migrate

---
w DB Browser
 mamy dodana tabele `maths_math`
 
 ---
 ```python
exercises>python manage.py shell
```
 (venv) C:\Users\kurs\PycharmProjects\bootcamp\zjazd_5\django_examples\exercises>python manage.py shell
-uruchamia konsole pytjhonowa do tworzenia obiektow bazy


```python
In [1]: from maths.models import Math

In [2]: Math.objects.create("add", 1,2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-07a0ebb6f2bc> in <module>
----> 1 Math.objects.create("add", 1,2)

~\PycharmProjects\bootcamp\venv\lib\site-packages\django\db\models\manager.py in manager_method(self, *args, **kwargs)
     80         def create_method(name, method):
     81             def manager_method(self, *args, **kwargs):
---> 82                 return getattr(self.get_queryset(), name)(*args, **kwargs)
     83             manager_method.__name__ = method.__name__
     84             manager_method.__doc__ = method.__doc__

TypeError: create() takes 1 positional argument but 4 were given


```

POPRAWKA!!!
In [4]: Math.objects.create(operation="add", arg_a=3, arg_b=4)
```python

TypeError: create() takes 1 positional argument but 2 were given

In [4]: Math.objects.create(operation="add", arg_a=3, arg_b=4)
Out[4]: <Math: Math object (1)>

In [5]: 

```
po tym sprawdzam w bazie czy element został dodany
- maths_math w DB....

----
```python
In [5]: Math.objects.create(operation="add", arg_a=5, arg_b=5)
Out[5]: <Math: Math object (2)>
```
```python
In [6]: Math.objects.create(operation="sub", arg_a=5, arg_b=5)
Out[6]: <Math: Math object (3)>

```
WYSQWIETLANIE W FUNKCJI
 w maths/views.py
```python
from django.http import HttpResponse
from django.shortcuts import render
from maths.models import Math


# Create your views here.

def math_operations(request, operation, arg_a, arg_b):
    result = None
    if operation == "add":
        result = arg_a + arg_b
    elif operation == "sub":
        result = arg_a - arg_b

    return HttpResponse(result)


def math_list(request):
    objects = Math.objects.all()
    out = ""
    for o in objects:
        out += f"{o.operation}:{o.arg_a} {o.arg_b} <br>"

    return HttpResponse(out)

```
w urls.py dodaj
``    path("maths", math_list),``

jak wpisze w przeg;ladarke po uruchomieniu pliku RUN exercise to pojawi mi sie lista danych ktora dodałem do bazy
`http://127.0.0.1:8000/maths`
```python
add:3 4 
add:5 5 
sub:5 5 
add:7 8 
add:7 8 
add:1 9 
```
do maths/views.py dodaj linijke
    `Math.objects.create(operation=operation, a=arg_a, b=arg_b)`
    by mozna było dodawać wartosci na www 
np. http://127.0.0.1:8000/maths/add/2/2

----------
admin.py
```python
from django.contrib import admin

# Register your models here.

class MathAdmin(admin.ModelAdmin):
    pass
```
by z formularza mozna było dodawać operation
```python
from django.contrib import admin
from  maths.models import Math

# Register your models here.

class MathAdmin(admin.ModelAdmin):
    pass

admin.site.register(Math, MathAdmin)
```
run
w przegladarce
http://127.0.0.1:8000/admin/
widoczne MATHS

next:
```python
from django.contrib import admin
from  maths.models import Math

# Register your models here.

class MathAdmin(admin.ModelAdmin):
    list_display = ["operation", "arg_a", "arg_b"]

admin.site.register(Math, MathAdmin)
```

DODANIE pola search w django:
```python
from django.contrib import admin
from  maths.models import Math

# Register your models here.

class MathAdmin(admin.ModelAdmin):
    list_display = ["operation", "arg_a", "arg_b"]
    search_fields = ["operation"]

admin.site.register(Math, MathAdmin)
```
FILTER:
`    list_filter = ["operation"]`

---
MAths/views.py
```python
from django.http import HttpResponse
from django.shortcuts import render
from maths.models import Math

def calculate(operation, arg_a, arg_b):
    result = None
    if operation == "add":
        result = arg_a + arg_b
    elif operation == "sub":
        result = arg_a - arg_b
    return result

# Create your views here.

def math_operations(request, operation, arg_a, arg_b):
    Math.objects.create(operation=operation, a=arg_a, b=arg_b)
    return HttpResponse(calculate(m.operation, m.arg_a, m.arg_b))


def math_list(request):
    objects = Math.objects.all()
    out = ""
    for o in objects:
        out += f"{o.operation}:{o.arg_a} {o.arg_b} <br>"

    return HttpResponse(out)

def math_details(request, id):
    m = Math.objects.get(pk=id)

    out = f"""
    Operacja: {m.operation}<br>
    arg 1: {m.arg_a}<br>
    arg 2: {m.arg_b}<br>
    ----------------<br>
    wynik: {calculate(m.operation, m.arg_a, m.arg_b)}<br>
    """
    return HttpResponse(out)
```
urls.py
``
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main_page),
    path("hello", hello_world),
    path("hello/<name>/<lastname>", hello_personalized),
    path("calc/<a>/<b>", dodaj),
    path("maths", math_list),
    path("maths/<int:id>", math_details),
    path("maths/<operation>/<int:arg_a>/<int:arg_b>", math_operations),
]
``
run
http://127.0.0.1:8000/maths/1

Operacja: add
 arg 1: 3
 arg 2: 4
 ----------------
 wynik: 7
 
 ------------------------------------------------
 TWORZENIE TEMPLATES:
 exercises/maths/templates....
 np. math_list.html jakonowy plik
 wyświetlanie tabeli danych w formacie HTML...
 
 formatowanie htmla
 tworzenie css-ów
 w2school - 
 Bootstrap - 
 
 -----------------------------------------------
 Wymuszenie wyswietlania tablei osobom zalogowanym:
 @login_required
 
 login.html
```html
{% extends "base.html" %}

{% block content %}
    {% if error %}
        <p class="alert alert-danger">{{ error }}</p>
    {% endif %}
    <form method="POST">{% csrf_token %}
        <div class="form-group">
            <label for="exampleInputEmail1">User name</label>
            <input class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
                   placeholder="User name" name="username">
        </div>
        <div class="form-group">
            <label for="exampleInputPassword1">Password</label>
            <input type="password" class="form-control" placeholder="Password" name="password">
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
    </form>
{% endblock %}
```
 
 -------------------------------
 rozszerzenie pliku urls.py -gdy cos sie nowego pojawi to automatycznie zostanie dodane
 ```python
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'))
]
```