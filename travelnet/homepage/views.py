from django.http import HttpResponse
from django.shortcuts import render


def feed(request):
    return render(request, 'homepage/feed.html')
