from django.db import models
from apps.phones.models import Phone
from apps.users.models import User


class Review(models.Model):
    class RatingChoice(models.IntegerChoices):
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name="phone_reviews")
    comment = models.CharField(max_length=500, verbose_name="Отзыв")
    rating = models.IntegerField(choices=RatingChoice.choices, verbose_name="Оценка")
    published_date = models.DateField(auto_created=True, verbose_name="Дата")
    is_active = models.BooleanField(default=True, verbose_name="Активный")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_reviews")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ('-id',)

    def __str__(self):
        return str(self.phone)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        phone_obj = Phone.objects.get(id=self.phone.id)
        ratings = Review.objects.filter(phone=phone_obj).values('rating')
        ls = []
        for i in ratings:
            ls.append(i['rating'])
        ratings = sum(ls) / len(ls)
        phone_obj.ratings = ratings
        phone_obj.save()


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_favorite")
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name="phone_favorite")

    def __str__(self):
        return f"{self.user} - {self.phone}"




