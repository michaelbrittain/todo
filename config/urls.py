from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from todo.views import TaskList

urlpatterns = [
    path('', include('todo.urls'), name='todo'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('admin/', admin.site.urls),
]

