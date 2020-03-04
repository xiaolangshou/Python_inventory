from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.

def login(request):
    return HttpResponse('this is login page!')

def cache(request):
    x = time.time()
    return HttpResponse(x)
