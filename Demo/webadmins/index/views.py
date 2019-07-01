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
        return HttpResponse("file: %s upload success!"%obj.name)





