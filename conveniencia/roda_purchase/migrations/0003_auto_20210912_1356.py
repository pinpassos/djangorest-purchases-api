# Generated by Django 3.2.6 on 2021-09-12 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roda_purchase', '0002_rename_cod_purchase_purchase_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='purchase',
        ),
        migrations.AddField(
            model_name='product',
            name='sku_purchase',
            field=models.ManyToManyField(related_name='purchased', to='roda_purchase.Purchase'),
        ),
    ]
