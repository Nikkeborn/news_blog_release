from django.contrib import admin
from .models import Article, Tag, Startup

# admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'startup', 'created_date')
    list_filter = ('tag', 'startup')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Startup)