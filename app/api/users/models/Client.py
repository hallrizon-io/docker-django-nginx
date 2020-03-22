from django.db import models
from django.utils.crypto import get_random_string


class Client(models.Model):
    name = models.CharField(max_length=256, unique=True, help_text="Це поле буде заповнено автоматично", blank=True)

    def save(self, *args, **kwargs):
        self.name = get_random_string(length=6) if self.name == '' else self.name

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
