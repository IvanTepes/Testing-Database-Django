# Generated by Django 3.0.1 on 2021-01-25 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_remove_product_testspec'),
        ('setup', '0007_testspec'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='SpecName', max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Spec',
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='SpecificationName', max_length=254)),
                ('specification_for', models.CharField(default='Motherboard, Graphic Card etc. ', max_length=254, null=True)),
                ('spec_1', models.CharField(blank=True, max_length=254)),
                ('spec_2', models.CharField(blank=True, max_length=254)),
                ('spec_3', models.CharField(blank=True, max_length=254)),
                ('spec_4', models.CharField(blank=True, max_length=254)),
                ('spec_5', models.CharField(blank=True, max_length=254)),
                ('spec_6', models.CharField(blank=True, max_length=254)),
                ('spec_7', models.CharField(blank=True, max_length=254)),
                ('spec_8', models.CharField(blank=True, max_length=254)),
                ('spec_9', models.CharField(blank=True, max_length=254)),
                ('spec_10', models.CharField(blank=True, max_length=254)),
                ('spec_11', models.CharField(blank=True, max_length=254)),
                ('spec_12', models.CharField(blank=True, max_length=254)),
                ('spec_13', models.TextField(blank=True)),
                ('spec_14', models.TextField(blank=True)),
                ('spec_15', models.TextField(blank=True)),
                ('spec_10_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_10_names', to='setup.Spec')),
                ('spec_11_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_11_names', to='setup.Spec')),
                ('spec_12_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_12_names', to='setup.Spec')),
                ('spec_13_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_13_names', to='setup.Spec')),
                ('spec_14_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_14_names', to='setup.Spec')),
                ('spec_15_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_15_names', to='setup.Spec')),
                ('spec_1_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_1_names', to='setup.Spec')),
                ('spec_2_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_2_names', to='setup.Spec')),
                ('spec_3_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_3_names', to='setup.Spec')),
                ('spec_4_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_4_names', to='setup.Spec')),
                ('spec_5_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_5_names', to='setup.Spec')),
                ('spec_6_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_6_names', to='setup.Spec')),
                ('spec_7_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_7_names', to='setup.Spec')),
                ('spec_8_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_8_names', to='setup.Spec')),
                ('spec_9_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spec_9_names', to='setup.Spec')),
            ],
            options={
                'verbose_name_plural': 'Specification',
            },
        ),
        migrations.DeleteModel(
            name='TestSpec',
        ),
    ]
