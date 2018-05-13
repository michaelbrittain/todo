from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
import json
from .models import Task


class TaskTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', 'user1@gmail.com', 'user1')
        self.user2 = User.objects.create_user('user2', 'user2@gmail.com', 'user2')
        self.task1 = Task.objects.create(
            name = 'Task1',
            description = 'Desc1',
            status = 0,
            owner=self.user1,
        )
        self.task2 = Task.objects.create(
            name = 'Task2',
            description = 'Desc2',
            status = 0,
            owner=self.user2,
        )
        self.client = Client()
        self.client.login(username='user1', password='user1')

    def tearDown(self):
        self.task1.delete()
        self.task2.delete()
        self.user1.delete()
        self.user2.delete()


    # model tests
    def test_task_creation(self):
        self.assertTrue(isinstance(self.task1, Task))
        self.assertEqual(self.task1.__str__(), self.task1.name)

    def test_task_undone(self):
        self.assertFalse(self.task1.is_done)

    def test_task_set_done(self):
        self.task1.set_done(self.user1)
        self.assertTrue(self.task1.is_done)
        self.assertEqual(self.task1.completed_by, self.user1)


    # view tests
    def test_task_list_view(self):
        url = reverse('task_list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.task1.name, str(resp.content))
        self.assertIn(self.task2.name, str(resp.content))

    def test_task_new_view(self):
        payload = {
            'name': 'Task3',
            'description': 'Desc3',
        }
        url = reverse('task_new')
        resp = self.client.post(url, data=payload)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Task.objects.count(), 3)

    def test_task_edit_view(self):
        task_id = 1
        payload = {
            'name': 'TaskEdit',
            'description': 'DescEdit',
            'status': 0,
        }
        url = reverse('task_edit', kwargs={'pk':task_id})
        resp = self.client.post(url, data=payload)
        self.assertEqual(resp.status_code, 302)
        task = Task.objects.get(pk=task_id)
        self.assertEqual(payload['name'], task.name)

    def test_task_delete_view(self):
        task_id = 1
        url = reverse('task_delete', kwargs={'pk':task_id})
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 302)
        with self.assertRaises(Task.DoesNotExist):
            task = Task.objects.get(pk=task_id)

    def test_task_delete_not_others(self):
        task_id = 2
        url = reverse('task_delete', kwargs={'pk':task_id})
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 403)

    def test_task_done_view(self):
        task_id = 1
        task = Task.objects.get(pk=task_id)
        self.assertFalse(task.is_done)
        url = reverse('task_done', kwargs={'pk':task_id})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        task = Task.objects.get(pk=task_id)
        self.assertTrue(task.is_done)
