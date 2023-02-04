from rest_framework import status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics


class TaskList(generics.ListCreateAPIView):
    """
    List all tasks, or create a new task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a task instance.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
