# Generated by Django 3.0.8 on 2021-05-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0010_auto_20210520_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]