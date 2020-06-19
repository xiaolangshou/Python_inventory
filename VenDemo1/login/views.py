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

def about(request):
    return render(request, 'about.html')


def miniProgrammer(request):
    return render(request, 'miniProgrammer.html')


def companyActive(request):
    return render(request, 'companyActive.html')


def tradesActive(request):
    return render(request, 'tradesActive.html')


def developmentActive(request):
    return render(request, 'developmentActive.html')


def e_commerce(request):
    return render(request, 'e-commerce.html')


def website(request):
    return render(request, 'website.html')


def wchat(request):
    return render(request, 'wchat.html')


def business(request):
    return render(request, 'business.html')
