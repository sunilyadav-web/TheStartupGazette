from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .utils import *
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin


# =========Home Page================
def home(request):
    context={}
    posts=Post.objects.filter(status=1)
    
    # ---------Getting Start Up Stories-------
    try:
        tag=Tag.objects.get(name='startup stories')
        startup_stories=posts.filter(tag=tag)[:6]
        print('Startup Stores Objects : ',startup_stories)
    except Exception as e:
        print('Home tag filter Exception : ',e)
        startup_stories=Post.objects.none()
    # ---------End Getting Start Up Stories-------


    # -----Getting Featured Posts---------
    featured_objcts=[]
    featured=Featured.objects.order_by('-created_at')[:2]

    for item in featured:
        split=item.link.split('/')
        slug=split[-1]
        print('featured slug :',slug)
        check=Post.objects.filter(slug=slug).exists()
        if check:
            object=Post.objects.get(slug=slug)
            featured_objcts.append(object)

    # ----------End Getting Featured Post--------- 

    context['featured']=featured_objcts
    context['startup_stories']=startup_stories
    context['posts']=Post.objects.filter(status=1).order_by('-publish_date')[:10]
    context['lastpost']=posts.latest('publish_date')
    context['sliders']=Slider.objects.all()

    return render(request,'home/index.html',context)

def error(request):
    return HttpResponse('Hello error')

# =======Post Detail Page=============
def post(request,slug):
    context={}
    try:
        
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
        check=Tag.objects.filter(name=tag_name).exists()
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
class ContactView(SuccessMessageMixin,generic.CreateView):
    template_name='home/contact.html'
    model=Contact
    success_url='/contact/'
    fields='__all__'
    success_message=('ThanYou, Will Responde you very soon!')

# ============About us Page============
def aboutUs(request):
    context={}
    try:
       pass
    except Exception as e:
        print('About us Exception : ',e)
    return render(request,'home/about_us.html',context)


# =============Search Functionality===============
def search(request):
    context={}
    try:
        
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
                
                paginator=Paginator(queryset, 2)
                pager_number=request.GET.get('page')
                page=paginator.get_page(pager_number)
                page_range=paginator.page_range
                context['posts']=page
                context['page_range']=page_range
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
        pass
    except Exception as e:
        print("Term and Condition Exception : ",e)
    return render(request,'home/term_condition.html',context)

def privacyPolicy(request):
    context={}
    try:
        pass
    except Exception as e:
        print('Privacy Policy Exception : ',e)
    return render(request,'home/privacy_policy.html',context)

# ========SEO Robots.txt File=======
def robot(request):
    return render(request,'home/robots.txt')

