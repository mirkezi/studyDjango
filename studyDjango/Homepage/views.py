from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, logout

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def userLogin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(userLoggedIn)
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def userLoggedIn(request):
    return render(request, 'userLogged.html')

def userLogout(request):
    logout(request)
    return redirect(homepage)