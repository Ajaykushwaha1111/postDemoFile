from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Post,Comment,Like
@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    list_display = ('title', 'student', 'datetime','action','likes',"comments", 'views')
    list_filter = ('datetime', 'action','student')
    search_fields = ['name']
#
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('student','post','comment','status')
    list_filter = ('student', 'post', 'status')
    search_fields = ['comment']
#
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('student','post','like','status')
    list_filter = ('student','post','like','status')
    search_fields = ['post']