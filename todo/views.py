from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import Task


class TaskList(ListView):
    model = Task

    def get_queryset(self):
        queryset = Task.objects.all()
        if self.request.GET.get('status'):
            queryset = queryset.filter(status=self.request.GET.get('status'))
        return queryset


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['name', 'description']
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('task_list')
    fields = ['name', 'description', 'status']
    login_url = '/login/'

    # just to be sure, let's prevent non-owners from delete tasks here
    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.owner != self.request.user:
            raise PermissionDenied
        return super(TaskUpdate, self).dispatch(request, *args, **kwargs)
        

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')
    login_url = '/login/'

    # just to be sure, let's prevent non-owners from delete tasks here
    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.owner != self.request.user:
            raise PermissionDenied
        return super(TaskDelete, self).dispatch(request, *args, **kwargs)


@login_required
def set_task_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.set_done(request.user)
    return redirect('task_list')
