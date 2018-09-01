from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like

class Post(models.Model):

    creater = models.ForeignKey(User,
                                verbose_name="Создатель",
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    text = models.TextField(blank=True, verbose_name="Текст")
    date = models.DateTimeField("Дата создания", auto_now_add=True)
    likes = GenericRelation(Like)


    class Meta:

        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    @property
    def total_likes(self):
        return self.likes.count()