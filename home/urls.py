from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("home", views.index, name="home"),
    path("cart", views.cart, name="cart"),
    path("account", views.account, name="account"),
    path("products", views.products, name="products"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("blog/<title>", views.blog_detail, name="blog_detail"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("sign_up", views.sign_up, name="sign_up"),
]
