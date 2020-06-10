import json
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ban.models import Banner


def get_banner(request):
    rows = request.GET.get('rows')
    page = request.GET.get('page')
    pic_list = Banner.objects.all().order_by('id')
    all_page = Paginator(pic_list, rows)
    if int(page) > all_page.num_pages:
        page = all_page.num_pages
    page_obj = Paginator(pic_list, rows).page(page).object_list
    page_data = {
        'page': page,
        'total': all_page.num_pages,
        'records': all_page.count,
        'rows': list(page_obj)
    }

    def myDefault(u):
        if isinstance(u, Banner):
            return {"id": u.id,
                    'desc': u.desc,
                    'date': str(u.up_time.strftime("%Y-%m-%d %H:%M:%S")),
                    'status': '展示' if u.status == 1 else '不展示',
                    'pic': str(u.pic)
                    }

    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)


@csrf_exempt
def add_banner(request):
    title = request.POST.get("title")
    status = request.POST.get('status')
    pic = request.FILES.get('pic')
    try:
        result = Banner.objects.create(desc=title, status=status, pic=pic)
        if result:
            return HttpResponse('success')
    except:
        return HttpResponse('error')


@csrf_exempt
def edit_banner(request):
    option = request.POST.get('oper')
    if option == "edit":
        id = request.POST.get('id')
        desc = request.POST.get('desc')
        status = request.POST.get('status')
        data = Banner.objects.get(id=id)
        data.desc = desc
        data.status = status
        data.save()
        return HttpResponse('success')
    elif option == 'del':
        id = request.POST.get('id')
        data = Banner.objects.get(id=id)
        data.delete()
        return HttpResponse('del成功')