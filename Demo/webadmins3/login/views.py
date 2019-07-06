from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

import time
import os
import json


# Create your views here.

def login(request):
    print(request.META)
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    request.session["username"] = username
    return HttpResponseRedirect('/index')


def index(request):
    print(request.META)
    username = request.session.get("username", 'err')
    s = ' : %s, <a href="/home"> </a>' % username
    return HttpResponse(s)


def home(request):
    username = request.session.get("username", 'err')
    s = 'this is  %s home page! <a href="/logout">安全退出</a>' % username
    return HttpResponse(s)


def logout(request):
    request.session.clear()
    s = '          !'
    return HttpResponse(s)


def get(request):
    return request.GET.get('a')


def post(request):
    return request.POST.get('a')


def put(request):
    httpPut = QueryDict(request.body)
    a = httpPut.get("a")


def delete(request):
    httpDel = QueryDict(request.body)
    a = httpDel.get("a")


def file_upload(request):
    if request.method == 'POST':
        static_folder = os.path.join(settings.STATIC_ROOT, 'multipart')
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)
        obj = request.FILES.get('files')
        f = open(os.path.join(static_folder, obj.name), 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('OK')


@cache_page(5)
def cache(request):
    x = time.time()
    return HttpResponse(x)


def setCookies(request):
    response = HttpResponse("this is setcookie page")
    response.set_cookie("key", 'value')
    response.set_cookie("foo", "bar")
    return response


def getCookies(request):
    cookies = request.COOKIES
    return HttpResponse(json.dumps(cookies))
