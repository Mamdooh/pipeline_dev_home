from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    """
    Render the homepage with welcoming content.
    """
    context = {
        'title': 'Welcome to msite',
    }
    return render(request, 'home/home.html', context)


def health(request):
    """
    Health check endpoint.
    """
    return JsonResponse({
        'status': 'ok'
    })
