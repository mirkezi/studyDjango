from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='Homepage'),
    path('login',views.login, name="Login"),
    path('about', views.about, name="About"),
]