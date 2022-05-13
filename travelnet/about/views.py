from django.http import HttpResponse
from django.shortcuts import render


def description(request):
    return HttpResponse('thats it')


def faq(request):
    return HttpResponse('fuck')
