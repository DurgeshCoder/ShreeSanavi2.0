from django.db import models


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=True)
    description = models.TextField()
    banner = models.ImageField(upload_to="category/banners/")

    def __str__(self):
        return self.title


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.CharField(max_length=500, )
    logo = models.ImageField(upload_to="course/logo/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    url = models.CharField(max_length=500)
    isLive = models.BooleanField(default=False)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="unit")

    page_title = models.TextField(blank=True)
    page_keywords = models.TextField(blank=True)
    page_description = models.TextField(blank=True)
    page_author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
