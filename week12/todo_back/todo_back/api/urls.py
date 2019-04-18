from django.urls import path
from api import views


urlpatterns = [
    #path('count/',views.index),
    path('task_lists/',views.show_task_lists),
    path('task_lists/<int:pk>', views.show_task_lists_id),
    path('task_lists/<int:pk>/tasks/<int:pk2>', views.show_task_of_task_list2),
    path('task_lists/<int:pk>/tasks/',views.show_task_of_task_list),

]