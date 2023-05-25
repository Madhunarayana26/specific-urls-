from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>hai first string response of app2 views</h1>')
def second(request):
    return HttpResponse('<h1>hai second string response of app2 views</h1>')
