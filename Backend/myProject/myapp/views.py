from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('<h1> This is the About Page </h1>')

def funct():
    pass