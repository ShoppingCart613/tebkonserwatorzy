from django.db import models

class zadanie(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.CharField(max_length=2000)
    data_postu = models.DateField()

    Stan = models.CharField(choices=(
        'wykonane',
        'w trakcie',
        'oczekujące'
    ), max_length=1)

