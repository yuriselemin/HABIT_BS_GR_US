from django import forms
from .models import Habit, DailyProgress

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