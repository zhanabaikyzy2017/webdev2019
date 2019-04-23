from api.models import Task,TaskList
from api.serializers import TaskListSerializer,TaskSerializer,UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
class TaskLists(generics.ListCreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer



class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer