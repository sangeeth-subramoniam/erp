# Generated by Django 3.1.7 on 2021-04-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0009_auto_20210325_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='day',
            field=models.IntegerField(default=7),
        ),
    ]