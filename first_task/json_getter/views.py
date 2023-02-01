from django.shortcuts import render
from django.http import HttpResponse


def example_getter(request):
    return HttpResponse("Hello world!")
