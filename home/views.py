from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

def home(request):
    context={}
    posts=Post.objects.all()
    context['posts']=posts
    return render(request,'home/index.html',context)

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

def categoryFilter(request,category):
    context={}
    try:
        check=Category.objects.filter(name=category).exists()
        if check:
            print("Category Exits!!")
            category_obj=Category.objects.get(name=category)
            posts=Post.objects.filter(category=category_obj)
            posts=posts.filter(status=True)
            context['posts']=posts
    except Exception as e:
        print('Category Filter Exception : ',e)
    return render(request,'home/category.html',context)
