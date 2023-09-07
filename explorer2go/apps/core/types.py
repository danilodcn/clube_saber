from django.db import models


class FileType(models.TextChoices):
    IMAGE = 'IMAGE', 'imagem'
    VIDEO = 'VIDEO', 'video'
