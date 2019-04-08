from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import TaskList

def index (request):
    count = TaskList.objects.count()
    data = {
        'tasklist_count' :count
    }
    return JsonResponse(data,safe=False)


def show_list1(request):
    task_lists = TaskList.objects.all()
    json_tasks = [c.to_json() for c in task_lists]
    data = {
        'task_list': json_tasks

    }
    return JsonResponse(data,safe=False)


def show_list_2(request,pk):
    task = TaskList.objects.get(id=pk)
    json_task = task.to_json()
    data = {
        'task_list': json_task
    }
    return JsonResponse(data,safe=False)


# def show_list_3(request,pk):
#     task = TaskList.objects.get(id = pk)
#     tasks = task.set.all()
#     json_task = [t.to_json() for t in tasks]
#     data = {
#         'task_list': json_task
#     }
#     return JsonResponse(data,safe=False)