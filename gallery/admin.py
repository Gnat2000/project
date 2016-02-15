from django.contrib import admin
from models import Album, Photo


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'slug', 'img', 'biography']})
    ]
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}
    ordering = ['title']


class PhotoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['title', 'album', 'img', 'blog_post']})
    ]
    list_display = ['title', 'album', 'img']
    ordering = ['title']
    list_filter = ['album']

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
