from django.shortcuts import render
from .models import *


# Create your views here.

def home_page(request):
    courses = Course.objects.all()[:6]
    return render(request, "home.html", {
        "courses": courses
    })


def contact_page(request):
    return render(request, "contact.html", {})


def about_page(request):
    return render(request, "about.html", {})


def course_page(request):
    selected_cat = request.GET['cat']

    if str(selected_cat).upper() == "ALL":
        courses = Course.objects.all()
    else:
        courses = Course.objects.filter(category__title=selected_cat)

    categories = Category.objects.all()

    data = {
        "categories": categories,
        "courses": courses,

    }
    return render(request, 'courses.html', data)


def learning_page(request, topic_url):
    topic = Topic.objects.get(url=topic_url)

    units = Unit.objects.filter(course=topic.course)
    print(topic)

    data = {
        "topic": topic,
        "course": topic.course,
        "units": units
    }
    return render(request, 'reading.html', data)
