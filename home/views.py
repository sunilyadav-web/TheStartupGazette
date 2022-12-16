from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Q

# =========Home Page================
def home(request):
    context={}
    posts=Post.objects.filter(status=1)
    latestPosts=posts
    print(latestPosts)
    context['topics']=Tag.objects.all()
    context['posts']=posts

    return render(request,'home/index.html',context)

# =======Post Detail Page=============
def post(request,slug):
    context={}
    try:
        context['topics']=Tag.objects.all()
        check=Post.objects.filter(slug=slug).exists()
        if check:
            post=Post.objects.get(slug=slug)
            context['post']=post
        else:
            print('Post not found slug-',slug)
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
        context['topics']=Tag.objects.all()
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

# ==============Tag Filter==========
def tagFilter(request,tag_name):
    context={}
    try:
        print('tag name ',tag_name)
        context['topics']=Tag.objects.all()
        check=Tag.objects.filter(name=tag_name).exists()
        print('tag status : ',check)
        if check:
            tag_obj=Tag.objects.get(name=tag_name)

            queryset=Post.objects.filter(tag=tag_obj)
            posts=queryset.filter(status=1)
            print('tag posts : ',posts)
            context['posts']=posts
            context['tag']=tag_name
        else:
            messages.warning(request,'Topic Not Found! '+tag_name)
    except Exception as e:
        print("Tag Exception : ",e)
    return render(request,'home/tag.html',context)


# =========Contact Page ===========
def contact(request):
    context={}
    try:
        context['topics']=Tag.objects.all()
    except Exception as e:
        print("Contact Exception : ",e)
    return render(request,'home/contact.html',context)

# ============About us Page============
def aboutUs(request):
    context={}
    try:
        context['topics']=Tag.objects.all()
    except Exception as e:
        print('About us Exception : ',e)
    return render(request,'home/about_us.html',context)


# =============Search Functionality===============
def search(request):
    context={}
    try:
        context['topics']=Tag.objects.all()
        query=request.GET.get('q')
        print(query)
        if query:
            context['query']=query
            checkquery=list(query)

            if len(query)>78:
                messages.warning(request,'Query length cannot be greater than 77 characters')
                context['posts']=Post.objects.none()

            elif len(query) == checkquery.count(' '):
                messages.warning(request,'Query cannot be empty!')
                context['posts']=Post.objects.none()

            else:

                posts=Post.objects.filter(status=1)
                queryset=posts.filter(Q(title__icontains=query) | Q(content__icontains=query) ).order_by('-publish_date')
            
                context['posts']=queryset
                context['querysetLength']=queryset.count()
                if queryset.count() < 1:
                    messages.warning(request,'Query not found '+query)

        else:
            messages.warning(request,'Query cannot be empty. Please define something!')
            context['posts']=Post.objects.none()

    except Exception as e:
        print('Search Exception : ',e)
        messages.error(request,'Something went wrong!')
    return render(request,'home/search.html',context)

def termAndCondition(request):
    context={}
    try:
        context['topics']=Tag.objects.all()
    except Exception as e:
        print("Term and Condition Exception : ",e)
    return render(request,'home/term_condition.html',context)

def privacyPolicy(request):
    context={}
    try:
        context['topics']=Tag.objects.all()
    except Exception as e:
        print('Privacy Policy Exception : ',e)
    return render(request,'home/privacy_policy.html',context)

    