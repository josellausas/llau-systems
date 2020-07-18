from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

import slack

from .forms import UserLoginForm, UserRegisterForm


def signup_view(request):
    # Notify via Slack
    if request.POST:
        honey_name = request.POST.get('name', False)
        honey_email = request.POST.get('email3', False)
        if honey_name or honey_email:
            # Its a trap! Log bot spam attempt!
            # client = slack.WebClient(token=settings.SLACK_TOKEN)
            # client.chat_postMessage(
            #     channel='#llau-systems',
            #     text=f"Spam attempt: {honey_name} - {honey_email}"
            # )
            return redirect("/")
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        print("Saved user")
        client = slack.WebClient(token=settings.SLACK_TOKEN)
        client.chat_postMessage(
            channel='#llau-systems',
            text=f"New User: {user.username} - {user.email}"
        )
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/profile")
    context = {
        "title": "Sign Up",
        "form": form
    }
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    if request.user.is_authenticated:
        print("redirecting")
        return redirect("/profile")

    if request.POST:
        if request.POST['name'] or request.POST['email3']:
            # Its a trap! TODO: Log bot spam attempt!
            return redirect("/")

    # TODO: Log login view
    form = UserLoginForm(request.POST or None)
    # TODO: Log POST attempt
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # This only checks for valid creds
        user = authenticate(username=username, password=password)
        form = UserLoginForm()
        if user:
            # This logins a user with valid creds
            login(request, user)
            if request.user.is_authenticated:
                return redirect('/dashboard')
            
    else:
        # TODO: Log bad attempt here
        pass

    context = {
        "title": "Log In",
        "subtitle": "Auth yourself",
        "form": form,
    }
    return render(request, 'accounts/form.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def my_profile_view(request):
    context = {
        'title': "Profile"
    }
    return render(request, 'accounts/profile.html', context)
