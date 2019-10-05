from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.http import HttpResponseNotFound

from .models import BlogPost
from .forms import BlogPostModelForm


def blog_home(request):
    object_list = BlogPost.objects.filter(is_published=True)
    context = {
        'title': "Blog",
        'subtitle': 'Latest posts',
        'object_list': object_list,
        'count': object_list.count()
    }
    return render(request, "blog/index.html", context)


def blog_post_detail(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    is_owner = (obj.author == request.user)

    if obj.is_published or is_owner:
        if not is_owner:
            obj.view_count = obj.view_count + 1
        obj.save()
        context = {
            'title': 'Blog | LlauSys',
            'obj': obj
        }
        return render(request, "blog/post_detail.html", context)
    return HttpResponseNotFound("Not Found")


@login_required
def blog_post_create(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.slug = slugify(post.title)
        post.author = request.user
        post.save()
        form = BlogPostModelForm()
        link = "/blog/" + post.slug
        return redirect(link)
    context = {
        'form': form,
        'title': "Create Post"
    }
    return render(request, 'blog/post_create.html', context)


@login_required
def blog_post_update(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("/blog/"+obj.slug)

    context = {
        'title': f"Update: {obj.title}",
        'obj': obj,
        'form': form
    }
    return render(request, 'blog/post_create.html', context)


@login_required
def blog_post_remove(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    return render(request, "blog/index.html", {'title': 'LlauSys'})
