from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', null=True, related_name='tasks', on_delete=models.CASCADE)
    