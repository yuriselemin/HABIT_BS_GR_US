from django.urls import path
from .views import register_user, add_habit, daily_progress, home
from .views import welcome
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', TemplateView.as_view(template_name='welcome.html'), name='home'),
    path('register/', register_user, name='register'),
    path('add-habit/', add_habit, name='add_habit'),
    path('daily-progress/<int:habit_id>/', daily_progress, name='daily_progress'),
    path('home/', home, name='home'),
    path('', welcome, name='welcome'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
