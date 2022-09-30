from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='admission-home'),
    path('register/', views.register, name='admission-register'),
    path('login/', auth_views.LoginView.as_view(template_name='admission_app/login.html'), name='admission-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='admission_app/logout.html'), name='admission-logout'),
    path('profile/', views.profile, name='admission-profile'),
    path('application/', views.application, name='admission-application'),
]