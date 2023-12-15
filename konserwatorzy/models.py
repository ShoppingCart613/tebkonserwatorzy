from django.db import models

class Zadanie(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.CharField(max_length=2000)
    data_postu = models.DateField()

    Stan = models.CharField(choices=(
        (1,'wykonane'),
        (2,'w trakcie'),
        (3,'oczekujące')
    ), max_length=1)

