from django.contrib import admin
from .models import *

# Register your models here.



class NewsAdmin(admin.ModelAdmin):

	list_display = ["NoticeName", "NoticeDate","SendTo"]
	list_filter =["NoticeDate","Updated"]
	search_fields = ["NoticeName"]



admin.site.register(News, NewsAdmin)
