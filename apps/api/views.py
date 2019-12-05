from django.shortcuts import render

from .models import MobileApp

def api_home(request):
    context = {
        'title': "API",
        'subtitle': 'Hello Systems!',
    }
    return render(request, "api/index.html", context)

def api_test(request):
    obj, created = MobileApp.objects.get_or_create(
        name="Test", slug="test",
    )
    if request.method == "POST":
        print (request)
        obj.view_count = obj.view_count + 1
        obj.save()
    context = {
        'title': "API TEST",
        'subtitle': 'Test here',
        'count': obj.view_count
    }

    return render(request, "api/test.html", context)

