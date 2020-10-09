from django.shortcuts import render
from django.http import HttpResponse
from deepbrook_portfolio.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "deepbrook_portfolio/index.html", {
        "username":"username"
    })

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # user = authenticate(request, username=username, password=password)
        # if user:
            # login(request, user)
            # return HttpResponseRedirect((reverse("index"))
        # else:
            # return render(request, "deepbrook_portfolio/login.html", {
                # "message":"Invalid login credentials"
            # })
    return render(request, "deepbrook_portfolio/login.html")

def register(request):
    return render(request, "deepbrook_portfolio/register.html")

def portfolio(request):
    some_username = "UserDude"
    some_dollar_value = 1000
    cash_amount = 17.09
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

