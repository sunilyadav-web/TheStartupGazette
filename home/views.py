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
    except:
        print('Post Detail Exception!')
        messages.warning(request,'Something went wrong!')
        return redirect('home:home')
    return render(request,'home/post.html',context)
