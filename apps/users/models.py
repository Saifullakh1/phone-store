from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email is None:
            raise TypeError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    username = None
    name = models.CharField(
        max_length=150, verbose_name="Имя"
    )
    email = models.EmailField(
        unique=True, verbose_name="Почта"
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Активный"
    )
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

