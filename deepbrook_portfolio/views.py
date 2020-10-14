from django.db import IntegrityError
from django.shortcuts import render
from deepbrook_portfolio.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User

def index(request):
    return render(request, "deepbrook_portfolio/index.html")

def about(request):
    return render(request, "deepbrook_portfolio/about.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, "deepbrook_portfolio/index.html")
        else:
            return render(request, "deepbrook_portfolio/login.html", {
                "message": "Invalid login credentials. Try again:"
            })
    else:
        return render(request, "deepbrook_portfolio/login.html", {
            "message": "Log In"
        })

def logout_view(request):
    logout(request)
    return render(request, "deepbrook_portfolio/loggedout.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "deepbrook_portfolio/register.html", {
                "message": "Passwords do not match"
            })

        try:
            email = None
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "deepbrook_portfolio/register.html", {
                "message": "Username unavailable"
            })
        login(request, user)
        return render(request, "deepbrook_portfolio/index.html")
    else:
        return render(request, "deepbrook_portfolio/register.html")


@login_required
def portfolio(request):
    return render(request, "deepbrook_portfolio/portfolio.html")

@login_required
def quote(request):
    return render(request, "deepbrook_portfolio/quote.html")

@login_required
def buy(request):
    return render(request, "deepbrook_portfolio/buy.html")

@login_required
def sell(request):
    return render(request, "deepbrook_portfolio/sell.html")

@login_required
def history(request):
    return render(request, "deepbrook_portfolio/history.html")
