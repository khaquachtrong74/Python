from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskListDetailSerializers, TaskListSerializers
from .models import Task


# Create your views here.
class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializers
class TaskRetriveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Task.objects.all()
    serializer_class = TaskListDetailSerializers
class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListDetailSerializers

class TaskRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Task.objects.all()
    serializer_class = TaskListDetailSerializers
class TaskRetriveDestroyAPIView(generics.RetrieveDestroyAPIView):
    lookup_field = "id"
    queryset = Task.objects.all()
    serializer_class = TaskListDetailSerializers
    