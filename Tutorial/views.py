from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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


# uploading image
@csrf_exempt
def upload_image(request):
    print("testing")
    if request.method == 'POST':
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        print(file.name)
        print(uploaded_file_url)
        res = {'location': '' +
                           str(uploaded_file_url)}
        return JsonResponse(res)
    else:
        return HttpResponse("error")

#deleting image
@csrf_exempt
def delete_image(request):
    if request.method == 'POST':
        url = request.POST['url']
        if url.find('?') != -1:
            name = url[url.rindex('/') + 1: url.index('?'):]
        else:
            name = url[url.rindex('/') + 1::]
        import os
        full_path = os.path.join(settings.MEDIA_ROOT, name)
        os.remove(full_path)
        return JsonResponse({'msg': 'done'})
    return JsonResponse({"msg": "error"})
