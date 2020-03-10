from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint


class User(AbstractUser):
    birthday = models.DateField()
    number = models.PositiveSmallIntegerField(editable=False)

    def save(self, *args, **kwargs):
        if not self.number:
            self.number = randint(1, 100)
        super().save(*args, **kwargs)
