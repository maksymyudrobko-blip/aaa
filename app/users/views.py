from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomRegistrationForm
def login_view(request):
    if request.method == 'POST':
        # Важливо передавати request.POST в параметр data
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

def register_view(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Автоматично логінимо після реєстрації
            return redirect('/') # Перенаправляємо на головну
    else:
        form = CustomRegistrationForm()

    return render(request, 'users/register.html', {'form': form})