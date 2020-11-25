from django.contrib import admin

# Register your models here.
from posts.models import Post, Comment, Tag


class PostComments(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', ]
    inlines = [PostComments, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
