from django.shortcuts import render
from django.http.response import HttpResponse
from FirstApp.models import *
from FirstApp.responseMsg import Msg
from FirstApp.util import *


# Create your views here.
# 登录接口
def login(request):

    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print({"username": username, "password": password})
        users_data_dict = dict()
        users_data = UsersData.objects.values("username", "password")

        for i in users_data:
            users_data_dict[i["username"]] = i["password"]

        if not username or not password:
            return HttpResponse(Util().json_response(Msg().msg["2001"]))

        if username in users_data_dict:

            if password == users_data_dict[username]:
                login_success_msg = Msg().msg['login_200']
                UsersData.objects.filter(username=username).update(user_token=login_success_msg['userToken'])
                # print(login_success_msg['userToken'])
                return HttpResponse(Util().json_response(login_success_msg))

            return HttpResponse(Util().json_response(Msg().msg['2007']))

        return HttpResponse(Util().json_response(Msg().msg["2008"]))

    return render(request, 'login.html')


# 注册接口
def sign_in(request):

    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print({"username": username, "password": password})
        users_data_dict = dict()
        users_data = UsersData.objects.values("username", "password")

        for i in users_data:
            users_data_dict[i["username"]] = i["password"]

        if not username or not password:
            return HttpResponse(Util().json_response(Msg().msg["2001"]))

        if username in users_data_dict:
            return HttpResponse(Util().json_response(Msg().msg["2004"]))

        if len(password) >= 16:
            return HttpResponse(Util().json_response(Msg().msg["2006"]))

        if username not in users_data_dict:
            if len(username) <= 16:

                try:
                    UsersData.objects.create(username=username, password=password)
                    return HttpResponse(Util().json_response(Msg().msg["sign_in_200"]))

                except Exception:
                    return HttpResponse(Util().json_response({"msg": "注册失败"}))

            else:
                return HttpResponse(Util().json_response(Msg().msg["2005"]))

    return render(request, 'sign_in.html')


# 修改密码接口
def change_password(request):

    if request.method == "POST":
        username = request.POST.get("username", None)
        userToken = request.POST.get("userToken", None)
        new_password = request.POST.get("new_password", None)
        print({"username": username, "userToken": userToken, "new_password": new_password})

        if not username or not userToken or not new_password:
            return HttpResponse(HttpResponse(Util().json_response(Msg().msg["2001"])))

        users_data_dict = dict()
        users_data = UsersData.objects.values("username", "user_token")

        for i in users_data:
            users_data_dict[i["username"]] = i["user_token"]

        if username not in users_data_dict:
            return HttpResponse(Util().json_response(Msg().msg["2008"]))

        if userToken == users_data_dict[username]:

            try:
                UsersData.objects.filter(username=username).update(password=new_password)
                return HttpResponse(Util().json_response(Msg().msg["change_password_200"]))

            except Exception:
                return HttpResponse({"msg": "密码修改失败"})

        return HttpResponse(Util().json_response(Msg().msg["2009"]))

    return HttpResponse(Util().json_response(Msg().msg["300"]))


# Tools 接口（未完成）
def tools(request):

    if request.method == "GET":
        return render(request, 'tools.html')
