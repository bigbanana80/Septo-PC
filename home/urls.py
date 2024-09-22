from django.urls import path , re_path
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
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
    path("sign_in", views.sign_in, name="sign_in"),
    path("sign_out", views.sign_out, name="sign_out"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("forget_password" ,views.forget_password,name="forget_password"),
    path("reset_password_result" ,views.reset_password_result,name="reset_password_result"),
    path('password-reset/', PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
    # re_path(r'^.*$', views.not_available) use this to make the website not available temporary
]
