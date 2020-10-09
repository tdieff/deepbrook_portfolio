from django.urls import path
from . import views

app_name="deepbrook_portfolio"
urlpatterns = [
        path("", views.index, name="index"),
        path("login", views.login, name="login"),
        path("register", views.register, name="register"),
        path("portfolio", views.portfolio, name="portfolio"),
        path("qoute", views.quote, name="quote"),
        path("buy", views.buy, name="buy"),
        path("sell", views.sell, name="sell"),
        path("history", views.history, name="history")
    ]
