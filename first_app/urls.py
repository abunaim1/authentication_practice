from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('set_pass_old/', views.pass_change, name='password'),
    path('set_pass/', views.pass_change2, name='password2'),
]
