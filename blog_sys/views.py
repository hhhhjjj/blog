from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from blog_sys.models import *
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage
# the package use to auto paging
# if error:Page' object is not iterable,need add
# def __iter__(self):
#     for i in self.object_list:
#         yield i
# in the page class

# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by("-blog_publish_time")
    paginator = Paginator(blogs, 4, 2)
    # 2 is if blog number in the next page is less than 2, it will merge in the now page.
    # get value of index
    num = request.GET.get('index', '1')
    try:
        # get number of page
        number = paginator.page(num)
    except PageNotAnInteger:
        # if input is not int, return 1 page
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'blogs':  number, 'page': number, 'paginator': paginator})


def index(request):
    user_name = request.GET.get('user_name', '')
    blogs = Blog.objects.filter(blog_author__author_name=user_name)
    return render(request, 'index.html', {"user_name": user_name, "blogs": blogs})


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
                # filter will return a <QuerySet []> if not find value,and can not spring error
                return render(request, 'index.html', {"user_name": name, "blogs": blogs})
            return HttpResponse('name or password error')
        except Exception as e:
            return HttpResponse('no user,please check name')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', )
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


def write_blog(request):
    if request.method == 'GET':
        user_name = request.GET.get('nid', '')
        all_theme_list = Theme.objects.all()
        return render(request, 'write_blog.html', {'user_name': user_name, 'all_theme_list': all_theme_list})
    if request.method == 'POST':
        blog_author = request.GET.get('nid')
        blog_author_obj = Author.objects.get(author_name=blog_author)
        blog_name = request.POST.get('blog_name')
        blog_content = request.POST.get('blog_content')
        blog_theme = request.POST.getlist('theme_name')
        blog_theme_obj = Theme.objects.get(theme_name=blog_theme[0])
        blog_read_number = 0
        Blog.objects.create(blog_author=blog_author_obj, blog_name=blog_name, blog_content=blog_content,
                            blog_read_number=blog_read_number, blog_theme=blog_theme_obj)
        blogs = Blog.objects.filter(blog_author__author_name=blog_author)
        return render(request, 'index.html', {"user_name": blog_author, "blogs":blogs})


def get_detail(request, id):
    Blog.objects.get(id=id).blog_read_number = Blog.objects.get(id=id).blog_read_number + 1
    find_blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(comment_blog__id=id)
    return render(request, 'detail.html', {'blog': find_blog, 'comments': comments})




