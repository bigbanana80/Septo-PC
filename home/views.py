from django.shortcuts import render, HttpResponse
from . import package


# Create your views here.
def index(request):
    return HttpResponse(f"{package.blog.increment(11)}")
    # return render(request, "index.html")
