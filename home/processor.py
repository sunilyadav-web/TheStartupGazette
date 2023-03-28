from home.models import *


def custom_processor(request):
    context = {'topics': Tag.objects.all(), 'latest_posts': Post.objects.filter(status=StatusEnum.PUBLISH)[:3]}
    return context
