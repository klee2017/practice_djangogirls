from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        'posts':posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request):
    post = Post.objects.first()
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html' context)