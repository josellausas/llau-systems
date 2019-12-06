from django.shortcuts import render

def dashboard_home(request):
    context = {
        'title': "Dashboard",
        'subtitle': 'Hello Dashboard',
    }
    return render(request, "dashboard/index.html", context)
