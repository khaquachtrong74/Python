from django.db import models


class Task(models.Model):
    description_task = models.TextField(blank=True)
    time_start = models.DateTimeField(auto_now_add=True) # auto_now_add const | auto_now for update value
    
    def __str__(self):
        return self.description_task

