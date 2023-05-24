from django.shortcuts import render, redirect
from .models import User
from apps.settings.models import Setting
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
# Create your views here.

def signup(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting': setting,
    }
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
            return redirect('user_login')
    return render(request, 'pages/signup.html', context)

def user_login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        except:
            return HttpResponse("Пользователь не найден или пароль не верный")
    context = {
        'setting': setting,
    }
    return render(request, 'pages/login.html', context)