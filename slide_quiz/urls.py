from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('score/', views.Check_Ans, name='Check_Ans'),
    path('send_email/', views.send_email, name='send_email'),
    path('login_exam', views.Login_Exam, name='login_exam'),
    # path('about/', views.about, name='about'),
    # Add more URL patterns as needed
]
