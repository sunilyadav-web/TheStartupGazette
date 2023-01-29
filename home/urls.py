from django.urls import path
from .views import *
app_name='home'
urlpatterns = [
    path('',home,name='home'),
    path('**',error,name='error'),
    path('post/<slug>',post,name='post'),
    path('category/<name>',categoryFilter,name='category'),
    path('tag/<tag_name>',tagFilter,name='tag'),
    path('contact/',ContactView.as_view(), name='contact'),
    path('aboutus/',aboutUs, name='aboutus'),
    path('search/',search,name='search'),
    path('term-and-condition/',termAndCondition,name='term-and-condition'),
    path('privacy-policy/',privacyPolicy,name="privacy-policy"),
]
