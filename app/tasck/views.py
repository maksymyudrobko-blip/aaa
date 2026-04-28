from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Board, Task, TaskComment
from .forms import BoardForm, TaskForm, CommentForm


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tasck/board_list')
    else:
        form = UserCreationForm()
    return render(request, 'tasck/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tasck/board_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tasck/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('tasck/login.html')


@login_required
def board_list_view(request):
    boards = Board.objects.filter(Q(owner=request.user) | Q(is_public=True)).distinct()
    return render(request, 'tasck/board_list.html', {'boards': boards})


@login_required
def board_create_view(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.owner = request.user
            board.save()
            return redirect('tasck/board_list')
    else:
        form = BoardForm()
    return render(request, 'tasck/form_template.html', {'form': form, 'title': 'Створити дошку'})


@login_required
def board_detail_view(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    tasks = board.tasks.all()
    return render(request, 'tasck/board_detail.html', {'board': board, 'tasks': tasks})


@login_required
def task_create_view(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.board = board
            task.save()
            return redirect('tasck/board_detail', board_id=board.id)
    else:
        form = TaskForm()
    return render(request, 'tasck/form_template.html', {'form': form, 'title': 'Нове завдання'})


@login_required
def task_edit_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasck/task_detail.html', task_id=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasck/form_template.html', {'form': form, 'title': 'Редагувати завдання'})


@login_required
def task_detail_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = task.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            return redirect('tasck/task_detail', task_id=task.id)
    else:
        form = CommentForm()
    return render(request, 'tasck/task_detail.html', {'task': task, 'comments': comments, 'form': form})


from django.shortcuts import render

# Create your views here.
