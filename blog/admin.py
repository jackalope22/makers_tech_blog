from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_field = ('name', 'email', 'body')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)   

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_field = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)