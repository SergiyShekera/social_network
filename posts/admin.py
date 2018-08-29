from django.contrib import admin
from .models import Post


class Post_Admin(admin.ModelAdmin):

    list_display = ['creater','name', 'text']


admin.site.register(Post, Post_Admin)