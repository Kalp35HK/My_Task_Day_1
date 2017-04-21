# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post,comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
	list_display=('name','email','post','created','active')
	list_filter=('active','created','updated')
	search_filters=('name','email','body')
admin.site.register(comment,CommentAdmin)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish','Status')
admin.site.register(Post, PostAdmin)
	#blog/models.py:15,blog/admin.py:7

