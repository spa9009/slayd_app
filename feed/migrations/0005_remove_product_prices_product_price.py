# Generated by Django 5.1.1 on 2024-09-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_rename_price_product_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prices',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
