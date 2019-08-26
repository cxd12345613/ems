from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    salary=models.FloatField()
    age=models.SmallIntegerField(default=1)
    #将文件存于MEDIA_ROOT目录下的pics目录下
    headpic = models.ImageField(upload_to="pics",default='a')
