from django.contrib import admin
from django.db.models.query import QuerySet

from.models import Post, Author, Tag, Comment 
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter =("tags", "author", "date")
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
