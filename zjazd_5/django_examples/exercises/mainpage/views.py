from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, response


def main_page(request):
    return HttpResponse(content="Main Page")


def hello_world(request):
    return HttpResponse(content="Hello World")


def hello_personalized(request, name, lastname):
    return HttpResponse(content=f"Hello {name} {lastname}")


def dodaj(request, a, b):
    return HttpResponse(content=f"wynik {int(a) + int(b)}")
