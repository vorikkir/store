from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # # Обработчики действий со статьями.
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
]