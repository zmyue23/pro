from fofa.settings import PERMISSION_LIST, MENU_LIST


def init_permission(user, request):
    user_per = user.roles.filter(permissions__isnull=False).values("permissions__url",
                "permissions__title",
                "permissions__id",
                "permissions__is_menu",
                 ).distinct()
    # 获取用户权限中能够成为菜单的url
    menu_list = []
    for item in user_per:
        # 循环判断url是否是菜单
        if item["permissions__is_menu"]:
            temp = {
                "title": item["permissions__title"],
                "id": item["permissions__id"],
                "url": item["permissions__url"]
            }
            menu_list.append(temp)

    # 将用户的权限存入session

    permission_list = [item["permissions__url"] for item in user_per]

    # 将用户的权限列表   菜单列表存入session
    request.session[PERMISSION_LIST] = permission_list
    request.session[MENU_LIST] = menu_list
