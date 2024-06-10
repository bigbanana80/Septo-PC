from django.shortcuts import render, HttpResponse, get_object_or_404
from . import package, models, forms
from django.utils import timezone
from django.core.paginator import Paginator


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
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = forms.ContactForm()
    return render(request, "contact.html", {"form": form})


def blog(request):
    blogs = models.blog.objects.filter(
        publish_date__lte=timezone.now(), status=True
    ).order_by("-publish_date")
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    page_num = [x + 1 for x in range(paginator.num_pages)]
    context = {
        "page_obj": page_obj,
        "page_num": page_num,
    }
    return render(request, "blog.html", context=context)


def blog_detail(request, title):
    valid_blogs = models.blog.objects.filter(
        publish_date__lte=timezone.now(), status=True
    )
    blog = get_object_or_404(
        models.blog, title=title, publish_date__lte=timezone.now(), status=True
    )
    blog.view_count += 1
    blog.save()
    try:
        next_blog = blog.get_next_by_publish_date()
        if next_blog not in valid_blogs:
            next_blog = None
    except models.blog.DoesNotExist:
        next_blog = None
    try:
        prev_blog = blog.get_previous_by_publish_date()
        if prev_blog not in valid_blogs:
            prev_blog = None
    except models.blog.DoesNotExist:
        prev_blog = None
    context = {
        "blog": blog,
        "next": next_blog,
        "prev": prev_blog,
    }
    return render(request, "blog_detail.html", context=context)
