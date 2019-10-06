from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegisterForm


def signup_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("profile")
    context = {
        "title": "Sign Up",
        "form": form
    }
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    if request.user.is_authenticated:
        print("redirecting")
        return redirect("/profile")

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
                return redirect('dashboard')
            
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
