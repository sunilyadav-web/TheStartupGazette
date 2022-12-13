from django.urls import path
from .views import *
app_name='home'
urlpatterns = [
    path('',home,name='home'),
    path('post/<slug>',post,name='post'),
    path('category/<name>',categoryFilter,name='category'),
    path('contact/',contact, name='contact'),
    path('aboutus/',aboutUs, name='aboutus'),
]
