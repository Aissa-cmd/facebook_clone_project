from django.contrib import admin

from .models import User, Account, Post, Comment, Like

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
