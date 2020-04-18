from django.contrib import admin
from comments.models import CommentInfo


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_content', 'comment_create_time', 'order')


admin.site.register(CommentInfo, CommentAdmin)
