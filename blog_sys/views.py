from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from blog_sys.models import *
from pure_pagination import PageNotAnInteger, Paginator
# the package use to auto paging


# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by("-blog_publish_time")
    return render(request, 'home.html', {'blogs': blogs})


def index(request):
    return render(request, 'index.html')


# test account and password:1, 11;2, 22;3, 33
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        try:
            user_obj = Author.objects.get(author_name=name)
            password = user_obj.author_password
            if check_password(pwd, password):
                blogs = Blog.objects.filter(blog_author__author_name=name)
                # don't use blog_author to filter, need use it
                return render(request, 'index.html', {"user_name": name, "blogs": blogs})
            return HttpResponse('name or password error')
        except Exception as e:
            return HttpResponse('no user,please check name')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        re_pwd = request.POST.get('re_pwd')
        email = request.POST.get('email')
        if name and pwd and re_pwd:
            if pwd == re_pwd:
                user_obj = Author.objects.filter(author_name=name).first()
                if user_obj:
                    return HttpResponse('user exist')
                else:
                    pwd = make_password(pwd)
                    Author.objects.create(author_name=name, author_password=pwd, author_email=email).save()
                    return render(request, 'index.html', {"user_name": name})
            else:
                return HttpResponse('twice password is not same')
        else:
            return HttpResponse('can not have empty in name and password')



