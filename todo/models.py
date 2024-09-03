from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default = 1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title