from django.shortcuts import render

# Create your views here.
"""
VIEW
 the view is the function in Python.It has two requirement.
 1. the first augment is the route of request
 2. return HttpResponse
"""
from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    return HttpResponse('ok')