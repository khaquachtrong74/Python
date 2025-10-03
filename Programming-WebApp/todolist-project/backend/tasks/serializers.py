from rest_framework import serializers
from .models import Task

class TaskListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'description_task',
            "time_start",
        ]
# Detail
class TaskListDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task 
        fields = [
            'id',
            'description_task',
            'time_start',
        ]