from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth, messages
from django.urls import reverse

def index(request):
    return render(request, 'login/index.html')

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        "form": form,
        "title": "Авторизация",
    }
    return render(request, 'login/login.html', context)

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserRegistrationForm()
    context = {
        "form": form,
        "title": "Регистрация",
    }
    return render(request, 'login/register.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


# Create your views here.
