from django.db import models

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)