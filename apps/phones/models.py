from django.db import models


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
    name = models.CharField(max_length=150, verbose_name="Название")
    model = models.CharField(max_length=150, verbose_name="Модель")
    image = models.FileField(upload_to="phone_image", verbose_name="Картинка")
    price = models.IntegerField(default=0, verbose_name="Цена")
    currency = models.CharField(max_length=150, choices=CurrencyChoice.choices, verbose_name="Валюта")
    company = models.CharField(max_length=150, choices=CompanyChoice.choices, verbose_name="Компания")
    published = models.DateField(verbose_name="Дата выпуска")

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"

    def __str__(self):
        return self.name

