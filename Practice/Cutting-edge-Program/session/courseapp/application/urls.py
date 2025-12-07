from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from rest_framework.routers import DefaultRouter

r = DefaultRouter()
r.register('categories', views.CategoryView, basename='category')
r.register('courses', views.CourseView, basename='course')

urlpatterns = [
    path('', include(r.urls)),
]