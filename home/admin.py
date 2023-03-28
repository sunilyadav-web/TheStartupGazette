from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


admin.site.register(Tag, TagAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'category', 'publish_date']
    list_filter = ['status', 'category', 'publish_date']
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_no', 'message', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'phone_no']


admin.site.register(Contact, ContactAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ['caption', 'created_at']
    list_filter = ['created_at']
    search_fields = ['caption']


admin.site.register(Slider, SliderAdmin)

admin.site.register(Featured)
