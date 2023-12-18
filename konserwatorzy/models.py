from django.db import models

class Zadanie(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.CharField(max_length=2000)
    data_postu = models.DateField()

    Stan = models.CharField(choices={
        'wykonane': 'wykonane',
        'w_trakcie': 'w trakcie',
        'oczekujace': 'oczekujące',
    }, default='wykonane', max_length=10)

