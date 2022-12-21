from .models import *

def globalContext(request):
    context={}
    try:
        context['topics']=Tag.objects.all()
        context['latestPosts']=Post.objects.filter(status=1)[:3]
    except Exception as e:
        print('Global Context Processor Exception : ',e)
        
    return context