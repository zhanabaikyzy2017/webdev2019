from django.urls import path
from api import views
from api.views.old_w12 import show_task_of_task_list,show_task_of_task_list2


urlpatterns = [
    #path('count/',views.index),
    path('task_lists/',views.TaskLists.as_view()),
    path('task_lists/<int:pk>', views.TaskListDetail.as_view()),
    path('task_lists/<int:pk>/tasks/<int:pk2>', show_task_of_task_list2),
    path('task_lists/<int:pk>/tasks/',show_task_of_task_list),
    path('users/',views.UserList.as_view()),
]