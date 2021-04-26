from django.db import models


class FieldDataType(models.TextChoices):
    TEXT ='text'
    NUMBER = 'number'
    DATE = 'date',
    ENUM = 'enum'
