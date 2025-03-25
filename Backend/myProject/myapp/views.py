from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1> HOME PAGE</h1>')


def about(request):
    return HttpResponse('<h1> About </h1>')

def index(request):
    context = {
        'name' : 'Peter',
        'Power' : 'Spider-man'
    }

    return render(request, 'index.html', context)
'''

def counter(request):
    words = request.POST['words']
    num_words = len(words.split())
    return render(request, 'counter.html', {'number_of_words': num_words})
'''
