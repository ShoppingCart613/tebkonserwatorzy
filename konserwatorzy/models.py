from django.db import models

class zadanie(models.Model):
    nazwa = models.CharField(max_length=40)
    opis = models.CharField(max_length=200)
    data_postu = models.DateField()