from django.shortcuts import render
from django.http import HttpResponse
import time


# Create your views here.

def login(request):
    return HttpResponse('this is login page!')


def cache(request):
    x = time.time()
    return HttpResponse(x)


def home(request):
    return render(request, 'homePage.html')


def intro(request):
    return render(request, 'projectIntroduce.html')


def cooper(request):
    return render(request, 'cooperation.html')
