# Generated by Django 3.2.6 on 2021-09-12 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('roda_purchase', '0004_auto_20210912_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchased_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
