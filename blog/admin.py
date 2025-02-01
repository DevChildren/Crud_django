from django.contrib import admin
from .models import Category, Post, Comment, Like, Tag, Profile, Newsletter

# Registrasi Model ke Admin Panel
admin.site.register(Category)
admin.site.register(Newsletter)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(Profile)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'post', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('user__username', 'text')



