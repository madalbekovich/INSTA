from django.contrib import admin
from django.urls import path, include
from .views import view, success_page

urlpatterns = [
    path('', view, name='login'),
    path('', success_page, name='success_page'),
]
