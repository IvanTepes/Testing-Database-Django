# Generated by Django 3.0.1 on 2021-01-23 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_product_has_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_logo_extra',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='brand',
            name='brand_logo_secundary',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]