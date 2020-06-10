from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from fofa import settings
from tools.code import num
from tools.send_msg import Message
from django.http import JsonResponse


def index(request):
    return render(request,'index.html')


def photo(request):
    return render(request, '../static/static_html/lbo_list.html')


def login(request):
    return render(request,'login.html')


@csrf_exempt
def code(request):
    mobile = request.POST.get('mobile')
    if mobile:
        code2 = num()
        request.session["m"] = mobile
        request.session["c"] = code2
        msg = Message(settings.API_KEY)
        msg.send_message(mobile=mobile, code=code2)
        return HttpResponse('123')


def check(request):
    mobile = request.POST.get('mobile')
    passw = request.POST.get('passw')
    c = request.session.get('c')
    m = request.session.get('m')
    if mobile == m and passw == c:
        return HttpResponse('1')
    return render(request, 'index.html')

