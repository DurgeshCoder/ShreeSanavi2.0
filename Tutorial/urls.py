from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home', home_page),
    path('', home_page),
    path('contact', contact_page),
    path('about', about_page),
    path('courses', course_page),
    path('learning', learning_page)

]
