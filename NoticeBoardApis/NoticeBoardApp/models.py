from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.




class News(models.Model):

    NoticeName = models.CharField(max_length=200)
    SendTo = models.CharField(default="+255746244743", max_length=14,blank=True,null=True)
    NoticeDescription = models.TextField(max_length=10000,blank=True,null=True)

    NoticeImage = models.ImageField(upload_to='media/NewsImage/',blank=True,null=True)
    NoticeDate = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
    	verbose_name_plural = "News"

    def __str__(self):
    	return self.NoticeName


