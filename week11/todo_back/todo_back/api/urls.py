from django.urls import path
from api import views


urlpatterns = [
    path('count/',views.index),
    path('task_lists/',views.show_list1),
    #path('task_lists/<int:pk>', views.show_list_3),
    path('task_lists/tasks/<int:pk>',views.show_list_2)
]