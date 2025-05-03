from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        content = {'message':'You are not yet authorized to login on this website'}
        return render(request, 'login.html', content)

def about(request):
    return render(request, 'about.html')
