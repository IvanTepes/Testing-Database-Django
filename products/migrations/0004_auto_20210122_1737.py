# Generated by Django 3.0.1 on 2021-01-22 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210122_0508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['name'], 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='memory',
            options={'verbose_name_plural': 'Memorys'},
        ),
    ]
