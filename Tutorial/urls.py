from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('upload_image/', upload_image),
    path('delete_image/', delete_image),
    path('home', home_page),
    path('', home_page),
    path('contact', contact_page),
    path('about', about_page),
    path('courses', course_page),
    path('<slug:topic_url>', learning_page)

]
