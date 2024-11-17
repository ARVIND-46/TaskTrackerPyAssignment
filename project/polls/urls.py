from django.urls import path
from . import views

urlpatterns =[
    path("addTask/", views.addTask, name="add_task"),
    path("",views.taskList,name='task_list'),
    path("diplayTL/",views.display_tasks,name="displayTL"),
    path('task/',views.display_tasks,name='display_tasks'),
    path('tasks/complete/<int:task_id>/', views.complete_Task, name='complete_task'),
]

