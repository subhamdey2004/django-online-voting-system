from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2 and username:
            User.objects.create_user(username=username, password=password1)
            return redirect('login')
        return render(request, "register.html")
    from django.contrib import messages
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("USERNAME:", username)
        print("PASSWORD:", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("LOGIN SUCCESS")
            return redirect('vote')   
        else:
            print("LOGIN FAILED")
            return render(request, "login.html")
def logout_view(request):
    logout(request)
    return redirect('home')

from django.contrib.auth.decorators import login_required
@login_required
def vote_view(request):
    return render(request, "vote.html")
