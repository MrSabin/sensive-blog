from django.contrib import admin

from blog.models import Comment, Post, Tag

admin.site.register(Tag)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ["author"]
    list_display = ["author", "text", "post"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ["author", "likes", "tags"]
