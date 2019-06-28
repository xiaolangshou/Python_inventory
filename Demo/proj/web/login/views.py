from django.shortcuts import render
from django.http import HttpResponse

def login(request):
	return HttpResponse("this is login page!")

# Create your views here.
