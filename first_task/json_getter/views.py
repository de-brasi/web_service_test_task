from django.shortcuts import render
from django.http import HttpResponse


def example_getter(request):
    return HttpResponse("I'll give some useful json")


def example_core_page(request):
    return HttpResponse("Hello world!")
