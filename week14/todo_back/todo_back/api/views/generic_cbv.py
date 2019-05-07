from api.models import Task,TaskList
from api.serializers import TaskListSerializer2,TaskSerializer,UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


class TaskLists(generics.ListCreateAPIView):
    # queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        #print(self.request.user)
        return TaskList.objects.for_user(self.request.user)
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2


class TaskListTasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend)
    filterset_fields = ('name')

    def get_queryset(self):
        try:
            task_list = TaskList.objects.get(id=self.kwargs.get('pk'))
        except TaskList.DoesNotExist:
            raise Http404

        queryset = task_list.tasks.all()

        #TODO Query params
        # name = self.request.query_params.get('name',None)
        # if name is not None:
        #     queryset = queryset.filter(name=name)


        return queryset








