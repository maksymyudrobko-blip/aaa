from django.contrib import admin
from .models import Board, Task, TaskComment

admin.site.register(Board)
admin.site.register(Task)
admin.site.register(TaskComment)
