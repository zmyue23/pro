from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=20)
    content = models.TextField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True ,default='2010-01-01')
    cate = models.BooleanField()
    status = models.CharField(max_length=255, blank=True, null=True,default=True)

    class Meta:
        db_table = 'articles'


class Pic(models.Model):
    img = models.ImageField(upload_to="static/img")

    class Meta:
        db_table = "pic"
