# Generated by Django 3.0.1 on 2021-01-25 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0007_testspec'),
        ('products', '0029_remove_product_specifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='testSpec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Specs', to='setup.TestSpec'),
        ),
    ]
