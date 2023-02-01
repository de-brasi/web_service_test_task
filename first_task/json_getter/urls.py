from django.urls import path

from . import views

urlpatterns = [
    path('', views.example_core_page, name='start_page'),
    path('getparamval/', views.example_getter, name='example_getter'),
]
