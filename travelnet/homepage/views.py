from django.http import HttpResponse
from django.shortcuts import render


def feed(request):
    return HttpResponse('feed')
