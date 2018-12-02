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