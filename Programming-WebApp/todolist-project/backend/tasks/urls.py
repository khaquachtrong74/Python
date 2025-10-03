from django.urls import path
from . import views
urlpatterns = [
    path('todo-list', views.TaskListAPIView.as_view(),
    name='tasks_view'),
    path('todo-list-detail/<int:id>/', views.TaskRetriveAPIView.as_view(),
    name='tasks_view_detail'),
    path('create/', views.TaskCreateAPIView.as_view(),
    name='task_create'),
    path('update/<int:id>/', views.TaskRetriveUpdateAPIView.as_view(),
    name='task_update'),
    path('destroy/<int:id>/', views.TaskRetriveDestroyAPIView.as_view(),
    name='task_destroy'),
]