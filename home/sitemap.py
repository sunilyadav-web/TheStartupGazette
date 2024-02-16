from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import *


class StaticViewSitemap(Sitemap):
    priority = 0.6

    def items(self):
        urls = ['home:home', 'home:about_us', 'home:search', 'home:term_and_condition', 'home:privacy_policy']
        return urls

    def location(self, item):
        return reverse(item)


class PostSiteMap(Sitemap):
    priority = 0.6

    def items(self):
        return Post.objects.all()

    def location(self, item):
        lastmod = item.updated_at
        return '/post/%s' % item.slug

    def get_latest_lastmod(self):
        return super().get_latest_lastmod()


class CategorySiteMap(Sitemap):
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def location(self, item):
        return '/category/%s' % item.name


class TagSiteMap(Sitemap):
    priority = 0.6

    def items(self):
        return Tag.objects.all()

    def location(self, item):
        return '/tag/%s' % item.name
