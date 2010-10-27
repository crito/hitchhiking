from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.views.generic import list_detail

def post_detail(request, slug):
    '''Display one post.'''
    posts = Post.objects.all()

    return list_detail.object_detail(request, queryset=post, template_name='blog/post_detail.html', slug=slug)
