import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.deprecation import MiddlewareMixin
from fofa.settings import PERMISSION_LIST


class CheckPermission(MiddlewareMixin):

    def process_request(self, request):

        current_url = request.path
        per_list = request.session.get(PERMISSION_LIST)
        print(per_list, 369)
        # 设置路径白名单
        valid_url_list = [
            "/power/check_user/",
            "/index/login/",
            "/index/index/",
            "/admin/.*",
            ""
        ]
        # 用户当前要访问的url是否在白名单中  在不拦截

        for url in valid_url_list:
            if re.match(url, current_url):
                return None
        for u in per_list:
            print(55)
            print(current_url)
            if current_url == u:
                return None
        else:
            print(333)
            return HttpResponse("无权访问")
            # if per_list == []:
            #     return redirect('index:login')
