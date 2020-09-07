from django.contrib import admin
from django.db import models
from .models import Topic, Course, Student, Order


# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('upper_case_name', 'city')

    def upper_case_name(self, obj):
        return '{} {}'.format(obj.first_name.upper(), obj.last_name.upper())
    upper_case_name.short_description = 'Student Full Name'


def add_50_to_hours(modeladmin, request, queryset):
    for course in queryset:
        course.hours += 10
        course.save()


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'price', 'hours', 'for_everyone')
    actions = [add_50_to_hours]


admin.site.register(Topic)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Order)
