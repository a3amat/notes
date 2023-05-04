from django.db import models


class Article(models.Model):

    class Meta:
        db_table = 'article'
        
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name