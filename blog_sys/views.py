from django.shortcuts import render
from blog_sys.models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def logout(request):
    return render(request, 'logout.html')
