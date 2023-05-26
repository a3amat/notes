from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):

    class Meta:
        db_table = 'article'
        ordering = ["-id"]
        verbose_name = u"статью"
        verbose_name_plural = u"статьи"
        
    name = models.CharField(verbose_name="Название статьи", max_length=255)
    description = models.TextField(verbose_name="Текст", blank = True)
    create_date = models.DateTimeField(verbose_name="Время создания", auto_now_add=True, editable=False)
    update_date = models.DateTimeField(verbose_name="Время последнего изменения", auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name="Автор")

    def __str__(self):
        return '{} '' : '' {}'.format(self.id, self.name)
    
    