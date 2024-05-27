from django.shortcuts import render, HttpResponse
from . import package, models
from django.utils import timezone


# Create your views here.
def index(request):
    return render(request, "index.html")


def cart(request):
    return render(request, "cart.html")


def account(request):
    return render(request, "account.html")


def products(request):
    return render(request, "products.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def blog(request):
    blogs = models.blog.objects.filter(
        date_published__lte=timezone.datetime(2025, 11, 21, 8, 22, 40)
    )
    context = {"blogs": blogs}
    return render(request, "blog.html", context=context)


def blog_detail(request, title):
    blog = models.blog.objects.get(title=title)
    blog.view_count += 1
    blog.save()
    context = {"blog": blog}
    return render(request, "blog_detail.html", context=context)
