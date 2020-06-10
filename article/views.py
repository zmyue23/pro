import json
import os
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin
from article.models import Articles, Pic

@xframe_options_sameorigin
@csrf_exempt
def get_article(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    article = Articles.objects.all().order_by('id')
    all_page = Paginator(article, row_num)
    page = Paginator(article, row_num).page(page_num).object_list

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    for i in page:
        rows.append(i)

    def myDefault(u):
        if isinstance(u, Articles):
            return {'id': u.id,
                    'content': u.content,
                    'title': u.title,
                    'author': u.author,
                    'status': u.status,
                    'createDate': u.create_date.strftime('%Y-%m-%d'),

                    }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)

@xframe_options_sameorigin
@csrf_exempt
def upload_img(request):
    image = request.FILES.get("imgFile")

    if image:
        img_url = request.scheme + "://" + request.get_host() + "/static/img/" + str(image)
        result = {"error": 0, "url": img_url}
        Pic.objects.create(img=image)
    else:
        result = {"error": 500, "url": "图片上传失败"}

    return HttpResponse(json.dumps(result), content_type="application/json")


def get_img(request):
    pic_url = request.scheme + "://" + request.get_host() + "/"
    pic_list = Pic.objects.all()
    rows = []
    for item in list(pic_list):
        path, pic_suffix = os.path.splitext(item.img.url)
        rows.append(
            {"is_dir": False,
             "has_file": False,
             "filesize": item.img.size,
             "dir_path": "",
             "is_photo": True,
             "filetype": pic_suffix,
             "filename": item.img.name,
             "datetime": "2018-06-06 00:36:39"},
        )
    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": pic_url,
        "total_count": len(pic_list),
        "file_list": rows
    }
    return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def add_article(request):
    cate = True if request.POST.get('cate') == 'true' else False
    title = request.POST.get('title')
    content = request.POST.get('content')
    author = request.POST.get('author')
    try:
        Articles.objects.create(title=title, cate=cate, author=author, content=content)
        return JsonResponse({'status': 1, 'msg': '添加成功'})
    except Exception as error:
        print(error)
        return JsonResponse({'status': 0, 'msg': '添加失败'})


@csrf_exempt
def edit(request):
    id = request.POST.get('id')
    cate = True if request.POST.get('cate') == '显密法要' else False
    title = request.POST.get('title')
    content = request.POST.get('content')
    author = request.POST.get('author')
    try:
        art = Articles.objects.get(id=id)
        art.content = content
        art.author = author
        art.title = title
        art.cate = cate
        art.save()
    except:
        return JsonResponse({'status': 0})
    return JsonResponse({'status': 1})


@csrf_exempt
def article_del(request):
    oper = request.POST.get('oper')
    id = request.POST.get('id')
    if oper == 'del':
        Articles.objects.get(id=id).delete()
    return HttpResponse()
