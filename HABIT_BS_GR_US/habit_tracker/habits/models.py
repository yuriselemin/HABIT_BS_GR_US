from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _




class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    name = models.CharField(_("Название привычки"), max_length=255)  # Название привычки
    start_date = models.DateField(_("Дата начала"))  # Дата начала
    end_date = models.DateField(_("Дата окончания"))  # Дата окончания

    def __str__(self):
        return self.name  # Метод для строкового представления объекта



class DailyProgress(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='daily_progress')  # Привязка к конкретной привычке
    date = models.DateField(_("Дата записи"))  # Дата записи
    completed = models.BooleanField(_("Выполнено"), default=False)  # Признак выполнения

    class Meta:
        unique_together = ('habit', 'date')  # Уникальность пары (привычка, дата)

    def __str__(self):
        return f"{self.habit.name} - {self.date}"  # Строковое представление объекта