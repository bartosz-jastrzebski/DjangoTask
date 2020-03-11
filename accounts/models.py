from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from random import randint


class User(AbstractUser):
    birthday = models.DateField(null=True)
    number = models.PositiveSmallIntegerField(editable=False, blank=False, null=True)

    def get_absolute_url(self):
        return reverse('accounts:detail', kwargs={'username': self.username})

    def save(self, *args, **kwargs):
        if not self.number:
            self.number = randint(1, 100)
        super().save(*args, **kwargs)
