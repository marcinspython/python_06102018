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
