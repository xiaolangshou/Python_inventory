from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(os.path.join(BASE_DIR, 'static'), 'upload')


def get_values(request):
    if request.method == "GET":
        s = open('/tmp/xyz.log').read()
        return HttpResponse(s)


def index(request):
    username = request.session.get('username', 'unknown')
    s = """
    welcome: %s


    <a href="/home/">跳转到你自己的主目录..</a>
    """ % username
    return HttpResponse(s)


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


def set_cookie(request):
    resp = HttpResponse("this is set cookie")
    resp.set_cookie("foo", "bar")
    resp.set_cookie("key", "value")
    return resp


def get_cookie(request):
    print(request.COOKIES)


def set_session(request):
    request.session["foo"] = "bar"
    request.session["key"] = "value"
    return HttpResponse("session set  success")


def get_session(request):
    x = request.session.get("foo")
    y = request.session.get('key')
    z = request.session.get("haha", 'err')
    print(x, y, z)
