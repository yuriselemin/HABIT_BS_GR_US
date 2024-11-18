from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import timedelta, datetime
from .models import Habit, DailyProgress
from .forms import HabitForm, DailyProgressForm


# Функция для страницы приветствия
def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'welcome.html')


# Функция регистрации нового пользователя
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Пароли не совпадают!")
            return redirect('register')

        try:
            User.objects.get(username=username)
            messages.error(request, "Такой пользователь уже существует!")
            return redirect('register')
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, "Вы успешно зарегистрированы!")
            return redirect('home')

    return render(request, 'register.html')


# Представление для добавления новой привычки
@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.start_date = datetime.now().date()
            habit.end_date = habit.start_date + timedelta(days=40)
            habit.save()
            messages.success(request, "Привычка была успешно создана!")
            return redirect('home')
    else:
        form = HabitForm()
    return render(request, 'add_habit.html', {'form': form})


# Функционал для фиксации ежедневного прогресса
@login_required
def daily_progress(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    if request.method == 'POST':
        form = DailyProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.habit = habit
            progress.date = datetime.now().date()
            progress.save()
            messages.success(request, "Прогресс был зафиксирован!")
            return redirect('home')
    else:
        form = DailyProgressForm()
    return render(request, 'daily_progress.html', {'form': form, 'habit': habit})


# Главная страница с перечнем привычек пользователя
@login_required
def home(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'home.html', {'habits': habits})