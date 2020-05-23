from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.conf import settings

import slack

from .forms import ContactForm, EmailLeadForm

def soon_view(request):
    # Notify via Slack
    if request.POST:
        honey_name = request.POST.get('name', False)
        if honey_name:
            # Its a trap! Log bot spam attempt!
            client = slack.WebClient(token=settings.SLACK_TOKEN)
            client.chat_postMessage(
                channel='#llau-systems',
                text=f"[Spam]: {honey_name}"
            )
            return redirect("/")
    form = EmailLeadForm(request.POST or None, auto_id=False)
    if form.is_valid():
        lead = form.save(commit=False)
        lead.topic = "home/notify/release"
        lead.save()
        client = slack.WebClient(token=settings.SLACK_TOKEN)
        client.chat_postMessage(
            channel='#llau-systems',
            text=f"New Lead: [{lead.topic}]: {lead.email}"
        )
        return redirect("/thanks")
    context = {
        'title': 'LlauSys',
        'subtitle': 'Professional Services',
        "form": form
    }
    return render(request, "soon.html", context)


def home(request):
    context = {
        'title': 'LlauSys',
        'subtitle': 'Professional Services'
    }
    # return render(request, 'main.html', context)
    # return render(request, "soon.html", context)
    return render(request, 'skin/index.html', context)
    


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

def notify_confirm(request):
    context = {
        'title': 'Thanks!',
        'subtitle': 'You are now receiving updates!',
    }
    return render(request, 'thanks.html',context=context)

