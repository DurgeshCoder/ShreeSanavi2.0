from django.shortcuts import render


# Create your views here.

def home_page(request):
    return render(request, "home.html", {})


def contact_page(request):
    return render(request, "contact.html", {})


def about_page(request):
    return render(request, "about.html", {})


def course_page(request):
    return render(request, 'courses.html', {})


def learning_page(request):
    return render(request, 'reading.html', {})
