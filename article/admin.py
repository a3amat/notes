from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'create_date', 'update_date']
    list_filter = ['create_date', 'update_date']




admin.site.register(Article, ArticleAdmin)

