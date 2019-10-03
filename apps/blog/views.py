from django.shortcuts import render

from .models import BlogPost


def blog_home(request):
    context = {
        'title': "Blog | LlauSys",
        'count': BlogPost.objects.all().count()
    }
    return render(request, "blog/index.html", context)


def blog_post_detail_page(request, slug):
    post = BlogPost.objects.get(slug=slug)
    context = {
        'title': 'Blog | LlauSys',
        'obj': post
    }
    return render(request, "blog/post_detail.html", context)
