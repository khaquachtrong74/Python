from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='lessons/%Y/%m', null=True)
    course = models.ForeignKey(Course, on_delete=models.RESTRICT)
    active = models.BooleanField(default=True)

