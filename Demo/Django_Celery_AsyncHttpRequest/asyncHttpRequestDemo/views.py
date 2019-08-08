from django.shortcuts import render

# Create your views here.
from __future__ import unicode_literals
from asyncHttpRequestDemo.task import f1
from django.http import HttpResponse


def celery_index(request):
    r = f1.delay()
    print(r)
    return HttpResponse('this is index page!')

