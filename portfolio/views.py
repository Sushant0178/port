from django.http import HttpResponse
from django.shortcuts import render
import os

from portfolio import settings


def home(request):
    # return HttpResponse("this is home page ")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("this is about page ")
    return render(request,'about.html')
        
def contact(request):
    return HttpResponse("this is contact page ")


def audio(request):
    return render(request, '#')



