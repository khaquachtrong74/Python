from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe
from .models import Category, Lesson, Course
from django.urls import path

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'content', 'active']
    list_filter = ['id', 'subject']
    readonly_fields = ['image_view']
    search_fields = ['subject']
    @staticmethod
    def image_view(self, course):
        if course.image:
            return mark_safe(f'<img src="/static/{course.image.name}"/>')

    class Media:
        css = {
            'all': ('css/style.css',)
        }

class MyAdminSite(admin.AdminSite):
    site_header = "E app!"
    def get_urls(self):
        return [path('stats-view/', self.get_stats)] + super().get_urls()
    def get_stats(self, request):
        count = Course.objects.filter(active=True).count()
        stats = Course.objects.annotate(lesson_count=Count('lesson')).values('id', 'subject', 'lesson_count')
        return TemplateResponse(request, 'admin/static.html',{
            'course_count': count,
            'course_stats': stats
        })
admin_site = MyAdminSite()
# Register your models here.
admin_site.register(Category)
# admin.site.register(Comment)
# admin.site.register(Tag)
admin_site.register(Lesson)
admin_site.register(Course)
# admin.site.register(Rating)