# Generated by Django 5.1.1 on 2024-09-28 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.00, max_digits=10),
            preserve_default=False,
        ),
    ]
