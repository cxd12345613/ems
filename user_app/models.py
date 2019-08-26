from django.db import models

# Create your models here.

class User(models.Model):
    user=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='pics',default='aa')
    password=models.CharField(max_length=20)
    sex=models.NullBooleanField()
