# Generated by Django 5.1.8 on 2025-04-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product__trigger_scrape_product_trigger_scrape'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
