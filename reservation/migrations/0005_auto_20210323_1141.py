# Generated by Django 3.1.7 on 2021-03-23 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_auto_20210323_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
