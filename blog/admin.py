from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from blog.models import Category, Post, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'category')
    search_fields = ['id', 'name', 'content']
    list_filter = ['status', 'category', 'created_at']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)