# Generated by Django 3.0.1 on 2021-01-25 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_remove_product_has_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='specifications',
        ),
    ]