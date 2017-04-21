# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.contrib.auth.models import User 
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class PublishedManager(models.Manager):
		def get_queryset(self):
			return super(PublishedManager,
					 self).get_queryset()\
						  .filter(Status='published')#PublishedManager blog/models.py:9

class Post(models.Model):
	STATUS_CHOICES=(
		('draft','Draft'),
		('published','Published')
		)

	published = PublishedManager()

	#Post title
	title=models.CharField(max_length=250);

	#slug is intended for used in url slug can be used for the date and slug 
	#for post 
	slug=models.SlugField(max_length=250,unique_for_date='publish')

	#author used to  define many  to  one  relationship post is written by user and user can wrote many post
	author=models.ForeignKey(User,related_name='blog_post')

	#body of post
	body=models.TextField()

	#publish is datetime
	publish=models.DateTimeField(default=timezone.now)

	#created  is indicate for when the post is created date will save automatically as we creating object
	created= models.DateTimeField(auto_now_add=True)

	#updated ia indicate when lat time post is updated
	updated=models.DateTimeField(auto_now=True)

	#show status of post we use choices parameter 
	Status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

	objects = models.Manager() # The default manager.


	def get_absolute_url(self):
		return reverse('blog:post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

	class Meta:
		ordering=('-publish',)

	

	
		

	def __str__(self):
		return self.title

class  comment(models.Model):
		post = models.ForeignKey(Post,related_name='comments')
		name=models.CharField(max_length=80)
		email=models.EmailField()
		body=models.TextField()
		created=models.DateTimeField(auto_now_add=True)
		updated=models.DateTimeField(auto_now=True)
		active=models.BooleanField(default=True)

		class Meta:
			ordering =('created',)
		def __str__(self):
			return 'comment by {} on {}'.format(self.name,self.post)





