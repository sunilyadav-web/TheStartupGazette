from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import *

class StaticViewSitemap(Sitemap):
    def items(self):
        urls= ['home:home','home:aboutus','home:search','home:term-and-condition','home:privacy-policy']
        return urls   
        
    def location(self, item):
        return reverse(item)

class PostSiteMap(Sitemap):
    def items(self):
        return Post.objects.all()
    
    def location(self,item):
        return '/post/%s' % (item.slug)

class CategorySiteMap(Sitemap):
    def items(self):
        return Category.objects.all()

    def location(self,item):
        return '/category/%s' %(item.name)
    
class TagSiteMap(Sitemap):
    def items(self):
        return  Tag.objects.all()
    
    def location(slef,item):
        return '/tag/%s'%(item.name)