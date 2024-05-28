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
    all_blogs = models.blog.objects.all()
    valid_blogs = models.blog.objects.filter(publish_date__lte=timezone.now())
    for blog in all_blogs:
        if blog in valid_blogs:
            blog.status = True
            blog.save()
        else:
            blog.status = False
            blog.save()

    blogs = models.blog.objects.filter(status=True)
    context = {"blogs": blogs}
    return render(request, "blog.html", context=context)


def blog_detail(request, title):
    blog = models.blog.objects.get(title=title)
    blog.view_count += 1
    blog.save()
    context = {"blog": blog}
    return render(request, "blog_detail.html", context=context)
