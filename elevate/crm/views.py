from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm

# Auth functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


@login_required(login_url="my-login")
def homepage(request):
    return render(request, "crm/index.html")


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")

    contxet = {
        "registerform": form,
    }

    return render(request, "crm/register.html", context=contxet)


def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    context = {
        "loginform": form,
    }
    return render(request, "crm/my-login.html", context=context)


@login_required(login_url="my-login")
def dashboard(request):
    return render(request, "crm/dashboard.html")


def user_logout(request):
    auth.logout(request)
    return redirect("")
