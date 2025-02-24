from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health_check, name='health-check'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('update_profile/', views.update_partial_profile, name='update-partial-profile'),
]
