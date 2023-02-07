from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class TaskList(generics.ListCreateAPIView):
    """
    List all tasks, or create a new task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a task instance.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
