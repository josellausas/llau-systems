from django.shortcuts import render, get_object_or_404

from .models import BlogPost


def blog_home(request):
    object_list = BlogPost.objects.all()
    context = {
        'title': "Blog | LlauSys",
        'object_list': object_list,
        'count': object_list.count()
    }
    return render(request, "blog/index.html", context)


def blog_post_detail(request, slug):
    context = {
        'title': 'Blog | LlauSys',
        'obj': get_object_or_404(BlogPost, slug=slug)
    }
    return render(request, "blog/post_detail.html", context)
