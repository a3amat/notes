from django.db import models


class Article(models.Model):

    class Meta:
        db_table = 'article'
        ordering = ["-id"]
        
    name = models.CharField(verbose_name="Название статьи", max_length=255)
    description = models.TextField(verbose_name="Текст", blank = True)
    create_date = models.DateField(verbose_name="Дата создания", auto_now=True)


    def __str__(self):
        return self.name