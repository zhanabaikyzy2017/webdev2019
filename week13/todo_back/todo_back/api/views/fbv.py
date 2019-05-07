from api.models import Task,TaskList
from api.serializers import TaskListSerializer,TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET','POST'])
def show_task_lists(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET','PUT','DELETE'])
def show_task_lists_id(request,pk):
    try:
        taskList = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = TaskListSerializer(taskList)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer(instance=taskList,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=='DELETE':
        taskList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def show_task_of_task_list(request, pk):
    try:
        task_lists = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    tasks = task_lists.task_set.all()
    serializer = TaskSerializer(tasks,many=True)

    return Response(serializer.data,status=status.HTTP_200_OK)
