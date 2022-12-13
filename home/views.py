from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    context={}
    posts=Post.objects.all()
    context['posts']=posts
    return render(request,'home/index.html',context)
