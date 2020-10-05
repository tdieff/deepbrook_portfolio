from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    some_username = "UserDude"
    some_dollar_value = 1000
    cash_amount = 17.09
    return render(request, "deepbrook_portfolio/index.html", {
        "username": some_username,
        "portfolio_value": some_dollar_value,
        "cash": cash_amount,
        "total_assets": some_dollar_value + cash_amount
    })
