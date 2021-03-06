# Generated by Django 2.0.5 on 2018-05-13 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
