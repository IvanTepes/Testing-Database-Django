# Generated by Django 3.0.1 on 2021-01-25 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0008_auto_20210125_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='name',
            field=models.CharField(default='of Specification!', max_length=254),
        ),
        migrations.AlterField(
            model_name='specification',
            name='spec_1',
            field=models.CharField(default='Unfortunately we do not have any specification for this product. ', max_length=254),
        ),
        migrations.AlterField(
            model_name='specification',
            name='spec_1_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_1_names', to='setup.Spec'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='specification_for',
            field=models.CharField(default='Motherboard, Graphic Card, etc. ', max_length=254, null=True),
        ),
    ]
