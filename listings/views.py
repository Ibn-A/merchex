from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello django ! </h1>')

def about(request):
    return HttpResponse('<h1> A propos </h1> <p>Nous adorons merchex</p>')

def listings(request):
    return HttpResponse('<h1>Liste des annonces</h1>')