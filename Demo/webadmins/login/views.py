from django.shortcuts import render
import random, json
from django.http import HttpResponse


def login(request):
    if request.method == "GET":
        result = {}
        check_num = ''.join([str(j) for j in [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),random.randint(0, 9)]])
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





# Create your views here.
