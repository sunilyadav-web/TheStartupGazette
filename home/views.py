from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

# =========Home Page================
def home(request):
    context={}
    posts=Post.objects.filter(status=1)
    context['posts']=posts
    return render(request,'home/index.html',context)

# =======Post Detail Page=============
def post(request,slug):
    context={}
    try:
        check=Post.objects.filter(slug=slug).exists()
        if check:
            post=Post.objects.get(slug=slug)
            context['post']=post
        else:
            messages.error(request,'Post not found!!')
    except Exception as e:
        print('Post Detail Exception: ',e)
        messages.warning(request,'Something went wrong!')
        return redirect('home:home')
    return render(request,'home/post.html',context)

# ===========Filter Category===========
def categoryFilter(request,name):
    context={}
    try:
        check=Category.objects.filter(name=name).exists()
        if check:
            category_obj=Category.objects.get(name=name)
            queryset=Post.objects.filter(category=category_obj)
            posts=queryset.filter(status=1)
            context['posts']=posts
            context['category']=name
        else:
            messages.warning(request,'This '+name+' Category Not Found!')
    except Exception as e:
        print('Category Filter Exception : ',e)
        messages.error(request,'Somthing went Wrong!')
    return render(request,'home/category.html',context)

# =========Contact Page ===========
def contact(request):
    context={}
    try:
        pass
    except Exception as e:
        print("Contact Exception : ",e)
    return render(request,'home/contact.html',context)

# ============About us Page============
def aboutUs(request):
    context={}
    try:
        pass
    except Exception as e:
        print('About us Exception : ',e)
    return render(request,'home/about_us.html',context)
