from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    creater = models.ForeignKey(User,
                                verbose_name="Создатель",
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    text = models.TextField(blank=True, verbose_name="Текст")
    date = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:

        verbose_name = "Пост"
        verbose_name_plural = "Посты"
