from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# HTTP RESPONSE

def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Eberton Marinho'})

def sobre(request):
    return HttpResponse('<h1>SOBRE - Django</h1>')

def contato(request):
    return HttpResponse('<h1>CONTATO - Django</h1>')