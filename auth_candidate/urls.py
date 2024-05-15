from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SignUp, name='signup'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    
]
handler403 = 'auth_candidate.views.permission_denied_view'
