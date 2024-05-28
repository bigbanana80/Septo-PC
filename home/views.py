from django.shortcuts import render, HttpResponse, get_object_or_404
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
    blogs = models.blog.objects.filter(publish_date__lte=timezone.now(), status=True)
    context = {"blogs": blogs}
    return render(request, "blog.html", context=context)


def blog_detail(request, title):
    blog = get_object_or_404(
        models.blog, title=title, publish_date__lte=timezone.now(), status=True
    )
    blog.view_count += 1
    blog.save()
    context = {"blog": blog}
    return render(request, "blog_detail.html", context=context)
