from django.shortcuts import render, HttpResponse
from . import package, models
from django.utils import timezone


# Create your views here.
def index(request):
    blog = models.blog.objects.get(title="blog 1")
    blog.view_count += 1
    blog.save()
    context = {"blog": blog}
    return render(request, "index.html", context)


def cart(request):
    return render(request, "cart.html")


def account(request):
    return render(request, "account.html")


def products(request):
    return render(request, "products.html")
