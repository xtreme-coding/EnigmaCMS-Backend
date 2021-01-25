from django.urls import path
from . import views

urlpatterns = [
    # path('',views.user,name="user"),
    path('', views.register, name='users-register'),
    path('login/', views.login, name='users-login'),
]
