from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'publish', 'status')
    list_filter = ('user', 'publish', 'status')
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

