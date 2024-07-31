from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to our HomePage!!")

def about(request):
    return HttpResponse("Welcome to about page!!")
# Create your views here.
