# Generated by Django 3.0.6 on 2020-05-16 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_auto_20200515_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infectionstats',
            name='new_infected',
            field=models.IntegerField(default=0, verbose_name='新規感染者数'),
        ),
    ]
