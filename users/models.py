from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Создан новый класс CustomUser, который является подклассом AbstractBaseUser.
    Добавлены поля для электронной почты, is_staff, is_active и date_joined.
    Установлен USERNAME_FIELD - который определяет уникальный идентификатор для модели пользователя - на электронную почту
    Указано, что все объекты для класса поступают из CustomUserManager
    """

    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
