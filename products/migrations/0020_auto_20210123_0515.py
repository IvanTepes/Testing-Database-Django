# Generated by Django 3.0.1 on 2021-01-23 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20210123_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='extra_logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='extra_logo', to='products.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer_logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manufacturer_logo', to='products.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='processor_brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='processor_brand', to='products.Brand'),
        ),
    ]
