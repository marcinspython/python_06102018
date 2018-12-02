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