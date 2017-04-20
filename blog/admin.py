# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish','Status')
admin.site.register(Post, PostAdmin)
	#blog/models.py:15,blog/admin.py:7