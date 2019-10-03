from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from apps.blog.views import blog_post_detail_page


def home(request):
    context = {
        'title': 'LlauSys'
    }
    return render(request, 'index.html', context)


def services(request):
    context = {
        'title': 'Services'
    }
    return render(request, 'services.html', context)


def projects(request):
    return render(request, 'projects.html', {'title': 'LlauSys | Projects'})


def techs(request):
    template_obj = get_template('techs.html')
    context = {
        'title': 'LlauSys | Technologies'
    }
    render_item = template_obj.render(context)
    return HttpResponse(render_item)


def contact(request):
    return render(request, 'contact.html', {'title': 'LlauSys | Contact'})
