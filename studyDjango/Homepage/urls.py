from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='Homepage'),
    path('login',views.userLogin, name="Login"),
    path('about', views.about, name="About"),
    path('userLogged', views.userLoggedIn),
    path('logout',views.userLogout, name="Logout"),
]