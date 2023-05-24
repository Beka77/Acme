from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    gender = models.CharField(
        max_length = 55,
        verbose_name = 'Пол',
        blank = True, null = True,
    )
    profile_image = models.ImageField(
        upload_to = 'profile_image/', 
       verbose_name = 'Изображение профиля',
       blank = True, null = True,
       default = None ,
    )
    age = models.CharField(
        verbose_name = 'Возраст',
        max_length = 10,
        blank = True, null = True,
    )
    def __str__(self):
        return f"{self.username}"
    