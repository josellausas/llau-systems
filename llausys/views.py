from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm


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
    context = {
        'title': 'LlauSys | Technologies'
    }
    return render(request, 'techs.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        data = form.changed_data
        # TODO: Send slack message
        # TODO: Create its own model
        form = ContactForm()

    context = {
        'title': 'LlauSys | Contact',
        'form': form
    }
    return render(request, 'contact.html', context)
