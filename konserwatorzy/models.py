from django.db import models
from django.utils import timezone

class Zadanie(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.CharField(max_length=2000)
    data_postu = models.DateTimeField(default=timezone.now())

    stan = models.CharField(choices=[
        ('not_done', 'not done'),
        ('in_progress', 'in progress'),
        ('done','done'),
    ], default='not_done', max_length=20)

    def __str__(self):
        return self.nazwa

