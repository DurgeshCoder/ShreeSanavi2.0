from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)


class CourseAdmin(admin.ModelAdmin):
    list_filter = ("category",)


admin.site.register(Course)


class UnitAdmin(admin.ModelAdmin):
    list_filter = ("course",)


admin.site.register(Unit, UnitAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "isLive")
    search_fields = ("title",)
    list_filter = ("course", "unit")
    list_per_page = 50


admin.site.register(Topic, TopicAdmin)
