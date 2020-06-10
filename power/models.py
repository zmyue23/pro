from django.db import models

# Create your models here.

class Permission(models.Model):
    title = models.CharField(verbose_name="权限标题", max_length=32)
    url = models.CharField(verbose_name="权限url", max_length=128)
    is_menu = models.BooleanField(default=False, verbose_name="是否可以成为菜单")

    def __str__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(verbose_name="角色名称", max_length=32)
    permissions = models.ManyToManyField(to="Permission", verbose_name="角色对应的权限", blank=True)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    roles = models.ManyToManyField(to="Role", verbose_name="用户对应的角色", blank=True)

    def __str__(self):
        return self.username
