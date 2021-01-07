from django.contrib import admin
from .models import Category, Blog, Article
    
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Article, ArticleAdmin)