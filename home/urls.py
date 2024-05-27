from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("cart", views.cart, name="cart"),
    path("account", views.account, name="account"),
    path("products", views.products, name="products"),
]
