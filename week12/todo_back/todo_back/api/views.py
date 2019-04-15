from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import TaskList

def index (request):
    count = TaskList.objects.count()
    data = {
        'tasklist_count' :count
    }
    return JsonResponse(data,safe=False)


def show_task_lists(request):
    task_lists = TaskList.objects.all()
    json_tasks = [c.to_json() for c in task_lists]
    data = {
        'task_list': json_tasks

    }
    return JsonResponse(data,safe=False)


def show_task_lists_id(request,pk):
    task = TaskList.objects.get(id=pk)
    json_task = task.to_json()
    data = {
        'task_list': json_task
    }
    return JsonResponse(data,safe=False)


def show_task_of_task_list(request, pk):
    try:
        t_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    tasks = t_list.task_set.all()
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks, safe=False)