from rest_framework import viewsets, generics, permissions
from rest_framework.viewsets import ViewSet
from . import models
from . import serializers
class CategoryView(ViewSet, generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseView(ViewSet, generics.ListAPIView):
    queryset = models.Course.objects.filter(active=True)
    serializer_class = serializers.CourseSerializer
