from rest_framework import serializers
from application import models
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = [
            'id', 'subject', 'active'
        ]