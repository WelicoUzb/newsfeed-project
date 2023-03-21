from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title' , 'category' , 'publish' , 'status']
    list_filter = ['status' , 'created' , 'publish']
    date_hierarchy = 'publish'
    search_fields = ['title' , 'body']
    ordering = ['status' , 'publish']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'direction']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'email' , 'text']