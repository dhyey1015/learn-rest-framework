# Generated by Django 5.1 on 2024-09-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='search',
            field=models.BooleanField(default=True),
        ),
    ]
