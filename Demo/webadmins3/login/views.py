from django.shortcuts import render
import random, json
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def logout(request):
    if request.method == "GET":
        result = {}
        username = request.session.get("username", '')
        request.session.clear()
        result["code"] = 200
        result["message"] = '%s already safety logout!' % username
        return HttpResponse(json.dumps(result))


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
        result = {}
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
                request.session["username"] = username
                result["code"] = 200
                result["message"] = "%s登录成功!" % username
                return HttpResponse(json.dumps(result))
            else:
                return HttpResponse("未知!")


def get_user(request):
    if request.method == "GET":
        result = {}
        username = request.session.get("username", 'unknown')
        result["code"] = 200
        result["message"] = {"username": username}
        return HttpResponse(json.dumps(result))

# Create your views here.
