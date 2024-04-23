from django.db import models
from apps.images.models import Image


class Phone(models.Model):
    class CompanyChoice(models.TextChoices):
        apple = "Apple"
        samsung = "Samsung"
        mi = "Mi"
        honor = "Honor"
        google = "Google"
        microsoft = "Microsoft"
        nokia = "Nokia"

    class CurrencyChoice(models.TextChoices):
        som = "Som"
        dollar = "Dollar"
        euro = "Euro"

    class ColorChoice(models.TextChoices):
        black = "Black"
        white = "White"
    class MemoryChoice(models.TextChoices):
        gb256 = "256 GB"
        gb512 = "512 GB"
        tb1 = "1 TB"
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    color = models.CharField(max_length=150, choices=ColorChoice.choices)
    memory = models.CharField(max_length=150, choices=MemoryChoice.choices)
    model = models.CharField(max_length=150, verbose_name="Модель")
    image = models.ManyToManyField(Image, related_name="phone_images", verbose_name="Картинка")
    price = models.IntegerField(default=0, verbose_name="Цена")
    currency = models.CharField(max_length=150, choices=CurrencyChoice.choices, verbose_name="Валюта")
    company = models.CharField(max_length=150, choices=CompanyChoice.choices, verbose_name="Компания")
    ratings = models.FloatField(default=0, verbose_name="Оценка")
    published = models.DateField(verbose_name="Дата выпуска")
    is_exists = models.BooleanField(default=True, verbose_name="Есть в наличии")
    is_active = models.BooleanField(default=True, verbose_name="Активный")

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"

    def __str__(self):
        return self.name

