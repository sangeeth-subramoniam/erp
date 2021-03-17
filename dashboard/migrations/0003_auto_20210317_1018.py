# Generated by Django 3.1.7 on 2021-03-17 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0006_auto_20210315_1538'),
        ('dashboard', '0002_auto_20210317_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reciever',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_reciever', to='structure.employee'),
        ),
    ]
