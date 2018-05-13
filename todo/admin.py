from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'created', 'status')
    

admin.site.register(Task, TaskAdmin)

