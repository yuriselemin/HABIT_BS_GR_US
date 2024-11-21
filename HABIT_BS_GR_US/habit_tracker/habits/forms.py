from django import forms
from .models import Habit, DailyProgress, Users


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name']


# Форма для добавления новой привычки
class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name']  # Поле названия привычки


# Форма для фиксации прогресса
class DailyProgressForm(forms.ModelForm):
    class Meta:
        model = DailyProgress
        fields = ['completed']  # Поле выполнения