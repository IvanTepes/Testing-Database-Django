# Generated by Django 3.0.1 on 2021-01-25 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_product_testspec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='testSpec',
        ),
    ]
