from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from .models import BlogPost
from .forms import BlogPostModelForm


def blog_home(request):
    object_list = BlogPost.objects.filter(is_published=True)
    context = {
        'title': "Blog | LlauSys",
        'object_list': object_list,
        'count': object_list.count()
    }
    return render(request, "blog/index.html", context)


def blog_post_detail(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    obj.view_count = obj.view_count + 1
    obj.save()
    context = {
        'title': 'Blog | LlauSys',
        'obj': obj
    }
    return render(request, "blog/post_detail.html", context)


def blog_post_create(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.slug = slugify(post.title)
        post.created_by = request.user
        post.save()
        form = BlogPostModelForm()
    context = {
        'form': form,
        'title': "Create Post"
    }
    return render(request, 'blog/post_create.html', context)


def blog_post_update(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    # TODO: Make changes to object here
    context = {
        'title': obj.title,
        'obj': obj
    }
    return render(request, 'blog/post_update.html', context)


def blog_post_remove(request, slug):
    return render(request, "blog/index.html", {})
