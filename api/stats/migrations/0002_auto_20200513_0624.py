# Generated by Django 3.0.6 on 2020-05-13 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infectionstats',
            name='infected',
        ),
        migrations.AddField(
            model_name='infectionstats',
            name='current_infected',
            field=models.PositiveIntegerField(default=0, verbose_name='現在感染者数'),
        ),
        migrations.AddField(
            model_name='infectionstats',
            name='new_infected',
            field=models.PositiveIntegerField(default=0, verbose_name='新規感染者数'),
        ),
        migrations.AddField(
            model_name='infectionstats',
            name='total_infected',
            field=models.PositiveIntegerField(default=0, verbose_name='累計感染者数'),
        ),
    ]