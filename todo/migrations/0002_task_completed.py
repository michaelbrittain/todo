# Generated by Django 2.0.5 on 2018-05-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
