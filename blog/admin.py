from django.contrib import admin
from models import BlogPost, Comment, Category
from mptt.admin import MPTTModelAdmin


class CategoryAdmin(MPTTModelAdmin):
    fields = ['name', 'parent']


class ArticleInline(admin.StackedInline):
    model = Comment
    extra = 1


class BlogPostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'body', 'video', 'date', 'slug', 'image', 'category']})
    ]
    list_display = ('title', 'date', 'preview', 'slug')
    prepopulated_fields = {'slug': ['title']}
    inlines = [ArticleInline]


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
