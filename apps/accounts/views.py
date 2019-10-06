from django.shortcuts import render


def signup_view(request):
    context = {}
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    context = {}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    context = {}
    return render(request, 'accounts/logout.html', context)
