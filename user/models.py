from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    status = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    register_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'