from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from django.views.decorators.cache import cache_page

import os
import time
import json, random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(os.path.join(BASE_DIR, 'static'), 'upload')


def upload(request):
    if request.method == "POST":
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        obj = request.FILES.get("files")
        print(obj)
        f = open(os.path.join(UPLOAD_FOLDER, obj.name), 'wb')
        for c in obj.chunks():
            f.write(c)
        f.close()
        return HttpResponse("file: %s upload success!" % obj.name)


@cache_page(2)
def cache(request):
    x = time.time()
    return HttpResponse(x)


class AddClass(View):
    def get(self, request):
        return HttpResponse('this is add class get method')

    def put(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass


def setCookies(request):
    response = HttpResponse("this is setCookie page")
    response.set_cookie("key", 'value')
    response.set_cookie("foo", "bar")
    return response


def getCookies(request):
    cookies = request.COOKIES
    return HttpResponse(json.dumps(cookies))


def set_session(request):
    request.session["foo"] = "bar"
    request.session["key"] = "value"
    return HttpResponse("session set  success")


def get_session(request):
    x = request.session.get("foo")
    y = request.session.get('key')
    z = request.session.get("haha", 'err')
    print(x, y, z)


def login(request):
    if request.method == "GET":
        result = {}
        check_num = ''.join(
            [str(j) for j in [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]])
        request.session["check_num"] = check_num
        msg = {"check_num": check_num}
        result["code"] = 200
        result["message"] = msg
        return HttpResponse(json.dumps(result))
    elif request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        check_num = request.POST.get("check_num", '')

        session_check_num = request.session.get("check_num", '')
        print(session_check_num, type(session_check_num))
        print(check_num, type(check_num))
        print(username, type(username))
        print(password, type(password))

        if check_num != session_check_num:
            return HttpResponse("验证码不正确!")
        else:
            if username == "lily" and password == "abc123":
                return HttpResponse("登录成功!")
            else:
                return HttpResponse("未知!")
