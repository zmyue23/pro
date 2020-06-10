from django.db import models

# Create your models here.

class Banner(models.Model):
    desc = models.CharField(max_length=50)
    status = models.IntegerField()
    up_time = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to="img")

