import json
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from user.models import User


def get_user(request):
    rows = request.GET.get('rows')
    page = request.GET.get('page')
    user_list = User.objects.all().order_by('id')
    all_page = Paginator(user_list, rows)

    if int(page) > all_page.num_pages:
        page = all_page.num_pages

    page_obj = Paginator(user_list, rows).page(page).object_list
    page_data = {
        'page': page,
        'total': all_page.num_pages,
        'records': all_page.count,
        'rows': list(page_obj)
    }

    def myDefault(u):
        if isinstance(u, User):
            return {"id": u.id,
                    'username': u.username,
                    'nickname': u.nickname,
                    'address': u.address,
                    'status': '不禁用' if u.status == 1 else '禁用',
                    'register_time': u.register_time.strftime("%Y-%m-%d %H:%M:%S"),
                    }

    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)


@csrf_exempt
def add_user(request):
    username = request.POST.get("username")
    nickname = request.POST.get('nickname')
    address = request.POST.get('address')
    status = request.POST.get('status')
    gender = request.POST.get('gender')
    print(status, username, nickname, address, gender)
    try:
        result = User.objects.create(username=username,
                                      nickname=nickname,
                                      address=address,
                                      status=int(status),
                                      gender=gender,
                                    )
        if result:
            return HttpResponse('添加成功！')
    except BaseException as error:
        print(error)
        return HttpResponse('添加失败！')


@csrf_exempt
def edit_user(request):
    method = request.POST.get("oper")
    print(method)
    if method == 'edit':
        id = request.POST.get('id')
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        address = request.POST.get('address')
        status = request.POST.get('status')
        print(id, username, nickname, address, status)
        user = User.objects.get(id=id)
        user.username = username
        user.nickname = nickname
        user.address = address
        user.status = status
        user.save()
        return HttpResponse('修改成功')

    elif method == 'del':
        id = request.POST.get('id')
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponse('删除成功')



