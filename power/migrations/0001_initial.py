# Generated by Django 2.0.6 on 2020-06-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='权限标题')),
                ('url', models.CharField(max_length=128, verbose_name='权限url')),
                ('is_menu', models.BooleanField(default=False, verbose_name='是否可以成为菜单')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='角色名称')),
                ('permissions', models.ManyToManyField(blank=True, to='power.Permission', verbose_name='角色对应的权限')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('roles', models.ManyToManyField(blank=True, to='power.Role', verbose_name='用户对应的角色')),
            ],
        ),
    ]
