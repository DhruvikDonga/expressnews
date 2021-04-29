from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class Newsapi(models.Model):
    newstitle = models.CharField(max_length=255,unique=True)
    source = models.CharField(max_length=255)
    content = models.TextField(max_length=400)
    url = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    favourite = models.ManyToManyField(User, related_name='news_favourite')


    

