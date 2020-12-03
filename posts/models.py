from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    short_description = models.CharField(max_length=256,null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)

    __str__ = lambda self:self.title
