from django.shortcuts import render

def login_view(request):
    context = {}
    return render(request, 'accounts/login.html', context)
