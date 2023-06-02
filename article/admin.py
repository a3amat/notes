from django.contrib import admin
from .models import Article
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionModelAdmin


# класс обработки данных
class ArticleResource(resources.ModelResource):

    class Meta:
        model = Article

# вывод данных на странице
class ArticleAdmin(ImportExportModelAdmin):
    resource_classes = [ArticleResource]


class ArticleAdmin(ExportActionModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
     list_display = ['__str__', 'author', 'create_date', 'update_date']
     list_filter = ['create_date', 'update_date']
     search_fields = ['name', 'author', 'create_date', 'update_date']



admin.site.register(Article, ArticleAdmin)