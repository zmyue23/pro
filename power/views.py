from django.http import JsonResponse
from django.shortcuts import render, redirect
from power.models import User
from power.service.init_permission import init_permission


def r_login(request):
    return render(request, "login.html")


def check_user(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username, password=password)
        # 处理权限相关的业务
        init_permission(user, request)
        return redirect("/index/index/")

    except BaseException as error:
        return JsonResponse({ 'msg': f'用户名或密码错误{error}'})
