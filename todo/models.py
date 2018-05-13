from django.db import models
from django.urls import reverse
import datetime 

STATUS_CHOICES = ( 
    (0, 'undone'), 
    (1, 'done'), 
)


class Task(models.Model): 
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=25) 
    description = models.CharField(max_length=250) 
    status = models.IntegerField(choices=STATUS_CHOICES, default=0) 
    created = models.DateTimeField(default=datetime.datetime.now) 
    completed = models.DateTimeField(blank=True, null=True) 
    completed_by = models.ForeignKey('auth.User', related_name='completed_tasks', on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('task_edit', kwargs={'pk': self.pk})

    @property
    def is_done(self):
        return self.status == 1

    def set_done(self, by_user):
        if not self.status:
            self.status = 1
            self.completed = datetime.datetime.now()
            self.completed_by = by_user
            self.save()

    def __str__(self): 
        return self.name 

    class Meta: 
        ordering = ['-status', 'name'] 

    class Admin: 
        pass
