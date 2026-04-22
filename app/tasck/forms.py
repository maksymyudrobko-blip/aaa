from django import forms
from .models import Board, Task, TaskComment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'is_public']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ['text']