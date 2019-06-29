from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    return HttpResponse("this is login page!")


def index(request):
    return HttpResponse("this is login page! ni da ye")


def add(request):
    a = int(request.GET.get('a'))
    b = int(request.GET.get('b'))
    return HttpResponse("a + b = %s" % (a + b))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse("Total is %s" % c)


def get(request):
    return request.GET.get("a")


def post(request):
    return request.POST.get("a")


def put(request):
    httpPut = QueryDict(request.body)
    a = httpPut.get("a")


def delete(request):
    httpDel = QueryDict(request.body)
    a = httpDel.get("a")

