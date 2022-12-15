from django.db import models
from ckeditor.fields import RichTextField
from .utils import *
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=100, verbose_name="Category Name ",unique=True)
    description=models.CharField(max_length=250, verbose_name="Category Description")
    created_at=models.DateTimeField(auto_now_add=True, editable=False)
    updated_at=models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(max_length=100,unique=True)
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish")
) 

class Post(models.Model):
    title=models.CharField(max_length=600, unique=True)
    image=models.ImageField(upload_to='post_images',null=True,blank=True)
    content=RichTextField()
    category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True,blank=True)
    meta_description=models.TextField(blank=True,null=True)
    meta_keyword=models.TextField(blank=True,null=True)
    slug=models.SlugField(max_length=1000, unique=True,null=True,blank=True)
    status=models.IntegerField(choices=STATUS, default=0)
    publish_date=models.DateTimeField()
    writer=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    tag=models.ForeignKey(Tag,on_delete=models.SET_NULL,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(auto_now=True, editable=False)


    @property
    def imageURL(self):
        try:
            URL=self.image.url
        except:
            URL=''
        return URL

    class Meta:
        ordering = ['-created_at']  

    def __str__(self):
        return self.title 

    def save(self,  *args, **kwargs):
        s=generate_slug(self.title)
        print('this is slug',s)
        self.slug=s
        super(Post,self).save(*args, **kwargs)



