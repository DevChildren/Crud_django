from django.contrib import admin
from .models import Category, Post, Comment, Like, Tag, Profile, Newsletter

# Registrasi Model ke Admin Panel
admin.site.register(Category)
admin.site.register(Newsletter)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(Profile)
