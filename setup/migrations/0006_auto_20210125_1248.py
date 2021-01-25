# Generated by Django 3.0.1 on 2021-01-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0005_auto_20210124_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='friendly_name',
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='feature',
            name='name',
            field=models.CharField(default='FeatureName', max_length=254),
        ),
        migrations.AlterField(
            model_name='keyfeatures',
            name='feature_for',
            field=models.CharField(blank=True, default='Motherboard, Graphic Card etc. ', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='keyfeatures',
            name='name',
            field=models.CharField(default='ProductCategory Features', max_length=254),
        ),
    ]
