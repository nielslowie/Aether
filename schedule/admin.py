from django.contrib import admin

from .models import Teacher, Course, Location, Class, Subject


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class ClassAdmin(admin.ModelAdmin):
    list_display = ('start_date_time', 'end_date_time', 'course', 'teacher', 'activity', 'topic', 'location')


class ClassInline(admin.TabularInline):
    model = Class
    extra = 0


class CourseInline(admin.TabularInline):
    model = Subject.courses.through
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = (ClassInline,)


class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']})
    ]

    inlines = (CourseInline,)

admin.site.register(Location)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
