from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def feed(request):
    # return render(request, 'homepage/feed.html')
    return redirect(reverse('publications:publication_list'))
