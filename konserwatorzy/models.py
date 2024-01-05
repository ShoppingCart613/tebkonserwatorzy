from django.db import models
from django.utils import timezone

class Zadanie(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.CharField(max_length=2000)
    data_postu = models.DateTimeField(default=timezone.now())

    stan = models.CharField(choices={
        'wykonane': 'wykonane',
        'w_trakcie': 'w trakcie',
        'oczekujace': 'oczekujące',
    }, default='wykonane', max_length=10)

    def __str__(self):
        return self.nazwa

