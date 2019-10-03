from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


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


def about(request):
    return render(request, 'about.html', {'title': 'LlauSys | About'})


def projects(request):
    return render(request, 'projects.html', {'title': 'LlauSys | Projects'})


def techs(request):
    return render(request, 'techs.html', {'title': 'LlauSys | Technologies'})


def blog(request):
    template_obj = get_template('blog.html')
    context = {
        'title': 'LlauSys | Blog'
    }
    render_item = template_obj.render(context)
    return HttpResponse(render_item)


def contact(request):
    return render(request, 'contact.html', {'title': 'LlauSys | Contact'})
