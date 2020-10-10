from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from deepbrook_portfolio.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "deepbrook_portfolio/index.html", {
        "username":"username"
    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, "deepbrook_portfolio/index.html")
    return render(request, "deepbrook_portfolio/login.html")

def register(request):
    return render(request, "deepbrook_portfolio/register.html")

def portfolio(request):
    return render(request, "deepbrook_portfolio/portfolio.html", {
        "username": some_username,
        "portfolio_value": some_dollar_value,
        "cash": cash_amount,
        "total_assets": some_dollar_value + cash_amount
    })

def quote(request):
    some_username = "UserDude"
    return render(request, "deepbrook_portfolio/quote.html", {
        "username": some_username,
    })


def buy(request):
    some_username = "UserDude"
    return render(request, "deepbrook_portfolio/buy.html", {
        "username": some_username,
    })


def sell(request):
    some_username = "UserDude"
    return render(request, "deepbrook_portfolio/sell.html", {
        "username": some_username,
    })

def history(request):
    some_username = "UserDude"
    return render(request, "deepbrook_portfolio/history.html", {
        "username": some_username,
    })

