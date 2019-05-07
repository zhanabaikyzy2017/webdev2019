from api.models import Task,TaskList
from api.serializers import TaskListSerializer,TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class TaskList_list(APIView):
    def get (self,request):
        taskLists =  TaskList.objects.all()
        serializer = TaskListSerializer(taskLists,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,requst):
        serializer = TaskListSerializer(data=requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskListDetail(APIView):
    def get_object(self,pk):
        try:
            return TaskList.objects.get(id=pk)
        except TaskList.DoesNot.Exist:
            raise Http404

    def get(self,request, pk):
        taskList = self.get_object(pk)
        serializer = TaskListSerializer(taskList)
        return Response(serializer.data)

    def put(self,request,pk):
        taskList = self.get_object(pk)
        serializer = TaskListSerializer(instance=taskList,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,requst,pk):
        taskList = self.get_object(pk)
        taskList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
