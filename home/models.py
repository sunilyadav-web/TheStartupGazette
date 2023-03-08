from django.db import models
from ckeditor.fields import RichTextField

from .enum import StatusEnum
from .utils import *
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name ", unique=True)
    description = models.CharField(max_length=250, verbose_name="Category Description")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=600, unique=True)
    image = models.ImageField(upload_to='post_images', null=True, default="../static/img/deafult.jpg")
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="post")
    meta_description = models.TextField(blank=True, null=True)
    meta_keyword = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=1000, unique=True, null=True, blank=True)
    status = models.CharField(choices=StatusEnum.choices, default=StatusEnum.DRAFT, max_length=10)
    publish_date = models.DateTimeField()
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    @property
    def image_url(self):
        try:
            URL = self.image.url
        except:
            URL = ''
        return URL

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        s = generate_slug(self.title)
        self.slug = s
        super(Post, self).save(*args, **kwargs)


class Slider(models.Model):
    caption = models.CharField(max_length=70)
    link = models.CharField(max_length=300)
    image = models.ImageField(upload_to='slider_images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Created On")
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.caption

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Featured(models.Model):
    link = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Featured At')
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        try:
            split = self.link.split('/')
            slug = split[-1]
            obj = Post.objects.get(slug=slug)
        except:
            obj = 'Enter a Valid Link-'
        return str(obj)


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Full Name')
    email = models.EmailField()
    phone_no = models.IntegerField(verbose_name='Phone No')
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Featured At')
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.name}  Email - {self.email}"
