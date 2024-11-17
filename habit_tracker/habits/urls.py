from django.urls import path
from .views import register_user, add_habit, daily_progress, home
from .views import welcome

urlpatterns = [
    path('register/', register_user, name='register'),
    path('add-habit/', add_habit, name='add_habit'),
    path('daily-progress/<int:habit_id>/', daily_progress, name='daily_progress'),
    path('home/', home, name='home'),
    path('', welcome, name='welcome'),  # Новая домашняя страница
]