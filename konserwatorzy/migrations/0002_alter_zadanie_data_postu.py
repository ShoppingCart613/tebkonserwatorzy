# Generated by Django 5.0 on 2024-01-09 02:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konserwatorzy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zadanie',
            name='data_postu',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 9, 2, 16, 7, 349043, tzinfo=datetime.timezone.utc)),
        ),
    ]