from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home', home_page),
    path('', home_page),
    path('contact', contact_page),
]
