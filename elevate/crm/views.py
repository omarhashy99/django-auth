from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("this is the home page")


def register(request):
    pass


def my_login(request):
    pass


def dashboard(request):
    pass
