from django.shortcuts import (
    render,
    HttpResponse,
    get_object_or_404,
    redirect,
)
from django.template import RequestContext
from . import package, models
from . import forms as f
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import forms, authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from Septo_PC.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

# responses


def handler404(request, *args, **argv):
    response = render(request, "404.html", {}, context=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, "500.html", {}, context=RequestContext(request))
    response.status_code = 500
    return response


# Create your views here.


def not_available(request):
    return render(request, "home/not_available.html")


def index(request):
    return render(request, "home/index.html")


def cart(request):
    return render(request, "home/cart.html")


def account(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        is_auth = True
    else:
        is_auth = False
    sign_up_form = f.RegisterForm()
    login_form = f.LoginForm()
    return render(
        request,
        "home/account.html",
        {"is_auth": is_auth, "form": sign_up_form, "login": login_form},
    )


def sign_in(request):
    if request.method == "POST":
        form = f.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            try:
                user = authenticate(username=username, password=password)
            except:
                return render(
                    request, "accounts/sign_in.html", {"ObjectDoesNotExist": True}
                )
            if user is not None and not user.is_superuser:
                login(request, user)
                redirect("/")
            else:
                try:
                    username = User.objects.get(email=username)
                    user = authenticate(username=username, password=password)
                    if user is not None and not user.is_superuser:
                        login(request, user)
                        redirect("/")
                    else:
                        return HttpResponse("Error 405")
                except ObjectDoesNotExist:
                    return render(
                        request, "accounts/sign_in.html", {"ObjectDoesNotExist": True}
                    )
        else:
            return render(request, "accounts/sign_in.html", {"FailCaptcha": True})
    return render(request, "accounts/sign_in.html")


def sign_out(request):
    logout(request)
    return render(request, "accounts/sign_out.html")


def sign_up(request):
    if request.method == "POST":
        form = f.RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            pass
        else:
            return render(request, "accounts/sign_up.html", {"FailCaptcha": True})
        form = forms.UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = request.POST["email"]
            password = form.cleaned_data.get("password1")
            try:
                temp = User.objects.get(username=request.POST["username"])
                return render(request, "accounts/sign_up.html", {"UserExist": True})
            except:
                pass
            try:
                temp = User.objects.get(email=str(email))
                return render(request, "accounts/sign_up.html", {"EmailExist": True})
            except:
                pass
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            user.save()
            return render(request, "accounts/sign_up.html", {"SignUpSuccess": True})
        else:
            return render(request, "accounts/sign_up.html", {"WrongPassword": True})
    return HttpResponse("Unknown Error please contact the support.")

# TODO this bloody send email still doesn't work
def forget_password(request):
    if request.method == "POST":
        form = f.ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            user = User.objects.get(email=email)
            if user is not None:
                send_mail(
                    "Reset password",
                    f"{PasswordResetView.as_view()}",
                    EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                    auth_password=EMAIL_HOST_PASSWORD,
                )
                return HttpResponse(
                    "Please check out the email( for now check out the console)"
                )

    form = f.ForgetPasswordForm()
    return render(request, "accounts/forget_password.html", {"form": form})


def reset_password_result(request):
    if request.method == "POST":
        form = f.ResetPasswordForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            user = User.objects.get(email=email)
            if user is not None and password1 == password2 and not user.is_superuser:
                user.set_password(password1)
                user.save()
                return redirect("/")
    else:
        return HttpResponse("Error 405")


def products(request):
    return render(request, "home/products.html")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == "POST":
        form = f.ContactForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.name = "Unknown"
            p.save()
            messages.add_message(
                request, messages.SUCCESS, "ticket sended successfully ! "
            )
        else:
            messages.add_message(request, messages.ERROR, "Error, pls try again  ! ")

    form = f.ContactForm()
    return render(request, "home/contact.html", {"form": form})


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
    return render(request, "home/blog.html", context=context)


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
    return render(request, "home/blog_detail.html", context=context)


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Allow: /",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def search_blog(request):
    query = request.GET.get('search')  # Get the search query from the URL
    results = []
    if query:
        results = models.blog.objects.filter(title__icontains=query)  # Search in the title
    return render(request, 'home/search_results.html', {'results': results, 'query': query})