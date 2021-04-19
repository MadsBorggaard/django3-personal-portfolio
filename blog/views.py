from django.shortcuts import render, get_object_or_404
from .models import Blogs


def all_blogs(request):
    blogs = Blogs.objects.order_by('-createdate')[:5]
    count = Blogs.objects.count()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'count': count})


def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
