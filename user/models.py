from django.db import models
from django.contrib.auth.models import User

class User_Acc(models.Model):

    user = models.ForeignKey(User, verbose_name="Юзер", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, db_index=True, verbose_name="Имя")
    last_name = models.CharField(max_length=200, db_index=True, verbose_name="Фамилия")

    class Meta:

        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

