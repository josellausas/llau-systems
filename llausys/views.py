from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.conf import settings

from .forms import ContactForm


def home(request):
    context = {
        'title': 'LlauSys',
        'subtitle': 'Professional Services'
    }
    return render(request, 'main.html', context)


def services(request):
    context = {
        'title': 'Services',
        'subtitle': 'Our services'
    }
    return render(request, 'services.html', context)


def projects(request):
    context = {'title': 'Our Projects', 'subtitle': 'Check out our work'}
    return render(request, 'projects.html', context)


def techs(request):
    context = {
        'title': 'Technologies',
        'subtitle': 'We work with the latest tools'
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
        'title': 'Contact',
        'subtitle': 'Leave us a message!',
        'form': form
    }
    return render(request, 'contact.html', context)


def acme_challenge(request):
    return HttpResponse(settings.WELL_KNOWN_KEY)
