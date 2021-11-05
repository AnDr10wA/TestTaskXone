from django.db import models
from django.conf import settings


class Link(models.Model):

    input_link = models.CharField(max_length=255, verbose_name='Входная ссылка')
    output_link = models.CharField(max_length=255, verbose_name='Сокращенная ссылка', unique=True)
    date_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)




