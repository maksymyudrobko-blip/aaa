from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва дошки")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Власник")
    is_public = models.BooleanField(default=False, verbose_name="Публічна")

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'До виконання'),
        ('in_progress', 'В процесі'),
        ('done', 'Виконано'),
    )
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200, verbose_name="Назва завдання")
    description = models.TextField(blank=True, verbose_name="Опис")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo', verbose_name="Статус")
    image = models.ImageField(upload_to='task_images/', blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return self.title

class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Коментар")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Коментар від {self.author.username}"