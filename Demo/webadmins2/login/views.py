from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings

import os
import time

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
