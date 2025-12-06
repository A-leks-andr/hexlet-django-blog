from django.db import models

# Create your models here.


class Article(models.Model):
    name = models.CharField(
        max_length=200, verbose_name="Заголовок", unique=True
    )  # название статьи
    body = models.TextField(verbose_name="Текст статьи")  # тело статьи
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
