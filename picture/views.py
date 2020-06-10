from django.http import  JsonResponse
# from redis import Redis
from user.models import User
# res = Redis(host='127.0.0.1', port=6379)


def get_map(request):
    provinces = ["北京", "天津", "河北", "山西", "内蒙古", "吉林", "黑龙江", "辽宁", "上海", "江苏", "浙江", "安徽",
                 "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州", "云南", "西藏",
                 "陕西", "甘肃", "青海", "宁夏", "新疆", "香港", "澳门", "台湾"
                 ]
    data = []
    for i in provinces:
        data.append({'name': i, 'value': len(User.objects.filter(address=i))})

    return JsonResponse({'data': data}, safe=False)


def get_data(request):
    use = User.objects.all()
    month1 = 0
    month2 = 0
    month3 = 0
    month4 = 0
    month5 = 0
    month6 = 0
    for i in use:
        r_time = i.register_time
        lists = str(r_time).split('-')
        if lists[1] == '01':
            month1 += 1
        elif lists[1] == '02':
            month2 += 1
        elif lists[1] == '03':
            month3 += 1
        elif lists[1] == '04':
            month4 += 1
        elif lists[1] == '05':
            month5 += 1
        elif lists[1] == '06':
            month6 += 1
    x = ['1月', '2月', '3月', '4月', '5月', '6月']
    y = [month1, month2, month3, month4, month5, month6]
    data = {
        "x": x,
        "y": y
    }
    return JsonResponse({'data': data}, safe=False)