from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse('<h1>This is my home Page</h1>')

