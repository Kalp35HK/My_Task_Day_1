# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import CommentForm



def post_list(request):
	object_list=Post.published.all()
	paginator=Paginator(object_list,3)
	page=request.GET.get('page')
	try:
		posts=paginator.page(page)
	except PageNotAnInteger:
		posts=paginator.page(1)
	except EmptyPage:
		posts=paginator.page(paginator.num_pages)
	return render(request,'blog/post/list.html',{'page':page,'posts':posts})
	
def post_detail(request,year,month,day,post):
	#post = get_object_or_404(Post,slug=post,Status='published',publish_year=year,publish_month=month,publish_day=day)
	post = get_object_or_404(Post, slug=post,Status='published',publish__year=year,publish__month=month,publish__day=day)
	comments=post.comments.filter(active=True)
	if (request.method=='POST'):
		#A comment was posted
		comment_form=CommentForm(data=request.POST)
		#if comment_form is valid create the commnet but dont push in  database
		new_comment=comment_form.save(commit=False)
		#assign the current post to the comment
		new_comment.post=post
		new_comment.save()
		comment_form=CommentForm()
	else:
		comment_form=CommentForm()
	return render(request,'blog/post/detail.html',{'post':post,'comments':comments,'comment_form':comment_form})

class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 3
	template_name = 'blog/post/list.html'
