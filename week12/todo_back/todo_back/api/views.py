from django.http import HttpResponse,JsonResponse
from api.models import TaskList,Task
from api.serializers import TaskListSerializer,TaskSerializer
import json
from django.views.decorators.csrf import csrf_exempt
from api import models


@csrf_exempt
def show_task_lists(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        #print('post request')
        task_lists = json.loads(request.body)
        serializer = TaskListSerializer(data=task_lists)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@csrf_exempt
def show_task_lists_id(request,pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except models.TaskList.DoesNotExist as e:
        return JsonResponse({'error':str(e)},safe=False)
    if request.method == 'GET':
        serializer = TaskListSerializer(task_list)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        #print('It does work')
        serializer = TaskListSerializer(instance=task_list,data=data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({})

@csrf_exempt
def show_task_of_task_list(request, pk):
    try:
        t_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)
    if request.method == 'GET':
        serializer = TaskSerializer(t_list.task_set.all(),many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        t_list = data.pop('task_list')
        taskList = TaskList(t_list['id'],t_list['name'])
        serializer = TaskSerializer(data = data)
        if serializer.is_valid():
            serializer.save(task_list = taskList)
            return JsonResponse(serializer.data,safe = False)
        return JsonResponse(serializer.errors)
    elif request.method == 'PUT':
        data = json.loads(request.body)

