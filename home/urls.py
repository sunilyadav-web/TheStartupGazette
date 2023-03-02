from django.urls import path
from .views import *

app_name = "home"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('**/', error, name='error'),
    path('post/<str:slug>/', PostDetailView.as_view(), name='post'),
    path('category/<str:name>', CategoryFilterView.as_view(), name='category'),
    path('tag/<str:name>/', TagFilterView.as_view(), name='tag'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('search/', search, name='search'),
    path('term-and-condition/', TermAndConditionView.as_view(), name='term_and_condition'),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name="privacy_policy"),
]
