# Generated by Django 5.0 on 2024-01-09 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zadanie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('opis', models.TextField()),
                ('data_postu', models.DateTimeField(default=datetime.datetime(2024, 1, 9, 2, 15, 56, 807536, tzinfo=datetime.timezone.utc))),
                ('stan', models.CharField(choices=[('not_done', 'not done'), ('in_progress', 'in progress'), ('done', 'done')], default='not_done', max_length=20)),
                ('waznosc', models.CharField(choices=[('malo_wazne', 'mało ważne'), ('wazne', 'ważne'), ('bardzo_wazne', 'bardzo ważne')], default='not_done', max_length=20)),
            ],
        ),
    ]
