from django.shortcuts import render


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
    return render(request, 'blog.html', {'title': 'LlauSys | Blog'})


def contact(request):
    return render(request, 'contact.html', {'title': 'LlauSys | Contact'})
