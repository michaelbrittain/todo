from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('new', views.TaskCreate.as_view(), name='task_new'),
    path('edit/<int:pk>/', views.TaskUpdate.as_view(), name='task_edit'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='task_delete'),
    path('done/<int:pk>/', views.set_task_done, name='task_done'),
]

