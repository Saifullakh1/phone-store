from django.db import models


class Image(models.Model):
    image = models.FileField(upload_to="images", verbose_name="Картинка")

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

    def __str__(self):
        return str(self.id)